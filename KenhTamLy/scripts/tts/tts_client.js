/**
 * tts_client.js — VBEE TTS API Client Module
 * Handles: voice listing, TTS submission, status polling, and audio download.
 */
const https = require('https');
const http = require('http');
const fs = require('fs');
const path = require('path');

const CONFIG_PATH = path.join(__dirname, 'config.json');

function loadConfig() {
  return JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf-8'));
}

function saveConfig(config) {
  fs.writeFileSync(CONFIG_PATH, JSON.stringify(config, null, 2), 'utf-8');
}

/**
 * Get auth headers for VBEE API
 */
function getAuthHeaders() {
  const config = loadConfig();
  return {
    'Content-Type': 'application/json',
    'app-id': config.app_id,
    'Authorization': `Bearer ${config.token}`,
  };
}

/**
 * Generic HTTPS request helper
 */
function request(method, url, extraHeaders = {}, body = null) {
  return new Promise((resolve, reject) => {
    const parsed = new URL(url);
    const options = {
      hostname: parsed.hostname,
      port: parsed.port || 443,
      path: parsed.pathname + parsed.search,
      method,
      headers: {
        ...getAuthHeaders(),
        ...extraHeaders,
      },
    };

    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', (chunk) => (data += chunk));
      res.on('end', () => {
        try {
          resolve({ status: res.statusCode, data: JSON.parse(data) });
        } catch {
          resolve({ status: res.statusCode, data });
        }
      });
    });

    req.on('error', reject);
    if (body) req.write(JSON.stringify(body));
    req.end();
  });
}

/**
 * 1. List available voices — find "Thiện Tâm" community voice
 */
async function listVoices() {
  const config = loadConfig();
  const ownership = config.voice_ownership || 'PERSONAL';
  const url = `${config.api_base}/public/v1/voices?voiceOwnership=${ownership}&languageCode=vi-VN`;
  
  console.log(`🔍 Đang lấy danh sách giọng đọc (${ownership})...`);
  const res = await request('GET', url);
  
  if (res.status !== 200) {
    throw new Error(`Lỗi khi lấy danh sách giọng: ${res.status} — ${JSON.stringify(res.data)}`);
  }

  // VBEE API returns { result: { voices: [...], pagination: {...} } }
  if (res.data && res.data.result && Array.isArray(res.data.result.voices)) {
    return res.data.result.voices;
  }
  
  if (Array.isArray(res.data)) {
    return res.data;
  }

  return [];
}

/**
 * Find and cache voice code for "Thiện Tâm"
 */
async function resolveVoiceCode() {
  const config = loadConfig();
  
  if (config.voice_code) {
    console.log(`✅ Đã có voice_code: ${config.voice_code}`);
    return config.voice_code;
  }

  const voices = await listVoices();
  
  // Search for Thiện Tâm
  let found = null;
  const voiceList = Array.isArray(voices) ? voices : [];
  
  for (const v of voiceList) {
    const name = (v.name || v.voiceName || v.voice_name || '').toLowerCase();
    const code = v.code || v.voiceCode || v.voice_code || '';
    
    if (name.includes('thiện tâm') || name.includes('thien tam') || name.includes('thientam')) {
      found = code;
      console.log(`🎤 Tìm thấy giọng "${v.name || v.voiceName}": ${code}`);
      break;
    }
  }

  if (!found) {
    console.log('\n📋 Danh sách giọng cộng đồng:');
    for (const v of voiceList.slice(0, 20)) {
      const name = v.name || v.voiceName || v.voice_name || 'N/A';
      const code = v.code || v.voiceCode || v.voice_code || 'N/A';
      console.log(`   - ${name}: ${code}`);
    }
    throw new Error('Không tìm thấy giọng "Thiện Tâm". Hãy xem danh sách trên và cập nhật voice_code trong config.json thủ công.');
  }

  // Cache for next time
  config.voice_code = found;
  saveConfig(config);
  console.log(`💾 Đã lưu voice_code "${found}" vào config.json`);
  
  return found;
}

/**
 * 2. Submit TTS request (direct mode — returns audio_link synchronously)
 */
