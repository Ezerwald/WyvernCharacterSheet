import os
from pathlib import Path


def get_default_downloads_folder():
    """Get the default downloads folder for the current user."""
    downloads_folder = Path(os.path.expanduser("~")) / "Downloads"
    if not downloads_folder.exists():
        raise FileNotFoundError("Downloads folder does not exist.")
    if not downloads_folder.is_dir():
        raise NotADirectoryError("Downloads is not a directory.")
    return downloads_folder
