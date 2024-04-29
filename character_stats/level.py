from constants import MIN_LEVEL, MAX_LEVEL
from abstract_character import AbstractCharacter


class Level:
    def __init__(self, character: AbstractCharacter, level):
        self.__character = character
        self.__level = level

    @property
    def value(self):
        return self.__level

    @value.setter
    def value(self, new_level: int):
        if MIN_LEVEL <= new_level <= MAX_LEVEL:
            self.__level = new_level
            # update prof bonus
            # update hit points
            # update hit dices amount
        else:
            raise ValueError("Invalid Level")
