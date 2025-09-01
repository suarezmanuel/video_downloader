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

def check_status_code(video_id):
    check_url = URL_TEMPLATE.format(video_id)
    try: 
        response = session.head(check_url, allow_redirects=True, timeout=10)
        return response.status_code
    except requests.exceptions.RequestException as e:
        pass
    return None

if __name__ == "__main__": 
    total_found = 0
    last_time = time.time()
    
    with open('log.txt', 'w') as f, open('results.txt', 'w') as g:
        for video_id in range(300000, 301000):
            
            curr_time = time.time()
            time_taken = curr_time-last_time
            
            status_code = check_status_code(video_id)
            string = f'{video_id}: {status_code}. time taken : {time_taken}\n'
            
            last_time = curr_time
            
            f.write(string)
            print(string)

            if (time_taken >= 1):
                print("too much time passed, timeout?")
                f.write("too much time passed, timeout?\n")
                break
            if (status_code not in [200, 404]):
                print("new status code")
                f.write("new status code\n")
                break
            if (status_code == 200):
                g.write(f'found thumbnail: {video_id}\n')
                total_found += 1
    
    print(f'found a total of: {total_found} videos')
                