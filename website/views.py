from flask import Blueprint, render_template, request, jsonify
from character_singleton import CharacterSingleton
from show_character_info import show_character_info
from constants import LIST_OF_ELEMENTS_TO_UPDATE

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
        # Extract data from JSON request
        data = request.json

        # Set attribute in character singleton
        character_singleton.set_attribute(data['type'], data['value'])

        # Show updated character info
        show_character_info()
        print("Saved data:", data)

        # Prepare data to send back as JSON response
        dict_of_elements_to_update = {element: character_singleton.get_attribute(element)
                                      for element in LIST_OF_ELEMENTS_TO_UPDATE}

        # Return JSON response
        return jsonify(dict_of_elements_to_update), 200

    except Exception as e:
        # Handle exceptions
        print("Error:", e)
        raise e
