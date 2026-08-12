import yt_dlp
import os
import shutil
import glob

url = 'https://www.youtube.com/watch?v=YOUR_VIDEO_ID'  # Replace with your YouTube video URL

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': '%(title)s',
}


def find_ffmpeg():
    # 1) explicit env var
    env_loc = os.environ.get('FFMPEG_LOCATION')
    if env_loc and os.path.isdir(env_loc):
        return env_loc

    # 2) on PATH
    ff = shutil.which('ffmpeg')
    if ff:
        return os.path.dirname(ff)

    # 3) common WinGet install location
    local_appdata = os.environ.get('LOCALAPPDATA')
    if local_appdata:
        pattern = os.path.join(local_appdata, 'Microsoft', 'WinGet', 'Packages', '*ffmpeg*', '*', 'bin')
        matches = glob.glob(pattern)
        if matches:
            return matches[0]

    # 4) common Program Files locations
    for p in (r"C:\Program Files\ffmpeg\bin", r"C:\Program Files (x86)\ffmpeg\bin"):
        if os.path.isdir(p):
            return p

    return None


ffmpeg_loc = find_ffmpeg()
if ffmpeg_loc:
    ydl_opts['ffmpeg_location'] = ffmpeg_loc
    print(f"Using ffmpeg at: {ffmpeg_loc}")
else:
    print('ffmpeg not found; set FFMPEG_LOCATION or install ffmpeg')


with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])