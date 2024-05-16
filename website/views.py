from flask import Blueprint, render_template, request, jsonify
from character_singleton import CharacterSingleton
from show_character_info import show_character_info
from utils.get_elements_update_data import get_elements_update_data

# Initialize character singleton and load character data
character_singleton = CharacterSingleton()
character_singleton.load_character('saved_characters/character_saved_data.json')
show_character_info()

# Create a Blueprint for views
views = Blueprint('views', __name__)


# Define routes and corresponding functions
@views.route('/')
def home():
    return render_template("index.html")


@views.route('/character_sheet')
def character_sheet():
    return render_template("character_sheet.html")


@views.route('/save_input', methods=['POST'])
def save_input():
    try:
        # saving
        data = request.json
        character_singleton.set_attribute(data['type'], data['value'])

        # logging
        show_character_info()
        print("Saved data:", data)

        # response
        return jsonify(get_elements_update_data()), 200

    except Exception as e:
        # Handle exceptions
        print("Error:", e)
        raise e


@views.route('/get_character_data')
def get_character_data():
    try:
        # logging
        print("Character loaded successfully")
        show_character_info()

        # response
        return jsonify(get_elements_update_data()), 200

    except Exception as e:
        # Handle exceptions
        print("Error:", e)
        raise e
