from skills_types import SkillType
from abstract_character import AbstractCharacter
from utils import SKILLS_TO_ABILITIES


class Skill:
    def __init__(self, character: AbstractCharacter, skill_type: SkillType, proficiency: bool = False):
        self.__skill_type = skill_type
        self.__character = character
        self.__proficiency = proficiency

    @property
    def value(self):
        value = self.__character.abilities[SKILLS_TO_ABILITIES[self.__skill_type]].modifier
        if self.__proficiency:
            value += self.__character.prof_bonus.value
        return value

    @property
    def proficiency(self):
        return self.__proficiency

    @proficiency.setter
    def proficiency(self, value):
        self.__proficiency = value
