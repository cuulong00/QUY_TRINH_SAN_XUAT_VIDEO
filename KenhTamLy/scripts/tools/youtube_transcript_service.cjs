function extractVideoId(input) {
  if (!input || typeof input !== 'string') return null;

  const trimmed = input.trim();
  if (/^[a-zA-Z0-9_-]{11}$/.test(trimmed)) return trimmed;

  try {
    const url = new URL(trimmed);

    if (url.hostname === 'youtu.be') {
      const id = url.pathname.replace(/^\//, '').split('/')[0];
      return /^[a-zA-Z0-9_-]{11}$/.test(id) ? id : null;
    }

    if (url.hostname.includes('youtube.com')) {
      const fromQuery = url.searchParams.get('v');
      if (fromQuery && /^[a-zA-Z0-9_-]{11}$/.test(fromQuery)) return fromQuery;

      const parts = url.pathname.split('/').filter(Boolean);
      const markerIndex = parts.findIndex((part) => ['embed', 'shorts', 'live'].includes(part));
      if (markerIndex >= 0 && parts[markerIndex + 1] && /^[a-zA-Z0-9_-]{11}$/.test(parts[markerIndex + 1])) {
        return parts[markerIndex + 1];
      }
    }
  } catch {
    return null;
  }

  return null;
}

function buildUrlVariants(input, videoId) {
  const variants = new Set();
  if (typeof input === 'string' && input.trim()) variants.add(input.trim());
  if (videoId) {
    variants.add(videoId);
    variants.add(`https://www.youtube.com/watch?v=${videoId}`);
    variants.add(`https://youtu.be/${videoId}`);
  }
  return Array.from(variants);
}

function decodeEntities(text) {
  return String(text || '')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&apos;/g, "'")
    .replace(/&#x([0-9a-fA-F]+);/g, (_, hex) => String.fromCodePoint(parseInt(hex, 16)))
    .replace(/&#(\d+);/g, (_, dec) => String.fromCodePoint(parseInt(dec, 10)));
}

function classifyError(error) {
  const message = String(error?.message || error || 'Unknown transcript error');
  const normalized = message.toLowerCase();

  if (normalized.includes('transcript is disabled') || normalized.includes('subtitles are disabled')) {
    return { code: 'TRANSCRIPT_DISABLED', retryable: false, message };
  }
  if (normalized.includes('no transcripts are available') || normalized.includes('could not find transcript')) {
    return { code: 'TRANSCRIPT_UNAVAILABLE', retryable: false, message };
  }
  if (normalized.includes('video is no longer available') || normalized.includes('video unavailable')) {
    return { code: 'VIDEO_UNAVAILABLE', retryable: false, message };
  }
  if (normalized.includes('captcha') || normalized.includes('too many requests') || normalized.includes('rate limit') || normalized.includes('429')) {
    return { code: 'RATE_LIMITED', retryable: true, message };
  }
  return { code: 'TRANSCRIPT_FETCH_FAILED', retryable: true, message };
}

function getPreferredLanguages(options = {}) {
  if (Array.isArray(options.languages) && options.languages.length) return options.languages;
  if (options.language) return [options.language, 'vi', 'en', 'en-US'];
  return ['vi', 'en', 'en-US'];
}

function chooseTrack(tracks, preferredLanguages) {
  if (!Array.isArray(tracks) || tracks.length === 0) return null;

  for (const lang of preferredLanguages) {
    const exactManual = tracks.find((track) => track.languageCode === lang && (!track.kind || track.kind !== 'asr'));
    if (exactManual) return exactManual;

    const exactAny = tracks.find((track) => track.languageCode === lang);
    if (exactAny) return exactAny;
  }

  const firstManual = tracks.find((track) => !track.kind || track.kind !== 'asr');
  return firstManual || tracks[0];
}

async function fetchTrackXml(trackUrl, lang) {
  const headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
  };
  if (lang) headers['Accept-Language'] = lang;

  const res = await fetch(trackUrl, { headers });
  if (!res.ok) {
    throw new Error(`No transcripts are available for this video (HTTP ${res.status})`);
  }
  return res.text();
}

function parseTranscriptXml(xml, lang) {
  const segments = [];
  const pRegex = /<p\s+t="(\d+)"\s+d="(\d+)"[^>]*>([\s\S]*?)<\/p>/g;
  let match;

  while ((match = pRegex.exec(xml)) !== null) {
    const start = parseInt(match[1], 10);
    const duration = parseInt(match[2], 10);
    const inner = match[3];

    let text = '';
    const sRegex = /<s[^>]*>([^<]*)<\/s>/g;
    let sMatch;
    while ((sMatch = sRegex.exec(inner)) !== null) {
      text += sMatch[1];
    }

    if (!text) text = inner.replace(/<[^>]+>/g, '');
    text = decodeEntities(text).replace(/\s+/g, ' ').trim();

    if (text) segments.push({ text, offset: start, duration, lang: lang || null });
  }

  if (segments.length > 0) return segments;

  const textRegex = /<text start="([^"]*)" dur="([^"]*)">([^<]*)<\/text>/g;
  while ((match = textRegex.exec(xml)) !== null) {
    const text = decodeEntities(match[3]).replace(/\s+/g, ' ').trim();
    if (text) {
      segments.push({
        text,
        offset: parseFloat(match[1]),
        duration: parseFloat(match[2]),
        lang: lang || null,
      });
    }
  }

  return segments;
}

function normalizeSegments(rawSegments) {
  const segments = (Array.isArray(rawSegments) ? rawSegments : [])
    .map((segment, index) => ({
      index,
      text: String(segment.text || '').replace(/\s+/g, ' ').trim(),
      start: Number.isFinite(Number(segment.offset)) ? Number(segment.offset) : 0,
      duration: Number.isFinite(Number(segment.duration)) ? Number(segment.duration) : 0,
      lang: segment.lang || null,
    }))
    .filter((segment) => segment.text.length > 0);

  const fullText = segments.map((segment) => segment.text).join(' ').replace(/\s+/g, ' ').trim();
  return {
    segments,
    fullText,
    segmentCount: segments.length,
    charCount: fullText.length,
    wordCount: fullText ? fullText.split(/\s+/).length : 0,
  };
}

async function fetchTranscriptViaInnerTube(videoId, preferredLanguages) {
  const clientVersion = '20.10.38';
  const body = {
    context: {
      client: {
        clientName: 'ANDROID',
        clientVersion,
      },
    },
    videoId,
  };

  const res = await fetch('https://www.youtube.com/youtubei/v1/player?prettyPrint=false', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'User-Agent': `com.google.android.youtube/${clientVersion} (Linux; U; Android 14)`,
    },
    body: JSON.stringify(body),
  });

  if (!res.ok) {
    throw new Error(`InnerTube player request failed (HTTP ${res.status})`);
  }

  const json = await res.json();
  const tracks = json?.captions?.playerCaptionsTracklistRenderer?.captionTracks;
  if (!Array.isArray(tracks) || tracks.length === 0) {
    throw new Error(`No transcripts are available for this video (${videoId})`);
  }

  const chosenTrack = chooseTrack(tracks, preferredLanguages);
  if (!chosenTrack?.baseUrl) {
    throw new Error(`No transcripts are available for this video (${videoId})`);
  }

  const xml = await fetchTrackXml(chosenTrack.baseUrl, chosenTrack.languageCode);
  const parsed = parseTranscriptXml(xml, chosenTrack.languageCode);
  if (!parsed.length) {
    throw new Error(`No transcripts are available for this video (${videoId})`);
  }

  return {
    rawSegments: parsed,
    language: chosenTrack.languageCode || null,
  };
}

