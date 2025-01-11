import streamlit as st
from app.video_downloader import download_video
import os

st.title("Video Downloader")
st.markdown("Wprowadź URL, aby pobrać filmy z YouTube lub Reels z Instagrama!")

tab1, tab2 = st.tabs(["YouTube", "Instagram"])

with tab1:
    st.header("YouTube Video Downloader")
    url = st.text_input("Wprowadź URL filmu z YouTube:")
    resolution = st.selectbox("Wybierz rozdzielczość:", ["360p", "480p", "720p", "1080p"])
    download_button = st.button("Pobierz YouTube Video", key="youtube_download")

    if download_button:
        if not url:
            st.error("Proszę wprowadzić prawidłowy URL.")
        else:
            st.info("Rozpoczynam pobieranie...")
            download_dir = "downloads/youtube"
            file_path = download_video(url, resolution, download_dir, platform="YouTube")
            if file_path:
                with open(file_path, "rb") as f:
                    st.download_button(
                        label="Pobierz film",
                        data=f,
                        file_name=os.path.basename(file_path),
                        mime="video/mp4",
                    )
                st.success("Film został pobrany! Kliknij przycisk, aby pobrać go na swoje urządzenie.")

with tab2:
    st.header("Instagram Reels Downloader")
    insta_url = st.text_input("Wprowadź URL rolki z Instagrama:")
    download_button_insta = st.button("Pobierz Instagram Reel", key="instagram_download")

    if download_button_insta:
        if not insta_url:
            st.error("Proszę wprowadzić prawidłowy URL.")
        else:
            st.info("Rozpoczynam pobieranie...")
            download_path = "downloads/instagram"
            file_path = download_video(insta_url, resolution=None, download_path=download_path, platform="Instagram")
            if file_path:
                with open(file_path, "rb") as f:
                    st.download_button(
                        label="Pobierz Reel",
                        data=f,
                        file_name=os.path.basename(file_path),
                        mime="video/mp4",
                    )
                st.success("Reel został pobrany! Kliknij przycisk, aby pobrać go na swoje urządzenie.")

st.markdown("Aplikacja stworzona przy użyciu Python, yt-dlp i Streamlit. 🚀")
