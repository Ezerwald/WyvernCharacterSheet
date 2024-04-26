from constants.constants import PROFICIENCY_BONUS


class ProfBonus:
    def __init__(self, character):
        self.__character = character

    @property
    def value(self):
        """Gets proficiency bonus value"""
        value = PROFICIENCY_BONUS[self.__character.level.value]
        return value
