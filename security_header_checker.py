import urllib.request

def check_headers(url):
    print(f"--- Checking Security Headers for: {url} ---")
    try:
        response = urllib.request.urlopen(url)
        headers = response.info()
        
        security_headers = [
            'Strict-Transport-Security',
            'X-Frame-Options',
            'X-Content-Type-Options',
            'Content-Security-Policy'
        ]
        
        for header in security_headers:
            if header in headers:
                print(f"[PASSED] {header}: Present")
            else:
                print(f"[WARNING] {header}: Missing!")
                
    except Exception as e:
        print(f"Error checking URL: {e}")

if __name__ == "__main__":
    # Test target
    test_target = "https://www.google.com"
    check_headers(test_target)
