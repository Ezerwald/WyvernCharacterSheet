from pathlib import Path

from flask import Blueprint, render_template, request, jsonify, send_file, redirect, url_for
import os

from utils import allowed_file
from utils.get_elements_update_data import get_elements_update_data
from character_singleton import CharacterSingleton

# Create a Blueprint for views
views = Blueprint('views', __name__)
character_singleton = CharacterSingleton()

STORAGE_FOLDER = Path("saved_characters/character_saved_data.json")


@views.route('/upload-character', methods=['GET', 'POST'])
def upload_character():
    """
    Handle character upload.

    Returns:
        GET: Rendered template for character upload.
        POST: Redirects to index if successful, otherwise returns error messages.
    """

    if request.method == 'POST':
        # Ensure file is uploaded
        file = request.files.get('file')
        if not file:
            return 'No file part', 400
        if file.filename == '':
            return 'No selected file', 400
        if not allowed_file(file.filename, {'json'}):
            return 'Invalid file type', 400

        # Saving uploaded file to user dir
        file.save(STORAGE_FOLDER)

        print("character was uploaded")
        return redirect(url_for('views.character_sheet'))
    return render_template('upload_character.html')


@views.route('/download-character', methods=['GET'])
def download_character():
    """Download character data to user's local storage."""
    # Log the client's IP address
    client_ip = request.remote_addr
    print(f"Client IP: {client_ip}")

    file_path = STORAGE_FOLDER
    print(f"File path: {file_path}")
    if os.path.exists(file_path):
        # Send the file to the client with a custom download name
        return send_file(file_path, as_attachment=True, download_name="character.json")
    return 'No file to download', 400


# Home page
@views.route('/')
def index():
    """Render the home page."""
    return render_template("index.html")


@views.route('/character-sheet')
def character_sheet():
    """Render the character sheet page."""
    return render_template("character_sheet.html")


@views.route('/save-input', methods=['POST'])
def save_input():
    """Save input data from the character sheet."""
    try:
        data = request.json  # Get JSON data from request
        character_singleton.set_attribute(data['type'], data['value'])  # Set character attribute based on received data

        # Log and respond with updated data in JSON format
        print("Saved data:", data)

        # Create a dictionary with two JSON objects
        response_data = {
            "elementsToUpdate": get_elements_update_data(),
            "packedCharacterData": character_singleton.pack_character_data()
        }

        return jsonify(response_data), 200

    except Exception as e:
        print("Error saving input:", e)
        raise e


@views.route('/get-character-data')
def get_character_data():
    """Retrieve character data for the character sheet."""
    try:
        # Log and respond with character data in JSON format
        return jsonify(get_elements_update_data()), 200

    except Exception as e:
        print("Error retrieving character data:", e)
        raise e