async function submitTTS(text, voiceCode) {
  const config = loadConfig();
  
  const body = {
    app_id: config.app_id,
    input_text: text,
    voice_code: voiceCode,
    audio_type: config.audio_type || 'mp3',
    bitrate: config.bitrate || 128,
    speed_rate: config.speed_rate || 1.0,
    response_type: 'direct',
  };

  const url = `${config.api_base}/v1/tts`;
  console.log(`📤 Đang gửi yêu cầu TTS (${text.length} ký tự)...`);
  
  const res = await request('POST', url, {}, body);
  
  if (res.status !== 200 && res.status !== 201) {
    throw new Error(`Lỗi khi gửi TTS: ${res.status} — ${JSON.stringify(res.data)}`);
  }

  // VBEE wraps response in { result: { ... }, status: 1 }
  const result = res.data.result || res.data;
  const requestId = result.request_id || result.requestId || result.id;
  const audioLink = result.audio_link || result.audio_url || result.audioUrl;
  const status = (result.status || '').toString().toUpperCase();

  if (!requestId) {
    throw new Error(`Không nhận được request_id từ API. Response: ${JSON.stringify(res.data)}`);
  }

  console.log(`📋 Request ID: ${requestId} — Status: ${status}`);
  
  if (status === 'SUCCESS' && audioLink) {
    console.log(`🔗 Audio link: ${audioLink}`);
  }

  return { requestId, audioLink, status, response: result };
}

/**
 * 3. Download audio file
 */
async function downloadAudio(audioUrl, outputPath) {
  return new Promise((resolve, reject) => {
    const dir = path.dirname(outputPath);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }

    console.log(`⬇️  Đang tải audio → ${path.basename(outputPath)}`);

    const protocol = audioUrl.startsWith('https') ? https : http;
    
    const download = (url) => {
      protocol.get(url, (res) => {
        // Handle redirects
        if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
          download(res.headers.location);
          return;
        }
        
        if (res.statusCode !== 200) {
          reject(new Error(`Download thất bại: HTTP ${res.statusCode}`));
          return;
        }

        const file = fs.createWriteStream(outputPath);
        res.pipe(file);
        file.on('finish', () => {
          file.close();
          const sizeMB = (fs.statSync(outputPath).size / 1024 / 1024).toFixed(2);
          console.log(`💾 Đã lưu: ${path.basename(outputPath)} (${sizeMB} MB)`);
          resolve(outputPath);
        });
        file.on('error', (err) => {
          fs.unlink(outputPath, () => {});
          reject(err);
        });
      }).on('error', reject);
    };
    
    download(audioUrl);
  });
}

/**
 * 4. Full TTS pipeline for a single text chunk (direct mode)
 */
async function processSingleChunk(text, voiceCode, outputPath) {
  // Submit and get audio link directly
  const { requestId, audioLink, status } = await submitTTS(text, voiceCode);
  
  if (!audioLink) {
    throw new Error(`Không lấy được audio_link cho request ${requestId}. Status: ${status}`);
  }

  // Download immediately (link may expire!)
  await downloadAudio(audioLink, outputPath);
  
  return outputPath;
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// CLI mode: list voices
if (require.main === module) {
  const args = process.argv.slice(2);
  
  if (args.includes('--list-voices')) {
    listVoices()
      .then((voices) => {
        const list = Array.isArray(voices) ? voices : [];
        console.log(`\n📋 Tổng: ${list.length} giọng cộng đồng\n`);
        for (const v of list) {
          const name = v.name || v.voiceName || v.voice_name || 'N/A';
          const code = v.code || v.voiceCode || v.voice_code || 'N/A';
          const gender = v.gender || v.voiceGender || '';
          console.log(`  🎤 ${name} (${gender}) → ${code}`);
        }
      })
      .catch(console.error);
  } else if (args.includes('--resolve-voice')) {
    resolveVoiceCode().catch(console.error);
  } else {
    console.log('Sử dụng: node tts_client.js --list-voices | --resolve-voice');
  }
}

module.exports = {
  loadConfig,
  listVoices,
  resolveVoiceCode,
  submitTTS,
  downloadAudio,
  processSingleChunk,
  sleep,
};
