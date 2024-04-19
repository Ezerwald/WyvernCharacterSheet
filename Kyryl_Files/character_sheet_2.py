from typing import List, Dict
from enum import Enum
from json import dumps
from abilities_types import AbilityType

from variables import stat_block


class Character:
    __abilities_scores: Dict[int, int]
    __saving_throws: Dict[int, int]
    def __init__(self, abilities_scores_list: abilities_scores) -> None:
        self.__level = Level
        self.__proficiency_bonus = ProficiencyBonus()
        self.__abilities_scores = abilities_scores_list
        self.__abilities_blocks = {ability.value: AbilityBlock for ability in AbilityType}
        self.__saving_throws = {ability.value: SavingThrow(self.abilities[ability]) for ability in AbilityType}
        self.__skills = {skill: Skill() for skill in SKILLS}


class Level:
    def __init__(self, character_class, level: int)
        self.__character_class: character_class
        self.__level = level

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, new_level: int):
        self.__level = new_level



class ProficiencyBonus:
    def __init__(self):
        self.__proficiency_bonus = 2

    @property
    def proficiency_bonus(self):
        return self.__proficiency_bonus

    @proficiency_bonus.setter
    def proficiency_bonus(self, new_proficiency_bonus: int):
        self.__proficiency_bonus = new_proficiency_bonus

    def calc_current_level_proficiency_bonus(self, current_level: int):
        return PROFICIENCY_BONUS[current_level]

class AbilityBlock:
    def __init__(self, ability_type: int, score: int) :
        self.__ability_type = ability_type
        self.__score = score
        self.__modifier = self._calculate_modifier()

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score):
        if 1 <= new_score <= 20:
            self.__score = new_score
            self.__modifier = self._calculate_modifier()

    @property
    def modifier(self):
        return self.__modifier

    def _calculate_modifier(self):
        return (self.__score - 10) // 2


class SavingThrow:
    def __init__(self, ability_type: int, proficiency = False):
        self.__ability_type = ability_type
        self.__proficiency = proficiency

    @property
    def value(self):
        value =
        if self.__proficiency:
            modifier +=
        return modifier


class Skill:
    def __init__(self):
        self._value = 0
        self.proficient = False

    @property
    def value(self):
        if self.proficient:
            return self.value + PROFICIENCY_BONUS
        return self.value


PROFICIENCY_BONUS = 2

SKILLS = ['acrobatics', 'animal_handling', 'wisdom', 'arcana', 'athletics', 'deception', 'history', 'insight',
          'intimidation',
          'investigation', 'medicine', 'nature', 'perception', 'performance', 'persuasion', 'religion',
          'sleight_of_hand', 'stealth', 'survival']
PROFICIENCY_BONUS = {1:2, 2:2, 3:2, 4:2, 5:3, 6:3, 7:3, 8:3, 9:4, 10:4, 11:4, 12:4, 13:5, 14:5, 15:5, 16:5, 17:6, 18:6, 19:6, 20:6}
