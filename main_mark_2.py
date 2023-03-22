import streamlit as st
from pytube import YouTube
import os

st.set_page_config(page_title="YouTube Downloader", page_icon=":arrow_down:", layout="wide")

def app():

    st.title("YouTube Video Downloader")
    st.header("Enter YouTube video URLs and select locations to save the downloaded videos")

    video_urls = st.text_area("Enter YouTube video URLs (one per line)", value="", key="urls")

    urls = [url.strip() for url in video_urls.split("\n")]

    output_file_paths = './output'
    if not os.path.exists(output_file_paths):
        os.makedirs(output_file_paths)

    if st.button("Download Videos"):

        for i, url in enumerate(urls):

            try:

                yt = YouTube(url)

                stream = yt.streams.get_highest_resolution()

                stream.download(output_path=output_file_paths)

                st.success(f"Video {stream.title} downloaded successfully to {output_file_paths}")
            except:

                st.warning(f"Could not download video {stream.title} from {url}")

if __name__ == "__main__":
    app()