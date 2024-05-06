from typing import List

from character_stats import AbilityType
from .attacks import Attack
from abstract_character import AbstractCharacter


class AttacksList:
    def __init__(self, character: AbstractCharacter):
        self.__character = character
        self.__attacks: List[Attack] = []

    def add_attack(self, name: str, main_ability: AbilityType, proficiency: bool = False, basic_damage: str = "") -> None:
        """Add an attack to the list."""
        attack = Attack(self.__character, name, main_ability, proficiency, basic_damage)
        self.__attacks.append(attack)

    def remove_attack(self, attack_name: str) -> None:
        """Remove an attack from the list by character_name."""
        for index, attack in enumerate(self.__attacks):
            if attack.name == attack_name:
                del self.__attacks[index]
                return
        raise ValueError(f"No attack with character_name '{attack_name}' found.")

    def get_attack(self, attack_name: str) -> Attack:
        """Get an attack from the list by character_name."""
        for attack in self.__attacks:
            if attack.name == attack_name:
                return attack
        raise ValueError(f"No attack with character_name '{attack_name}' found.")

    def get_all_attacks(self) -> List[Attack]:
        """Get a copy of all attacks in the list."""
        return self.__attacks.copy()

    def clear_attacks(self) -> None:
        """Clear all attacks from the list."""
        self.__attacks.clear()

    def attack_exists(self, attack_name: str) -> bool:
        """Check if an attack with the given character_name exists in the list."""
        return any(attack.name == attack_name for attack in self.__attacks)
