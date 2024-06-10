from enum import Enum


class CharacterAttribute(Enum):
    """Enumeration of character attributes."""
    NAME = 'name'  # Name of the character
    GAME_CLASS_TYPE = 'game_class_type'  # Type of the character's game class
    LEVEL = 'level'  # Level of the character
    BACKGROUND = 'background'  # Background of the character
    RACE = 'race'  # Race of the character
    ALIGNMENT = 'alignment'  # Alignment of the character
    EXPERIENCE_POINTS = 'experience_points'  # Experience points of the character
    ABILITIES_SCORES = 'abilities_scores'  # Ability scores of the character
    SAVING_THROWS_PROFICIENCIES = 'saving_throws_proficiencies'  # Proficient saving throws of the character
    SKILLS_PROFICIENCIES = 'skills_proficiencies'  # Proficient skills of the character
    SHIELD = 'shield'  # Whether the character has a shield equipped
    EQUIPPED_ARMOR = 'equipped_armor_name'  # Armor equipped by the character
    CURRENT_HIT_POINTS = 'current_hit_points'  # Current hit points of the character
    MAX_HIT_POINTS = 'max_hit_points'  # Maximum hit points of the character
    TEMPORARY_HIT_POINTS = 'temporary_hit_points'  # Temporary hit points of the character
    CURRENT_HIT_DICES_AMOUNT = 'current_hit_dices_amount'  # Number of hit dice remaining for the character
    SUCCESSFUL_DEATH_SAVES = 'successful_death_saves'  # Number of successful death saves
    FAILED_DEATH_SAVES = 'failed_death_saves'  # Number of failed death saves
    ATTACKS_LIST = 'attacks_data_list'  # List of attacks available to the character
    INVENTORY = 'inventory'  # Inventory carried by the character
    FEATURES = 'features'  # Features possessed by the character
    NOTES = 'notes'  # Notes of character
