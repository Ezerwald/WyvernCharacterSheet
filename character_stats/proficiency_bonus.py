from constants import PROFICIENCY_BONUS


class ProfBonus:
    def __init__(self, character):
        self.__character = character

    @property
    def value(self):
        value = self.calc_prof_bonus(self.__character.level.value)
        return value

    def calc_prof_bonus(self, current_level: int):
        return PROFICIENCY_BONUS[current_level]
