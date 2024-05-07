import json
import sqlite3


# Function to deserialize JSON string to Python object
def deserialize(json_str):
    return json.loads(json_str)


# Connect to SQLite database
conn = sqlite3.connect('my_character_database.db')
cursor = conn.cursor()

# Load character data with ID 1 from the database
cursor.execute("SELECT * FROM characters WHERE id = 1")
character_data = cursor.fetchone()

# Get column names
columns = [description[0] for description in cursor.description]

# Create a dictionary mapping column names to their values
character_dict = dict(zip(columns, character_data))

# Deserialize complex data structures
if character_dict:
    character_name = character_dict['character_name']
    current_game_class = character_dict['current_game_class']
    level = character_dict['level']
    background = character_dict['background']
    player_name = character_dict['player_name']
    race = character_dict['race']
    alignment = character_dict['alignment']
    experience_points = character_dict['experience_points']
    ability_scores = deserialize(character_dict['ability_scores'])
    saving_throws_proficiencies = deserialize(character_dict['saving_throws_proficiencies'])
    skills_proficiencies = deserialize(character_dict['skills_proficiencies'])
    shield = character_dict['shield']
    equipped_armor = character_dict['equipped_armor']
    current_hit_points = character_dict['current_hit_points']
    max_hit_points = character_dict['max_hit_points']
    temporary_hit_points = character_dict['temporary_hit_points']
    hit_dices_left = character_dict['hit_dices_left']
    successful_death_saves = character_dict['successful_death_saves']
    failed_death_saves = character_dict['failed_death_saves']
    attacks = deserialize(character_dict['attacks'])
    inventory = character_dict['inventory']
    features = character_dict['features']

    # Now you can work with the deserialized data
    print("Character Name:", character_name)
    print("Current Game Class:", current_game_class)
    print("Level:", level)
    print("Background:", background)
    print("Player Name:", player_name)
    print("Race:", race)
    print("Alignment:", alignment)
    print("Experience Points:", experience_points)
    print("Ability Scores:", ability_scores)
    print("Saving Throw Proficiencies:", saving_throws_proficiencies)
    print("Skills Proficiencies:", skills_proficiencies)
    print("Shield:", shield)
    print("Equipped Armor:", equipped_armor)
    print("Current Hit Points:", current_hit_points)
    print("Maximum Hit Points:", max_hit_points)
    print("Temporary Hit Points:", temporary_hit_points)
    print("Hit Dices Left:", hit_dices_left)
    print("Successful Death Saves:", successful_death_saves)
    print("Failed Death Saves:", failed_death_saves)
    print("Attacks:", attacks)
    print("Inventory:", inventory)
    print("Features:", features)
else:
    print("Character with ID 1 was not found in the database")

# Close connection
conn.close()
