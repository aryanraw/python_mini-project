from pytube import YouTube


def downlode(link):
    yt_obj = YouTube(link)
    yt_obj = yt_obj.streams.get_highest_resolution()
    try:
        yt_obj.download()
    except:
        print('an error has occurred')
    print('Downlode is completed')
    title = yt_obj.title
    return title


link = input('enter link: ')
downlode(link)
