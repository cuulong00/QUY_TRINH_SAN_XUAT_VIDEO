import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Test URL from search_web grounding
test_url = "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_5f2C8FpL7nPelEcYcTTrkLAlo7ITWYRXVvhPbMJURo6vCip43sTQ2sq5THAOTpoL7Yj-5koQHcVICjfpZOI0YYTO8cppTWoSHsYDOhOdvIhnulyc4_JXWC1TzJMpgC-kQ-LqhUCTQCs3DFhc9il0Se7YBE_vELG0lLmhsaAKOyrsvOKkwaMqdyZjB7K4CdN_"

req = urllib.request.Request(test_url, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
})

try:
    # Use a custom HTTPRedirectHandler to print intermediate locations
    class RedirectLogger(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            print(f"Redirecting ({code}) to: {newurl}")
            return super().redirect_request(req, fp, code, msg, headers, newurl)

    opener = urllib.request.build_opener(RedirectLogger, urllib.request.HTTPSHandler(context=ctx))
    with opener.open(req, timeout=10) as resp:
        print(f"Final URL: {resp.geturl()}")
except Exception as e:
    print(f"Error: {e}")
