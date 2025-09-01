import requests
import webbrowser
import time 
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import threading 
import functools

START_ID = 300000
END_ID = 300100
MAX_WORKERS = 100
OUTPUT_FILE = "video_ids.txt"
VIDEO_IDS = [301547,289016,295881]
URL_TEMPLATE = "https://lemida.biu.ac.il/local/video_directory/thumb.php?id={}"

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0'})

file_lock = threading.Lock()

def find_and_open_video(video_id):
    initial_url = URL_TEMPLATE.format(video_id)
    try: 
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(initial_url, allow_redirects=True, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"found a hit for id {video_id}")
            png_url = response.url
            if '.png' in png_url:
                base_url, _ = png_url.split('-5.png', 1)
                mp4_url = base_url + '.mp4'
                webbrowser.open_new_tab(mp4_url)
            else:
                print(f"redirected url for id {video_id} not a png")
        else: 
            print(f"thumbnail for id {video_id} not found")
    except requests.exceptions.RequestException as e:
        print(f"network error occured for id {video_id}: {e}")

def check_id(video_id):
    check_url = URL_TEMPLATE.format(video_id)
    try: 
        response = session.head(check_url, allow_redirects=True, timeout=10)
        if response.status_code == 200:
            with file_lock:
                with open(OUTPUT_FILE, 'a') as f:
                    f.write(f"{video_id}\n")
            return video_id
        
    except requests.exceptions.RequestException as e:
        # ignore errors, return None
        pass

    return None

host = 'brd.superproxy.io'
port = 33335
username = 'brd-customer-hl_ca6f9231-zone-datacenter_proxy1'
password = 'gtk2w57o1b1i'

proxy_url = f'http://{username}:{password}@{host}:{port}'
proxies = {
    'http': proxy_url,
    'https': proxy_url
}

session = requests.Session()
session.proxies.update(proxies)

def check_status_code(video_id):
    check_url = URL_TEMPLATE.format(video_id)
    try: 
        response = session.head(check_url, allow_redirects=True, timeout=10)
        return response.status_code
    except requests.exceptions.RequestException as e:
        pass
    return None

def print_proxy_ip():
    url = "http://lumtest.com/myip.json"
    try:
        response = session.get(url, timeout=10)
        print("Proxy IP info:", response.json())
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__": 
    total_found = 0

    print_proxy_ip()    

    for i in range(0, 100):
        print(f'{i}: {check_status_code(300000)}')
    
    # with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    #     results = executor.map(check_id, ids_to_check)
    #     for result in tqdm(results, total=len(ids_to_check), desc="scanning ids"):
    #         if results is not None:
    #             total_found += 1

    print(f"found a total of {total_found} videos")