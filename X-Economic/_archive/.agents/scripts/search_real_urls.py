import urllib.request
import urllib.parse
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def search_ddg_direct_urls(query):
    encoded_query = urllib.parse.quote(query)
    url = f"https://html.duckduckgo.com/html/?q={encoded_query}"
    req = urllib.request.Request(url, headers=headers)
    found_urls = []
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            # Extract URLs from ddg uddg parameter
            matches = re.findall(r'uddg=([^&"]+)', html)
            for m in matches:
                decoded = urllib.parse.unquote(m)
                if decoded.startswith('http') and 'duckduckgo.com' not in decoded:
                    found_urls.append(decoded)
    except Exception as e:
        print(f"Error searching DDG: {e}")
    return found_urls

# Test query for real Tuoi Tre article
urls = search_ddg_direct_urls("site:tuoitre.vn VinSpace SpaceX phong ve tinh")
print("Found Direct URLs:")
for u in urls[:5]:
    print(f"  - {u}")
