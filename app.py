import yt_dlp
import streamlit as st
import os
import re

def clean_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def download_video(url, resolution, download_path, platform="YouTube"):
    try:
        os.makedirs(download_path, exist_ok=True)  # Ensure the path exists
        
        ydl_opts = {
            'format': f'bestvideo[height<={resolution}]' if platform == "YouTube" else 'mp4',
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', 'Instagram_Reel')
            extension = info_dict.get('ext', 'mp4')
            
            clean_title = clean_filename(title)  # Sanitize the title
            file_path = os.path.join(download_path, f"{clean_title}.{extension}")
            
            # Rename the file if the sanitized name doesn't match the yt_dlp output
            original_path = ydl.prepare_filename(info_dict)
            if original_path != file_path:
                os.rename(original_path, file_path)
            
            return file_path
    except Exception as e:
        st.error(f"Wystąpił błąd: {str(e)}")
        return None

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
