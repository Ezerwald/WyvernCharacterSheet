import string
from typing import Dict

from variables import Ability, SavingThrow, AbilityType
from variables.constants import *


class Character:
    __abilities: Dict[int, Ability]
    __saving_throws: Dict[int, SavingThrow]

    def __init__(self, abilities_scores: Dict[int, int]) -> None:
        self.__level = Level()
        self.__prof_bonus = ProfBonus()
        self.__abilities = {ability.value: Ability(ability.value, abilities_scores[ability.value]) for ability in
                            AbilityType}
        self.__saving_throws = {ability.value: SavingThrow(ability.value) for ability in AbilityType}
        self.__skills = {skill: Skill(skill, self.abilities[SKILLS_TO_ABILITIES[skill].value].modifier)
                         for skill in SKILLS_TO_ABILITIES}

    @property
    def level(self):
        return self.__level

    @property
    def prof_bonus(self):
        return self.__prof_bonus

    @property
    def abilities(self):
        return self.__abilities

    @property
    def saving_throws(self):
        return self.__saving_throws

    @property
    def skills(self):
        return self.__skills


class Level:
    def __init__(self, level=MIN_LEVEL):
        self.__level_value = level

    @property
    def value(self):
        return self.__level_value

    @value.setter
    def value(self, new_level: int):
        if MIN_LEVEL <= new_level <= MAX_LEVEL:
            self.__level_value = new_level
            Character.prof_bonus.value = Character.prof_bonus.calc_prof_bonus(self.__level_value)
        else:
            raise ValueError("Invalid Level")


class ProfBonus:
    def __init__(self):
        self.__prof_bonus_value = self.calc_prof_bonus(Character.level.value)

    @property
    def value(self):
        return self.__prof_bonus_value

    @value.setter
    def value(self, new_proficiency_bonus: int):
        self.__prof_bonus_value = new_proficiency_bonus

    def calc_prof_bonus(self, current_level: int):
        return PROFICIENCY_BONUS[current_level]


class Skill:
    def __init__(self, skill_type: string, skill_value: int, proficiency=False):
        self.__skill_type = skill_type
        self.__skill_value = skill_value
        self.__proficiency = proficiency

    @property
    def value(self):
        value = self.__skill_value
        if self.__proficiency:
            value += Character.prof_bonus
        return value
