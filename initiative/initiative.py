from abstract_character import AbstractCharacter
from character_stats import AbilityType


class Initiative:
    def __init__(self, character: AbstractCharacter):
        self.__character = character

    @property
    def value(self) -> int:
        value = self.__character.__abilities[AbilityType.DEXTERITY].modifier
        return value
