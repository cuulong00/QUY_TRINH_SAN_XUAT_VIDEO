import re
import subprocess
import json

staging_file = "/Users/pro16/Documents/VideoProject/X-Economics/youtube_citations_staging.md"

with open(staging_file, "r", encoding="utf-8") as f:
    content = f.read()

urls = list(set(re.findall(r'https?://[^\s\)]+', content)))

status_report = {}

for u in urls:
    clean_url = u.rstrip('.,;')
    # Run curl -I to check HTTP status code
    cmd = ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-L", "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36", clean_url]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        code = res.stdout.strip()
        status_report[clean_url] = code
    except Exception as e:
        status_report[clean_url] = "TIMEOUT/ERROR"

print("--- URL CHECK RESULTS ---")
real_200 = []
dead_404 = []
blocked_403 = []
other = []

for u, code in status_report.items():
    if code in ["200", "301", "302"]:
        real_200.append(u)
    elif code == "404":
        dead_404.append(u)
    elif code in ["403", "429"]:
        blocked_403.append(u)
    else:
        other.append((u, code))

print(f"\n✅ VERIFIED WORKING (200/30x): {len(real_200)}")
for u in real_200:
    print(f"  - {u}")

print(f"\n❌ DEAD / HALLUCINATED (404 Not Found): {len(dead_404)}")
for u in dead_404:
    print(f"  - {u}")

print(f"\n⚠️ BLOCKED / ANTI-BOT (403/429): {len(blocked_403)}")
for u in blocked_403:
    print(f"  - {u}")

print(f"\n❓ OTHER / TIMEOUT: {len(other)}")
for u, c in other:
    print(f"  - [{c}] {u}")
