import yt_dlp
import os
from utils import clean_filename

# Download the video based on the URL and resolution
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
        return str(e)
