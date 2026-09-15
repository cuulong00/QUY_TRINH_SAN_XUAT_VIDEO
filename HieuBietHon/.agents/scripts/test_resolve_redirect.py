import urllib.request
import ssl

redirect_url = "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_5f2C8FpL7nPelEcYcTTrkLAlo7ITWYRXVvhPbMJURo6vCip43sTQ2sq5THAOTpoL7Yj-5koQHcVICjfpZOI0YYTO8cppTWoSHsYDOhOdvIhnulyc4_JXWC1TzJMpgC-kQ-LqhUCTQCs3DFhc9il0Se7YBE_vELG0lLmhsaAKOyrsvOKkwaMqdyZjB7K4CdN_"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request(redirect_url, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
})

try:
    with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
        final_url = resp.geturl()
        print(f"REAL DEEP URL RESOLVED: {final_url}")
except Exception as e:
        print(f"Error: {e}")
