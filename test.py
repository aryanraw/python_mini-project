import streamlit as st
from pytube import YouTube
import os

# Set Streamlit app title and page layout
st.set_page_config(page_title="YouTube Downloader", page_icon=":arrow_down:", layout="wide")

# Define Streamlit app content
def app():

    # Set app title and header
    st.title("YouTube Video Downloader")
    st.header("Enter YouTube video URLs and select locations to save the downloaded videos")

    # Create text input box for YouTube video URLs
    video_urls = st.text_area("Enter YouTube video URLs (one per line)", value="", key="urls")

    # Split the input URLs by newline and strip any leading or trailing whitespace
    urls = [url.strip() for url in video_urls.split("\n")]

    # Checks if the output file path is made or not if not it is created
    output_file_paths = './output'
    if not os.path.exists(output_file_paths):
        os.makedirs(output_file_paths)

    # Create download button to start video downloads
    if st.button("Download Videos"):

        # Loop through each video URL and download the video to the selected output file path
        for i, url in enumerate(urls):

            try:
                # Create a Pytube YouTube object
                yt = YouTube(url)

                # Get the highest resolution video stream
                stream = yt.streams.get_highest_resolution()

                # Download the video to the specified output file path
                stream.download(output_path=output_file_paths)

                # Display success message for each video
                st.success(f"Video {stream.title} downloaded successfully to {output_file_paths}")
            except:
                # Display error message if video download fails
                st.warning(f"Could not download video {stream.title} from {url}")

# Run the Streamlit app
if __name__ == "__main__":
    app()
