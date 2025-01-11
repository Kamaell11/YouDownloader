import streamlit as st
from video_downloader import download_video
from utils import get_translations
import os

# If the language is not set, default to Polish
if "language" not in st.session_state:
    st.session_state.language = "pl"  # Default language: Polish

# Function to change the language
def change_language(lang):
    st.session_state.language = lang

# Create a selectbox with flags as options
language = st.selectbox(
    "Choose language",  # Use a non-empty label for accessibility
    ["🇵🇱 Polish", "🇬🇧 English"], 
    format_func=lambda x: x,  # This ensures the flag is displayed correctly
    label_visibility="hidden"  # This hides the label visually
)

# Handle language change based on selection
if language == "🇵🇱 Polish":
    change_language("pl")
elif language == "🇬🇧 English":
    change_language("en")

# Translation dictionary
t = get_translations(st.session_state.language)

# Title and description
st.title(t["title"])
st.markdown(t["description"])

# Tabs for YouTube, Instagram, TikTok, and X
tab1, tab2, tab3, tab4 = st.tabs([t["youtube_tab"], t["instagram_tab"], "TikTok", "X (Twitter)"])

# YouTube Tab
with tab1:
    st.header(t["youtube_header"])
    url = st.text_input(t["url_prompt"])
    resolution = st.selectbox(t["resolution_prompt"], ["1080p", "720p", "480p", "360p"])
    download_button = st.button(t["download_youtube_button"], key="youtube_download")

    if download_button:
        if not url:
            st.error(t["error_url"])
        else:
            st.info(t["download_in_progress"])
            download_dir = "downloads/youtube"
            file_path = download_video(url, resolution, download_dir, platform="YouTube")
            if file_path:
                with open(file_path, "rb") as f:
                    st.download_button(
                        label=t["download_success"],
                        data=f,
                        file_name=os.path.basename(file_path),
                        mime="video/mp4",
                    )

# Instagram Tab
with tab2:
    st.header(t["instagram_header"])
    insta_url = st.text_input(t["url_prompt"], key="insta_url_input")
    download_button_insta = st.button(t["download_instagram_button"], key="instagram_download")

    if download_button_insta:
        if not insta_url:
            st.error(t["error_url"])
        else:
            st.info(t["download_in_progress"])
            download_path = "downloads/instagram"
            file_path = download_video(insta_url, resolution=None, download_path=download_path, platform="Instagram")
            if file_path:
                with open(file_path, "rb") as f:
                    st.download_button(
                        label=t["download_success"],
                        data=f,
                        file_name=os.path.basename(file_path),
                        mime="video/mp4",
                    )

# TikTok Tab
with tab3:
    st.header("TikTok")
    tiktok_url = st.text_input("Enter TikTok video URL", key="tiktok_url_input")
    download_button_tiktok = st.button("Download TikTok", key="tiktok_download")

    if download_button_tiktok:
        if not tiktok_url:
            st.error("Please enter a valid URL.")
        else:
            st.info("Downloading video...")
            download_path = "downloads/tiktok"
            file_path = download_video(tiktok_url, resolution=None, download_path=download_path, platform="TikTok")
            if file_path:
                with open(file_path, "rb") as f:
                    st.download_button(
                        label="Download TikTok Video",
                        data=f,
                        file_name=os.path.basename(file_path),
                        mime="video/mp4",
                    )

# X (formerly Twitter) Tab
with tab4:
    st.header("X (Twitter)")
    x_url = st.text_input("Enter X (Twitter) video URL", key="x_url_input")
    download_button_x = st.button("Download X (Twitter)", key="x_download")

    if download_button_x:
        if not x_url:
            st.error("Please enter a valid URL.")
        else:
            st.info("Downloading video...")
            download_path = "downloads/x"
            file_path = download_video(x_url, resolution=None, download_path=download_path, platform="X")
            if file_path:
                with open(file_path, "rb") as f:
                    st.download_button(
                        label="Download X (Twitter) Video",
                        data=f,
                        file_name=os.path.basename(file_path),
                        mime="video/mp4",
                    )

st.markdown(t["app_footer"])
