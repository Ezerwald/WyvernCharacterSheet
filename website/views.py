import io
import json

from flask import Blueprint, render_template, request, jsonify, send_file
from constants import DEFAULT_CHARACTER_PATH, DEFAULT_FILE_NAME
from utils import sanitize_filename
from utils.get_elements_update_data import get_elements_update_data
from character_singleton import CharacterSingleton

character_singleton = CharacterSingleton()

# Create a Blueprint for views
views = Blueprint('views', __name__)


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
        return generate_response_data()

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
        print("Error retrieving character data")
        raise e


@views.route('/load-character-from-storage', methods=['POST'])
def load_character_from_storage():
    """Load character data from browser's local storage."""
    data = request.json.get('characterData')
    try:
        if data is None:
            raise ValueError("No character data in storage, loading default character data.")

        # Debugging: Print the type and content of the data
        print("Data type:", type(data))
        print("Data content:", data)

        character_singleton.load_character_from_json(data)
    except Exception as e:
        print(f"Error loading character from storage: {e}. Loading default character.")
        load_default_character()
    finally:
        return generate_response_data()


def load_default_character():
    """Load default character data from a predefined path."""
    try:
        character_singleton.load_character_from_path(DEFAULT_CHARACTER_PATH)
        print("Loaded default character")
    except Exception as e:
        print("Failed to load default character", e)
        raise e


def generate_response_data():
    """Generate response data after loading character"""
    response_data = {
        "elementsToUpdate": get_elements_update_data(),
        "packedCharacterData": character_singleton.pack_character_data()
    }
    return jsonify(response_data), 200


@views.route('/download-character')
def download_character():
    character_data = character_singleton.pack_character_data()
    character_json = json.dumps(character_data, indent=4)

    # Create a BytesIO stream and write the JSON data to it
    byte_io = io.BytesIO()
    byte_io.write(character_json.encode('utf-8'))
    byte_io.seek(0)

    # Generating download name
    character_name = character_singleton.character.biography.name or 'MyCharacter'
    sanitized_name = sanitize_filename(character_name)
    download_name = f"{sanitized_name}.json"

    # Send the file to the client
    return send_file(byte_io, mimetype='application/json', as_attachment=True, download_name=download_name)


@views.route('/upload-character')
def upload_character():
    return render_template("/upload_character.html")
