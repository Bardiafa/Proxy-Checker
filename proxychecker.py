import concurrent.futures
import requests
import os
import time

url = "https://www.google.com/"
proxysource = "https://raw.githubusercontent.com/Bardiafa/Proxy-Leecher/main/proxies.txt"

pt = os.path.dirname(__file__)
good = os.path.join(pt, "good.txt")

session = requests.Session()
session.headers.update({"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'})

def check(proxy, idx, total):
    try:
        response = session.get(url, proxies={"http": "http://" + str(proxy), "https": "http://" + str(proxy)}, timeout=10)
        if response.status_code == 200:
            print(f"[+ {idx}/{total}] Proxy {proxy} is working!")
            with open(good, "a") as f:
                f.write(proxy + "\n")
                
    except (requests.exceptions.ProxyError, requests.exceptions.Timeout, requests.exceptions.ConnectTimeout):
        print(f"[- {idx}/{total}] Proxy {proxy} is NOT working!")

def main():
    proxylist = requests.get(proxysource).text.splitlines()
    print(f"Total number of proxies found: {len(proxylist)}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        for idx, proxy in enumerate(proxylist, start=1):
            executor.submit(check, proxy, idx, len(proxylist))

    print("Done!")  

if __name__ == "__main__":
    main()

