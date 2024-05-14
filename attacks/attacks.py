from abstract_character import AbstractCharacter
from character_stats import AbilityType


class Attack:
    def __init__(self, character: AbstractCharacter, name: str, main_ability: AbilityType,
                 proficiency: bool = False, basic_damage: str = "", extra_attack_bonus: int = 0, extra_damage_bonus: int = 0):
        self.__character: AbstractCharacter = character
        self.__name: str = name
        self.__main_ability: AbilityType = main_ability
        self.__proficiency: bool = proficiency
        self.__basic_damage: str = basic_damage
        self.__attack_bonus: int = 0
        self.__extra_attack_bonus: int = extra_attack_bonus
        self.__extra_damage_bonus: int = extra_damage_bonus

    @property
    def name(self) -> str:
        """Get name of the attack."""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """Set the name of the attack."""
        self.__name = name

    @property
    def main_ability(self) -> AbilityType:
        """Get the main ability associated with the attack."""
        return self.__main_ability

    @main_ability.setter
    def main_ability(self, main_ability: AbilityType) -> None:
        """Set the main ability associated with the attack."""
        self.__main_ability = main_ability

    @property
    def attack_bonus(self) -> int:
        """Calculate and get the attack bonus value."""
        value = self.__character.abilities[self.__main_ability].modifier
        if self.__proficiency:
            value += self.__character.prof_bonus.value + self.__extra_damage_bonus
        return value

    @property
    def extra_attack_bonus(self):
        """Get extra attack bonus"""
        return self.__extra_attack_bonus

    @extra_attack_bonus.setter
    def extra_attack_bonus(self, value) -> None:
        """Set the extra attack bonus."""
        self.__extra_attack_bonus = value

    @property
    def basic_damage(self) -> str:
        """Get the basic damage formula."""
        return self.__basic_damage

    @basic_damage.setter
    def basic_damage(self, value: str) -> None:
        """Set the basic damage formula."""
        # Add validation if necessary
        self.__basic_damage = value

    @property
    def extra_damage_bonus(self) -> int:
        """Get the extra damage bonus."""
        return self.__extra_damage_bonus

    @extra_damage_bonus.setter
    def extra_damage_bonus(self, value: int) -> None:
        """Set the extra damage bonus."""
        self.__extra_damage_bonus = value

    @property
    def damage_formula(self) -> str:
        """Get the full damage calculation formula."""
        return f"{self.__basic_damage} + {self.__character.abilities[self.__main_ability].modifier + self.__extra_damage_bonus}"

