import streamlit as st
from video_downloader import download_video
from utils import get_translations
import os

# If the language is not set, default to Polish
if "language" not in st.session_state:
    st.session_state.language = "pl"  # Domyślny język: polski

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

# Tabs for YouTube and Instagram
tab1, tab2 = st.tabs([t["youtube_tab"], t["instagram_tab"]])

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

st.markdown(t["app_footer"])
