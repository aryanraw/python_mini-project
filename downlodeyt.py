from pytube import YouTube


def downlode(link):
    yt_obj = YouTube(link)
    yt_obj = yt_obj.streams.get_highest_resolution()
    try:
        yt_obj.download()
    except:
        print('an error has occurred')
    title = yt_obj.title
    print(title+'is done....')
