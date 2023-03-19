from linkFeeder import file_to_links
from downlodeyt import downlode
import time
import os
file = 'video.txt'#take the input for the web page
folder_path_output = './output'#take the input from the page

if not os.path.exists(folder_path_output):
    os.makedirs(folder_path_output)

for links in file_to_links(file):
    video_paths = downlode(links, folder_path_output)
    print(f"Downloaded videos: {video_paths}")
    time.sleep(2)