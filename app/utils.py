import re

# Clean the filename by replacing invalid characters with underscores
def clean_filename(filename):
    """Sanitize a filename by replacing invalid characters with underscores."""
    return re.sub(r'[<>:"/\\|?*]', '_', filename)


# Translate the app to different languages
def get_translations(language):
    translations = {
        "pl": {
            "title": "Pobierz Wideo",
            "description": "Wprowadź URL, aby pobrać filmy z YouTube lub Reels z Instagrama!",
            "youtube_tab": "YouTube",
            "instagram_tab": "Instagram",
            "youtube_header": "Pobieranie wideo z YouTube",
            "instagram_header": "Pobieranie rolki z Instagrama", 
            "url_prompt": "Wprowadź link URL:",
            "resolution_prompt": "Wybierz rozdzielczość:",
            "download_youtube_button": "Pobierz YouTube Video",
            "download_instagram_button": "Pobierz Instagram Reel",
            "error_url": "Proszę wprowadzić prawidłowy URL.",
            "download_in_progress": "Rozpoczynam pobieranie...",
            "download_success": "Pobierz film",
            "app_footer": "Aplikacja stworzona przy użyciu Python, yt-dlp i Streamlit. 🚀",
            "choose language": "Wybierz język",
        },
        "en": {
            "title": "Video Downloader",
            "description": "Enter a URL to download videos from YouTube or Instagram Reels!",
            "youtube_tab": "YouTube",
            "instagram_tab": "Instagram",
            "youtube_header": "YouTube Video Downloader",
            "instagram_header": "Instagram Reel Downloader",  
            "url_prompt": "Enter the video URL:",
            "resolution_prompt": "Choose a resolution:",
            "download_youtube_button": "Download YouTube Video",
            "download_instagram_button": "Download Instagram Reel",
            "error_url": "Please enter a valid URL.",
            "download_in_progress": "Downloading in progress...",
            "download_success": "Download Video",
            "app_footer": "App created using Python, yt-dlp, and Streamlit. 🚀",
            "choose language": "choose language",
        },
    }
    return translations[language]
