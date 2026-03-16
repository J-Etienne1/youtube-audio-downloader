import yt_dlp
import os

url = '/////'

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': '%(title)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])