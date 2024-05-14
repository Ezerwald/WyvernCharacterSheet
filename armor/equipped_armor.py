from .armors import Armor
from abstract_character import AbstractCharacter


class EquippedArmor:
    def __init__(self, character: AbstractCharacter, equipped_armor: Armor):
        """Initialize the EquippedArmor instance."""
        self.__character = character
        self.__equipped_armor = equipped_armor

    @property
    def armor(self) -> Armor:
        """Get the equipped armor."""
        return self.__equipped_armor

    @armor.setter
    def armor(self, value: Armor) -> None:
        """Set the equipped armor."""
        self.__equipped_armor = value
