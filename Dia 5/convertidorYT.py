import yt_dlp

def descargar_video(url):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

descargar_video("https://www.youtube.com/watch?v=xvFZjo5PgG0")