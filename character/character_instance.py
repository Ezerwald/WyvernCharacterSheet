
from typing import List, Dict, Tuple
from armor import Armor
from character_stats import AbilityType
from game_classes import GameClassType
from .character import Character

# Define the type for character_creation_data
character_creation_data: Dict[Dict[AbilityType, int], GameClassType, str, int, Armor]

# Initialize the Character object
current_character = Character()
