import pytube

def Download(url):
    video = pytube.YouTube(url)
    video_stream = video.streams.get_highest_resolution()
    return video_stream