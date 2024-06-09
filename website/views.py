import shutil
import uuid
from pathlib import Path
from flask import Blueprint, render_template, request, jsonify, send_file, redirect, url_for, session
from werkzeug.utils import secure_filename
import os
from utils.get_elements_update_data import get_elements_update_data
from character_singleton import CharacterSingleton

# Initialize character singleton and load character data
character_singleton = CharacterSingleton()
character_singleton.load_character(Path('saved_characters/default_character.json'))

# Create a Blueprint for views
views = Blueprint('views', __name__)

# Create the users_data directory if it doesn't exist
USERS_DATA_DIR = 'users_data'
os.makedirs(USERS_DATA_DIR, exist_ok=True)


# Initializing session data
@views.before_request
def initialize_session():
    session.permanent = False  # This ensures the session is only valid until the tab is closed
    ensure_user_id()  # Generate a unique user_id
    ensure_user_dir()  # Create temporary user dir


def ensure_user_id():
    """Generate unique user id."""
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())


def ensure_user_dir():
    """ Create temporary user directory"""
    if 'user_dir' not in session:
        user_dir = os.path.join(USERS_DATA_DIR, str(uuid.uuid4()))
        os.makedirs(user_dir)
        session['user_dir'] = user_dir


# Managing session data
@views.route('/upload-character', methods=['GET', 'POST'])
def upload_character():
    if request.method == 'POST':
        # Ensure file is uploaded
        file = request.files.get('file')
        if not file:
            return 'No file part', 400
        if file.filename == '':
            return 'No selected file', 400

        # Ensure user dir exists
        user_dir = session['user_dir']
        os.makedirs(user_dir, exist_ok=True)

        # Saving uploaded file to user dir
        file_path = os.path.join(user_dir, secure_filename(file.filename))
        file.save(file_path)
        session['file_path'] = file_path
        return redirect(url_for('index'))
    return '''
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    '''


@views.route('/download-character', methods=['GET'])
def download_character():
    """Download character data to user's local storage."""
    # Log the client's IP address
    client_ip = request.remote_addr
    print(f"Client IP: {client_ip}")

    if 'file_path' in session:
        # Ensure the file exists before attempting to send it
        file_path = session['file_path']
        if os.path.exists(file_path):
            # Send the file to the client with a custom download name
            return send_file(file_path, as_attachment=True, download_name="character.json")
        else:
            return 'File not found', 404

    return 'No file to download', 400


@views.route('/end-session', methods=['POST'])
def end_session():
    """Ends the current session and deletes temporary files."""
    if 'user_dir' in session:
        user_dir = session.pop('user_dir')
        file_path = session.pop('file_path', None)
        if file_path and os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(user_dir):
            shutil.rmtree(user_dir)
    session.clear()
    return 'Session ended and files deleted', 200


# Home page
@views.route('/')
def index():
    """Render the home page."""
    session['visits'] = session.get('visits', 0) + 1
    print(f"Total visits: {session['visits']}")

    return render_template("index.html")


@views.route('/character-sheet')
def character_sheet():
    """Render the character sheet page."""
    return render_template("character_sheet.html")


@views.route('/save-input', methods=['POST'])
def save_input():
    """Save input data from the character sheet."""
    try:
        data = request.json
        character_singleton.set_attribute(data['type'], data['value'])

        # Log and respond with updated data
        print("Saved data:", data)
        return jsonify(get_elements_update_data()), 200

    except Exception as e:
        # Handle exceptions and respond with an error
        print("Error saving input:", e)
        raise e


@views.route('/get-character-data')
def get_character_data():
    """Retrieve character data for the character sheet."""
    try:
        # Log and respond with character data
        return jsonify(get_elements_update_data()), 200

    except Exception as e:
        # Log the exception and respond with an error message
        print("Error retrieving character data:", e)
        raise e
