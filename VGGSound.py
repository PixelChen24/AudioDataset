import os

import numpy as np
import pandas as pd
from moviepy.editor import *
from pytube import YouTube

source = np.array(pd.read_csv("SourceFile/VGGSound/vggsound.csv"))
length = len(source)
success = 0
fail = 0

# @TODO
'''  # system proxy (optional)
proxy_handler = {
"http": " http://127.0.0.1:10809",
'https': ' http://127.0.0.1:10809'
}'''
last = False  # 记录是否为最后一条
# @TODO
start = 0
end = length

# download video whose serial number is in range [start,end)
for i in range(start, end):
    line = source[i]
    id = line[0]  # Youtube ID
    start_seconds = int(line[1])  # valid start second
    label = line[2]  # label
    split = line[3]  # train/split
    if i == end - 1:  # 判断是不是最后一条记录
        last = True
    if not last:
        next_id = source[i + 1][0]  # 下一条的视频id
        next_start_seconds = int(source[i + 1][1])
    video_url = "https://www.youtube.com/watch?v=" + id
    save_path = "Dataset/VGGSound/" + split + '/'
    file_name = id + ".mp4"

    try:  # Link to youtube server
        video = YouTube(video_url)  # not using proxy
        # video = YouTube(video_url, proxies=proxy_handler)  # using proxy
    except:
        print("**No." + str(i) + "  video:  " + video_url + "  not found.**")
        fail += 1
        continue

    # Download
    try:
        print("Trying to download %s......" % id)
        video.streams.get_highest_resolution().download(output_path=save_path, filename=file_name)
    except:
        print("**No." + str(i) + "  video:  " + video_url + "  download failed.**")
        fail += 1
        continue

    file_path = save_path + file_name
    # cut
    if next_id == id:  # 如果出现一个视频中后面将出现不同乐器，那么此次拆分区间为[start_seconds,next_start_seconds)
        source_file = VideoFileClip(file_path)
        cut_file = source_file.subclip(t_start=start_seconds, t_end=next_start_seconds)  # 裁剪视频
        cut_file.write_videofile(save_path + str(i) + "+" + label + ".mp4")
        source_file.reader.close()
    elif next_id != id or last:  # 如果一个视频里只出现一个乐器，或者这条记录是一个视频中最后一种乐器，那么裁剪范围为[start_seconds,)
        source_file = VideoFileClip(file_path)
        cut_file = source_file.subclip(t_start=start_seconds)
        cut_file.write_videofile(save_path + str(i) + "+" + label + ".mp4")
        source_file.reader.close()
        os.remove(file_path)
    success += 1
    print("************No. %d success!************"%i)

print("\n\nFinished. %d of %d success, %d failed." % (success, end - start, fail))
