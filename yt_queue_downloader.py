# yt_queue_daemon.py

from __future__ import unicode_literals
import youtube_dl

from pathlib import Path
ROOT = Path(__file__).parent.absolute()

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

def main():
    title = '%(title)s'

    ydl_opts = {
        # 'username' : 'magicbro12lego@gmail.com',
        # 'password' : 'F!r3fr01234',
        'playlist_items': 1-3,
        'outtmpl': f'{Path} / {"%(title)s"} - {"%(duration)s"}.{"%(ext)s"}',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/playlist?list=PLB-g8PA1MbZnhfRVEk6pLrdw4PHT4UCZ7'])
    


if __name__ == '__main__':
    print('Running yt_queue_daemon.py')
    main()