from typing import List
from game_classes_types import GameClassType
from character_stats import AbilityType
from skills_types import SkillType


class GameClass:
    def __init__(self, game_class_type: GameClassType, name: str, hit_dice: int, saving_throws: List[AbilityType],
                 proficiencies: str, amount_of_skills: int, skills_to_choose: List[SkillType]):
        self.__game_class_type: GameClassType = game_class_type
        self.__name: str = name
        self.__hit_dice: int = hit_dice
        self.__saving_throws: List[AbilityType] = saving_throws
        self.__proficiencies: str = proficiencies
        self.__amount_of_skills: int = amount_of_skills
        self.__skills_to_choose: List[SkillType] = skills_to_choose

    @property
    def type(self) -> GameClassType:
        """Get game class type"""
        return self.__game_class_type

    @property
    def name(self) -> str:
        """Get game class name"""
        return self.__name

    @property
    def hit_dice(self) -> int:
        """Get hit dice of class"""
        return self.__hit_dice

    @property
    def saving_throws(self) -> List[AbilityType]:
        """Get list of saving throws"""
        return self.__saving_throws

    @property
    def proficiencies(self) -> str:
        """Get list of proficiencies"""
        return self.__proficiencies

    @property
    def amount_of_skills(self) -> int:
        """Get amount of skills that can be chosen"""
        return self.__amount_of_skills

    @property
    def skills_to_choose(self) -> List[SkillType]:
        """Get list of skills that can be chosen"""
        return self.__skills_to_choose

    def __str__(self) -> str:
        """String representation of the GameClass instance"""
        return f"Game Class: {self.__name}, Type: {self.__game_class_type}, Hit Dice: {self.__hit_dice}, " \
               f"Saving Throws: {', '.join(str(ability) for ability in self.__saving_throws)}, " \
               f"Proficiencies: {self.__proficiencies}, Amount of Skills: {self.__amount_of_skills}, " \
               f"Skills to Choose: {', '.join(str(skill) for skill in self.__skills_to_choose)}"
