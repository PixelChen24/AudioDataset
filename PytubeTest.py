from pytube import YouTube

# pprint-pretty print 不必要，仅仅为了让输出更好看，每个视频文件占一行
from pprint import pprint

yt = YouTube("http://www.youtube.com/watch?v=Ik-RsDGPI5Y")

resolution_list=yt.streams.order_by("resolution")
print(resolution_list)
length=len(resolution_list)
mid=(length+1)//2-1
resolution_list[mid].download()