import yt_dlp
import streamlit as st
import os

def download_video(url, resolution, download_path):
    try:
        ydl_opts = {
            'format': f'bestvideo[height<={resolution}]',
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict['title']
            
           
            file_path = os.path.join(download_path, f"{title}.mp4")
            return file_path
    except Exception as e:
        st.error(f"Wystąpił błąd: {str(e)}")
        return None


st.title("YouTube Video Downloader")
st.markdown("Wprowadź URL filmu, wybierz rozdzielczość i pobierz film na swoje urządzenie!")


url = st.text_input("Wprowadź URL filmu z YouTube:")
resolution = st.selectbox("Wybierz rozdzielczość:", ["360p", "480p", "720p", "1080p"])
download_button = st.button("Pobierz")


if download_button:
    if not url:
        st.error("Proszę wprowadzić prawidłowy URL.")
    else:
        st.info("Rozpoczynam pobieranie...")
        download_dir = "downloads"
        os.makedirs(download_dir, exist_ok=True)
        file_path = download_video(url, resolution, download_dir)
        if file_path:
            st.success("Film został pobrany!")


st.markdown("Aplikacja stworzona przy użyciu Python, yt-dlp i Streamlit. 🚀")
