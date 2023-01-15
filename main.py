from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)

# Getting the highest res available
yd = yt.streams.get_highest_resolution()

# Download & path for saving the video
yd.download('C:/Users/emilh/Desktop/Downloaded Videos')


# Open terminal:
# py main.py "[YOUTUBE VIDEO LINK]"

