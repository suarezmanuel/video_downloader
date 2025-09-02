# maybe split results.txt into files, each with 10k ids
import requests
import time 

URL_TEMPLATE = "https://lemida.biu.ac.il/local/video_directory/thumb.php?id={}"

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0'})

if __name__ == "__main__": 
    last_thumb_id = -1
    try: 
        with open('files/results.txt', 'r') as f, open('files/last_id_thumb.txt', 'r') as g:
            last_thumb_id = int(g.readline())
            lines = f.readlines()
            lines = [int(s) for s in lines]
            curr_index = lines.index(last_thumb_id)+1

            for i in range (curr_index, len(lines)):
                thumb_id = lines[i]
                check_url = URL_TEMPLATE.format(thumb_id)
                try: 
                    response = session.get(check_url, allow_redirects=True, timeout=10)
                    
                    if response.status_code == 200:
                        with open(f'./thumbnails/{thumb_id}.png', 'wb') as h:
                            h.write(response.content)
                    else:
                        print(f'failed to download thumbnail {thumb_id}')
                        
                    last_thumb_id = thumb_id
                    # write response thumbnail to thumbnails/video_id.png
                except requests.exceptions.RequestException as e:
                    print(f'exception on {thumb_id} : {e}')
    finally:
        if (last_thumb_id == -1):
            print("no new thumbnails")
        else:
            with open('files/last_id_thumb.txt', 'w') as g:
                g.write(str(last_thumb_id))