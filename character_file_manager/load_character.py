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

# Deserialize complex data structures
if character_data:
    character_name = character_data[1]
    current_game_class = character_data[2]
    level = character_data[3]
    background = character_data[4]
    player_name = character_data[5]
    race = character_data[6]
    alignment = character_data[7]
    experience_points = character_data[8]
    ability_scores = deserialize(character_data[9])
    saving_throws_proficiencies = deserialize(character_data[10])
    skills_proficiencies = deserialize(character_data[11])
    shield = character_data[12]
    equipped_armor = character_data[13]
    current_hit_points = character_data[14]
    max_hit_points = character_data[15]
    temporary_hit_points = character_data[16]
    hit_dice = character_data[17]
    hit_dices_left = character_data[18]
    successful_death_saves = character_data[19]
    failed_death_saves = character_data[20]
    attacks = deserialize(character_data[21])
    inventory = character_data[22]
    features = character_data[23]

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
    print("Hit Dice:", hit_dice)
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
