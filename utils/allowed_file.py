def allowed_character_file(filename, allowed_extensions):
    """Check if the filename has a valid extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions