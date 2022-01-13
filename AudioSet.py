import os

import numpy as np
import pandas as pd
from moviepy.editor import *
from pytube import YouTube

source = np.array(pd.read_csv("SourceFile/AudioSet/balanced_train_segments.csv",skipinitialspace=True))
length = len(source)
success = 0
fail = 0

# @TODO
'''  # system proxy (optional)
proxy_handler = {
"http": " http://127.0.0.1:10809",
'https': ' http://127.0.0.1:10809'
}'''
# @TODO
start = 0
end = length

# download video whose serial number is in range [start,end)
for i in range(start, end):
    line = source[i]

    id = line[0]  # Youtube ID
    start_seconds = int(line[1])  # valid start second
    end_seconds= int(line[2])
    label=line[3]

    video_url = "https://www.youtube.com/watch?v=" + id
    save_path = "Dataset/AudioSet/"
    file_name = id + ".mp4"

    # Link to youtube server
    try:
        video = YouTube(video_url)  # not using proxy
        # video = YouTube(video_url, proxies=proxy_handler)  # using proxy
    except:
        print("**No." + str(i) + "  video:  " + video_url + "  not found.**")
        fail += 1
        continue

    # Download
    try:
        print("Trying to download %s......"%id)
        video.streams.get_highest_resolution().download(output_path=save_path, filename=file_name)
    except:
        print("**No." + str(i) + "  video:  " + video_url + "  download failed.**")
        fail += 1
        continue
    file_path = save_path + file_name

    # cut
    source_file = VideoFileClip(file_path)
    cut_file = source_file.subclip(t_start=start_seconds,t_end=end_seconds)
    cut_file.write_videofile(save_path + str(i)+"+"+id+ ".mp4")
    source_file.reader.close()
    success += 1
    print("************No. %d success!************"%i)
    os.remove(file_path)

print("\n\nFinished. %d of %d success, %d failed." % (success, end - start, fail))
