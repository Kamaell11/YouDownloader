import re

def clean_filename(filename):
    """Sanitize a filename by replacing invalid characters with underscores."""
    return re.sub(r'[<>:"/\\|?*]', '_', filename)
