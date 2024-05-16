from constants.constants import MIN_ABILITY_VALUE, MAX_ABILITY_VALUE
from .abilities_types import AbilityType
from abstract_character import AbstractCharacter


class Ability:
    def __init__(self, character: AbstractCharacter, ability_type: AbilityType, score: int):
        self.__character = character
        self.__ability_type = ability_type
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score: int):
        if MIN_ABILITY_VALUE <= new_score <= MAX_ABILITY_VALUE:
            self.__score = new_score
        else:
            raise ValueError("Invalid Ability Value")

    @property
    def modifier(self):
        modifier = (self.__score - 10) // 2
        return modifier