async function fetchWatchPage(videoId, lang) {
  const headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
  };
  if (lang) headers['Accept-Language'] = lang;

  const res = await fetch(`https://www.youtube.com/watch?v=${videoId}`, { headers });
  const text = await res.text();

  if (text.includes('g-recaptcha')) {
    throw new Error('YouTube is receiving too many requests from this IP and now requires solving a captcha to continue');
  }
  if (!text.includes('playabilityStatus')) {
    throw new Error(`The video is no longer available (${videoId})`);
  }
  return text;
}

function parseInlineJson(html, variableName) {
  const marker = `var ${variableName} = `;
  const startIndex = html.indexOf(marker);
  if (startIndex === -1) return null;

  let jsonStart = startIndex + marker.length;
  let depth = 0;
  for (let i = jsonStart; i < html.length; i += 1) {
    if (html[i] === '{') depth += 1;
    else if (html[i] === '}') {
      depth -= 1;
      if (depth === 0) {
        try {
          return JSON.parse(html.slice(jsonStart, i + 1));
        } catch {
          return null;
        }
      }
    }
  }
  return null;
}

async function fetchTranscriptViaWatchPage(videoId, preferredLanguages) {
  const html = await fetchWatchPage(videoId, preferredLanguages[0]);
  const playerResponse = parseInlineJson(html, 'ytInitialPlayerResponse');
  const tracks = playerResponse?.captions?.playerCaptionsTracklistRenderer?.captionTracks;

  if (!Array.isArray(tracks) || tracks.length === 0) {
    throw new Error(`Transcript is disabled on this video (${videoId})`);
  }

  const chosenTrack = chooseTrack(tracks, preferredLanguages);
  if (!chosenTrack?.baseUrl) {
    throw new Error(`No transcripts are available for this video (${videoId})`);
  }

  const xml = await fetchTrackXml(chosenTrack.baseUrl, chosenTrack.languageCode);
  const parsed = parseTranscriptXml(xml, chosenTrack.languageCode);
  if (!parsed.length) {
    throw new Error(`No transcripts are available for this video (${videoId})`);
  }

  return {
    rawSegments: parsed,
    language: chosenTrack.languageCode || null,
  };
}

