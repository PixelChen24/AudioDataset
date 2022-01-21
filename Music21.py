import json

from pytube import YouTube

with open("SourceFile/Music21/MUSIC21_solo_videos.json", 'r') as f:
    source = json.load(f)
videos = source['videos']


# @TODO
'''  # system proxy (optional)
proxy_handler = {
"http": " http://127.0.0.1:10809",
'https': ' http://127.0.0.1:10809'
}'''
success = 0
fail = 0
total_cnt = 0
for key in videos.keys():
    this_type_video_list = videos[key]
    for id in this_type_video_list:
        total_cnt += 1
        video_url = "https://www.youtube.com/watch?v=" + id
        save_path = "Dataset/Music21/"
        file_name = id + "+" + str(key) + ".mp4"

        # Connect to youtube
        try:
            video = YouTube(video_url)  # not using proxy
            # video = YouTube(video_url, proxies=proxy_handler)  # using proxy
        except:
            print("** Video:  " + video_url + "  not found.**")
            fail += 1
            continue

        # Download
        try:
            print("Trying to download %s......" % id)
            video.streams.get_highest_resolution().download(output_path=save_path, filename=file_name)
        except:
            print("**Video:  " + video_url + "  download failed.**")
            fail += 1
            continue
        success += 1

print("\n\nFinished. %d of %d success, %d failed." % (success, total_cnt, fail))
