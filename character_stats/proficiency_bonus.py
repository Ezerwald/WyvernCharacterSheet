from constants.constants import PROFICIENCY_BONUS
from abstract_character import AbstractCharacter


class ProfBonus:
    def __init__(self, character: AbstractCharacter):
        self.__character = character

    @property
    def value(self):
        """Gets proficiency bonus value"""
        return PROFICIENCY_BONUS[self.__character.level.value]