async function fetchTranscriptWithFallback(input, options = {}) {
  const fetchedAt = new Date().toISOString();
  const videoId = extractVideoId(input);
  const variants = buildUrlVariants(input, videoId);
  const warnings = [];
  const attempts = [];
  const preferredLanguages = getPreferredLanguages(options);

  if (!variants.length || !videoId) {
    return {
      ok: false,
      status: 'invalid_input',
      sourceBackend: 'youtube-transcript-service',
      fetchedAt,
      url: input,
      videoId: null,
      warnings,
      attempts,
      error: {
        code: 'INVALID_YOUTUBE_INPUT',
        message: 'Không nhận diện được YouTube URL hoặc video ID hợp lệ.',
        retryable: false,
      },
    };
  }

  const backendAttempts = [
    { name: 'youtubei-player', run: () => fetchTranscriptViaInnerTube(videoId, preferredLanguages) },
    { name: 'youtube-watch-page', run: () => fetchTranscriptViaWatchPage(videoId, preferredLanguages) },
  ];

  for (const backend of backendAttempts) {
    try {
      const result = await backend.run();
      const normalized = normalizeSegments(result.rawSegments);

      return {
        ok: true,
        status: 'success',
        sourceBackend: backend.name,
        fetchedAt,
        url: input,
        videoId,
        language: result.language,
        warnings,
        attempts: [...attempts, { backend: backend.name, variant: variants[0], status: 'success' }],
        ...normalized,
      };
    } catch (error) {
      const classified = classifyError(error);
      attempts.push({ backend: backend.name, variant: variants[0], status: 'failed', error: classified });

      if (!classified.retryable && classified.code === 'VIDEO_UNAVAILABLE') {
        return {
          ok: false,
          status: 'failed',
          sourceBackend: backend.name,
          fetchedAt,
          url: input,
          videoId,
          warnings,
          attempts,
          error: classified,
        };
      }
    }
  }

  const lastAttempt = attempts[attempts.length - 1];
  const finalError = lastAttempt?.error || {
    code: 'TRANSCRIPT_FETCH_FAILED',
    message: 'Không lấy được transcript sau khi thử mọi backend.',
    retryable: true,
  };

  return {
    ok: false,
    status: finalError.code === 'TRANSCRIPT_UNAVAILABLE' || finalError.code === 'TRANSCRIPT_DISABLED' ? 'no_transcript' : 'failed',
    sourceBackend: lastAttempt?.backend || 'youtube-transcript-service',
    fetchedAt,
    url: input,
    videoId,
    warnings,
    attempts,
    error: finalError,
  };
}

module.exports = {
  extractVideoId,
  fetchTranscriptWithFallback,
  classifyError,
};
