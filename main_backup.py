import streamlit as st
from pytube import YouTube
import os
st.set_page_config(page_title="YouTube Downloader", page_icon=":arrow_down:", layout="wide")
st.title('YouTube Video Downloader')
url = st.text_area('Enter YouTube URL')
output_file = 'output'
if not os.path.exists(output_file):
    os.makedirs(output_file)


def downloadyt(link):
    try:
        # Create a YouTube object with the given URL
        yt = YouTube(link)

        # Get the highest resolution video stream
        stream = yt.streams.get_highest_resolution()

        # Download the video
        stream.download(output_path=output_file)
        return True
    except:
        return False


if st.button('Download Video'):
    ver = downloadyt(url)
    if ver:
        st.success("Video downloaded successfully!")
    else:
        st.warning('No links were entered.')
