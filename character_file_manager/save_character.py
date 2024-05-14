import json
import sqlite3

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect('my_character_database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store character data
cursor.execute('''CREATE TABLE IF NOT EXISTS characters (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    current_game_class TEXT,
                    level INTEGER,
                    background TEXT,
                    player_name TEXT,
                    race TEXT,
                    alignment TEXT,
                    experience_points INTEGER,
                    ability_scores TEXT,  -- Stored as a serialized string
                    saving_throws_proficiencies TEXT,  -- Stored as a serialized string
                    skills_proficiencies TEXT,  -- Stored as a serialized string
                    shield TEXT, 
                    equipped_armor TEXT,
                    current_hit_points INTEGER,
                    max_hit_points INTEGER,
                    temporary_hit_points INTEGER,
                    hit_dice TEXT,
                    hit_dices_left INTEGER,
                    successful_death_saves INTEGER,
                    failed_death_saves INTEGER,
                    attacks TEXT,  -- Stored as a serialized string
                    inventory TEXT,
                    features TEXT
                )''')

# Sample character data
character_data = {
    'name': 'Character Name',
    'current_game_class': 'Fighter',
    'level': 5,
    'background': 'Noble',
    'player_name': 'Player Name',
    'race': 'Human',
    'alignment': 'Neutral Good',
    'experience_points': 1000,
    'ability_scores': [16, 14, 12, 10, 10, 8],
    'saving_throws_proficiencies': ['Strength', 'Dexterity'],
    'skills_proficiencies': ['Athletics', 'Perception'],
    'shield': 'True',
    'equipped_armor': 'Chain Mail',
    'current_hit_points': 50,
    'max_hit_points': 60,
    'temporary_hit_points': 0,
    'hit_dices_left': 5,
    'successful_death_saves': 0,
    'failed_death_saves': 0,
    'attacks': [
        {'attack_name': 'Longsword', 'main_ability': 'Strength', 'proficiency': True, 'basic_damage': '1d8 + 3'}
    ],
    'inventory': 'Longsword, Shield, Backpack, Rations',
    'features': 'Action Surge, Second Wind'
}

# Insert character data into the database
cursor.execute('''INSERT INTO characters (
                    name, current_game_class, level, background, player_name, race, alignment,
                    experience_points, ability_scores, saving_throws_proficiencies, skills_proficiencies, shield,
                    equipped_armor, current_hit_points, max_hit_points, temporary_hit_points,
                    hit_dices_left, successful_death_saves, failed_death_saves,
                    attacks, inventory, features
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
               (
                   character_data['name'], character_data['current_game_class'], character_data['level'],
                   character_data['background'], character_data['player_name'], character_data['race'], character_data['alignment'],
                   character_data['experience_points'], json.dumps(character_data['ability_scores']),
                   json.dumps(character_data['saving_throws_proficiencies']),
                   json.dumps(character_data['skills_proficiencies']), character_data['shield'],
                   character_data['equipped_armor'],
                   character_data['current_hit_points'], character_data['max_hit_points'], character_data['temporary_hit_points'],
                   character_data['hit_dices_left'],
                   character_data['successful_death_saves'], character_data['failed_death_saves'],
                   json.dumps(character_data['attacks']), character_data['inventory'], character_data['features']
               ))

# Commit changes and close connection
conn.commit()
conn.close()
