import requests
import time 
# 1000856gf45ie6th717atnevv2
START_ID = 300000
RANGE = 1000
OUTPUT_FILE = "video_ids.txt"
URL_TEMPLATE = "https://lemida.biu.ac.il/local/video_directory/thumb.php?id={}"

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0'})

def check_status_code(video_id):
    check_url = URL_TEMPLATE.format(video_id)
    try: 
        response = session.head(check_url, allow_redirects=True, timeout=10)
        return response.status_code
    except requests.exceptions.RequestException as e:
        pass
    return None

plot_info = []

def crawl(data_lock):
    total_found = 0
    last_time = time.time()
    last_id = -1
    
    try:
        with open('files/log.txt', 'w') as f, open('files/results.txt', 'a') as g, open('files/last_id.txt', 'r') as h:
            # so we dont repeat id's, continue from last one. 
            # assuming we will always start from START_ID for now
            line = h.readline()
            if len(line):
                # upgrade this to use 'seek', if file is big it will be problematic.
                first_id = int(line)+1
            else: 
                first_id = START_ID
                
            print(first_id)
                
            g = open('files/results.txt', 'a')
            last_id = first_id

            for video_id in range(first_id, first_id+RANGE):
                
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
                    g.write(f'{video_id}\n')
                    total_found += 1
                    with data_lock:
                        plot_info.append({'x': video_id, 'y': time_taken})
                    last_id = video_id

        print(f'found a total of: {total_found} videos')
    finally:
        with open('files/last_id.txt', 'w') as h:
            if last_id == -1: print("last_id is -1 : error")
            h.write(str(last_id))