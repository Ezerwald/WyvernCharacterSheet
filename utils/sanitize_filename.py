# Function to sanitize the character name for a file name
import re
from constants import DEFAULT_FILE_NAME


def sanitize_filename(filename: str) -> str:
    # Remove any characters that are not alphanumeric, spaces, dots, underscores, or hyphens
    sanitized = re.sub(r'[^\w\s\.-]', '', filename)
    # Replace spaces with underscores
    sanitized = sanitized.replace(' ', '_')
    # Ensure the name is not empty or consists solely of invalid characters
    return sanitized or DEFAULT_FILE_NAME
