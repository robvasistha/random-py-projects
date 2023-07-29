from pytube import Playlist
import os

#Simple program that uses pytube lib to allow user to download entire playlist as mp3 in one step

link = input("Enter YT playlist URL: ")

pl = Playlist(link)

for video in pl.videos:
    out_file = video.streams.get_audio_only().download(r"<your folder destination path here>")
    print("Got Audio from video: ", video.title)
    base, ext = os.path.splitext(out_file)
    audio_file = base + '.mp3'
    os.rename(out_file,audio_file)
    print("Saved as MP3!")

print("Playlist downloaded successfully!")