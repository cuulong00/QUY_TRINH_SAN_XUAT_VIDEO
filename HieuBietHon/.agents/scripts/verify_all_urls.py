import re
import urllib.request
import ssl

staging_file = "/Users/pro16/Documents/VideoProject/HieuBietHon/youtube_citations_staging.md"

with open(staging_file, "r", encoding="utf-8") as f:
    content = f.read()

# Extract all URLs using regex: https?://[^\s\)]+
urls = re.findall(r'https?://[^\s\)]+', content)
unique_urls = list(set(urls))

print(f"Total unique URLs to test: {len(unique_urls)}")

# Create unverified SSL context to bypass SSL cert issues if any
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

valid_urls = {}
invalid_urls = {}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

for url in unique_urls:
    # clean trailing punctuation if any
    clean_url = url.rstrip('.,;')
    try:
        req = urllib.request.Request(clean_url, headers=headers, method='HEAD')
        with urllib.request.urlopen(req, context=ctx, timeout=5) as resp:
            if resp.status == 200 or resp.status == 301 or resp.status == 302:
                valid_urls[url] = resp.status
            else:
                invalid_urls[url] = f"Status code {resp.status}"
    except Exception as e:
        # try GET if HEAD fails
        try:
            req = urllib.request.Request(clean_url, headers=headers, method='GET')
            with urllib.request.urlopen(req, context=ctx, timeout=5) as resp:
                valid_urls[url] = resp.status
        except Exception as e2:
            invalid_urls[url] = str(e2)

print("\n--- VALID (200 OK / REDIRECT) ---")
for u, s in valid_urls.items():
    print(f"✅ [{s}] {u}")

print("\n--- INVALID / HALLUCINATED / DEAD (404 / ERROR) ---")
for u, err in invalid_urls.items():
    print(f"❌ [{err}] {u}")
