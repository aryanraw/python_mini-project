from pytube import YouTube
import os


def downlode(link, folder_path):
    try:
        yt = YouTube(link)
        # Get the highest resolution video
        video = yt.streams.get_highest_resolution()
        # Download the video
        video_path = os.path.join(folder_path, f"{yt.title}.mp4")
        video.download(folder_path)
        print(f"Video downloaded successfully: {yt.title}")
        return video_path
    except Exception as e:
        print(f"Error downloading video: {yt.title}\n{str(e)}")
        return None
