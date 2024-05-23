from flask import Blueprint, render_template, request, jsonify
from character_singleton import CharacterSingleton
from utils.get_elements_update_data import get_elements_update_data

# Initialize character singleton and load character data
character_singleton = CharacterSingleton()
character_singleton.load_character('saved_characters/character_saved_data.json')

# Create a Blueprint for views
views = Blueprint('views', __name__)


# Define routes and corresponding functions
@views.route('/')
def home():
    """Render the home page."""
    return render_template("index.html")


@views.route('/character_sheet')
def character_sheet():
    """Render the character sheet page."""
    return render_template("character_sheet.html")


@views.route('/save_input', methods=['POST'])
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
        raise e


@views.route('/get_character_data')
def get_character_data():
    """Retrieve character data for the character sheet."""
    try:
        # Log and respond with character data
        return jsonify(get_elements_update_data()), 200

    except Exception as e:
        # Handle exceptions and respond with an error
        raise e
