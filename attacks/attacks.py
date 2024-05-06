from abstract_character import AbstractCharacter
from character_stats import AbilityType


class Attack:
    def __init__(self, character: AbstractCharacter, name: str, main_ability: AbilityType,
                 proficiency: bool = False, basic_damage: str = ""):
        self._character = character
        self._name = name
        self._main_ability = main_ability
        self._proficiency = proficiency
        self._basic_damage = basic_damage
        self._attack_bonus = 0

    @property
    def name(self) -> str:
        """Get character_name of the attack."""
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """Set the character_name of the attack."""
        self._name = name

    @property
    def main_ability(self) -> AbilityType:
        """Get the main ability associated with the attack."""
        return self._main_ability

    @main_ability.setter
    def main_ability(self, main_ability: AbilityType) -> None:
        """Set the main ability associated with the attack."""
        self._main_ability = main_ability

    @property
    def attack_bonus(self) -> int:
        """Calculate and get the attack bonus value."""
        value = self._character.abilities[self._main_ability].modifier
        if self._proficiency:
            value += self._character.prof_bonus.value
        return value

    @property
    def basic_damage(self) -> str:
        """Get the basic damage formula."""
        return self._basic_damage

    @basic_damage.setter
    def basic_damage(self, value: str) -> None:
        """Set the basic damage formula."""
        # Add validation if necessary
        self._basic_damage = value

    @property
    def damage_formula(self) -> str:
        """Get the full damage calculation formula."""
        return f"{self._basic_damage} + {self._character.abilities[self._main_ability].modifier}"
