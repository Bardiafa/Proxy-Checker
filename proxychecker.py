import concurrent.futures
import requests
import os

url = "https://www.aparat.com/"
proxysorce = "https://raw.githubusercontent.com/Bardiafa/Proxy-Leecher/main/proxies.txt" # the raw text of the leeched proxy from your github repo

pt = os.path.dirname(__file__)
good = os.path.join(pt, "good.txt")

def check(proxy):
    print(f"Checking proxy {proxy}...")
    try:
        response = requests.get(url, proxies={"http": "http://" + str(proxy), "https": "http://" + str(proxy)}, timeout=3)
        if response.status_code == 200:
            print(f"Proxy {proxy} is working!")
            with open(good, "a") as f:
                f.write(proxy + "\n")
    except (requests.exceptions.ProxyError, requests.exceptions.Timeout, requests.exceptions.ConnectTimeout):
        print(f"Proxy {proxy} is NOT working X")

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    proxylist = requests.get(proxysorce).text.splitlines()
    proxy_chunks = [proxylist[i:i+50] for i in range(0, len(proxylist), 50)]
    for chunk in proxy_chunks:
        executor.map(check, chunk)

