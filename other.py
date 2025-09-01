import requests
import webbrowser
import time 

START_ID = 0 
END_ID = 400000
MAX_WORKERS = 100
OUTPUT_FILE = "video_ids.txt"
VIDEO_IDS = [249
,747
]
URL_TEMPLATE = "https://lemida.biu.ac.il/local/video_directory/thumb.php?id={}"

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0'})

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

if __name__ == "__main__": 
    for id in VIDEO_IDS:
        find_and_open_video(id)
        time.sleep(2) # sleep for 2 seconds