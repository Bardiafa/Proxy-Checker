import concurrent.futures
import requests
import os

url = "https://www.aparat.com/"
proxysorce = "https://raw.githubusercontent.com/Bardiafa/Proxy-Leecher/main/proxies.txt"

pt = os.path.dirname(__file__)
good = os.path.join(pt, "good.txt")
ir = os.path.join(pt, "IR.txt")

def check(proxy):
    print(f"Checking proxy {proxy}...")
    try:
        response = requests.get(url, proxies={"http": "http://" + str(proxy), "https": "http://" + str(proxy)}, timeout=10)
        if response.status_code == 200:
            print(f"Proxy {proxy} is working!")
            try:
                cu = requests.get(f"https://ipapi.co/{proxy}/json/", timeout=10).json()
                if cu["country"] == "IR":
                    with open(ir, "a") as f:
                        f.write(proxy + "\n")        
                else:
                    with open(good, "a") as f:
                        f.write(proxy + "\n")
            except:
                with open(good, "a") as f:
                    f.write(proxy + "\n")            
    except (requests.exceptions.ProxyError, requests.exceptions.Timeout, requests.exceptions.ConnectTimeout):
        print(f"Proxy {proxy} is NOT working X")

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    proxylist = requests.get(proxysorce).text.splitlines()
    proxy_chunks = [proxylist[i:i+50] for i in range(0, len(proxylist), 50)]
    for chunk in proxy_chunks:
        executor.map(check, chunk)

