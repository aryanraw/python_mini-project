from pytube import YouTube

# Paste the URL of the YouTube video you want to download
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Create a YouTube object with the given URL
yt = YouTube(url)

# Get the highest resolution video stream
stream = yt.streams.get_highest_resolution()

# Download the video
stream.download()
