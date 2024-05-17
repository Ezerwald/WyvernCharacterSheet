from character_stats import AbilityType
from abstract_character import AbstractCharacter


class SavingThrow:
    def __init__(self, character: AbstractCharacter, ability_type: AbilityType, proficiency: bool=False):
        self.__ability_type = ability_type
        self.__proficiency = proficiency
        self.__character = character

    @property
    def value(self) -> int:
        """Gets saving throw value."""
        value = self.__character.abilities[self.__ability_type].modifier
        if self.__proficiency:
            value += self.__character.prof_bonus.value
        return value

    @property
    def proficiency(self) -> bool:
        return self.__proficiency

    @proficiency.setter
    def proficiency(self, proficiency: bool):
        """Sets saving throw proficiency."""
        self.__proficiency = proficiency
