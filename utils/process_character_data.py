from typing import List, Tuple

from abstract_character import AbstractCharacter
from attacks import Attack
from character_stats import AbilityType


def process_attacks_data(character: AbstractCharacter, attacks_data_list: List[Tuple[str, str, bool, str, int, int]]):
    """Process the attacks data list to prepare it for character attacks_list attribute creation."""
    processed_attacks = []
    for attack_data in attacks_data_list:
        print(attack_data)
        name, ability_type_str, proficiency, damage_type, basic_damage, extra_damage_bonus = attack_data
        # Getting ability type
        try:
            ability_type = AbilityType(ability_type_str)
        except ValueError:
            print(f"Invalid ability type: {ability_type_str}. Skipping attack.")
            continue

        # Create Attack object
        attack = Attack(character, name, ability_type, proficiency, damage_type, basic_damage, extra_damage_bonus)
        processed_attacks.append(attack)
    # Returning list of attacks
    return processed_attacks
