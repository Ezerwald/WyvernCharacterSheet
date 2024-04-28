from abstract_character import AbstractCharacter
from character_stats import AbilityType


class Initiative:
    def __init__(self, character: AbstractCharacter):
        self.__character = character

    @property
    def value(self) -> int:
        """Get initiative value"""
        value = self.__character.abilities[AbilityType.DEXTERITY].modifier
        return value
