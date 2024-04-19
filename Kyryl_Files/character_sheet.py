from typing import List, Dict
from enum import Enum
from json import dumps
from abilities_types import AbilityType

from variables import stat_block


class Character:
    def __init__(self, strength=10, dexterity=10, constitution=10, intelligence=10, wisdom=10, charisma=10):
        self.stats = {
            'strength': AbilityScore(strength),
            'dexterity': AbilityScore(dexterity),
            'constitution': AbilityScore(constitution),
            'intelligence': AbilityScore(intelligence),
            'wisdom': AbilityScore(wisdom),
            'charisma': AbilityScore(charisma)
        }
        self.saving_throws = {stat: SavingThrow(self.stats[stat]) for stat in self.stats}
        self.skills = {skill: Skill() for skill in SKILLS}
        # Other AbilityScores and methods...


class AbilityScore:
    def __init__(self, value):
        self._value = value
        self._modifier = self._calculate_modifier()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if 1 <= new_value <= 20:
            self._value = new_value
            self._modifier = self._calculate_modifier()

    @property
    def modifier(self):
        return self._modifier

    def _calculate_modifier(self):
        return (self._value - 10) // 2


class SavingThrow:
    def __init__(self, AbilityScore):
        self.AbilityScore = AbilityScore
        self.proficient = False

    @property
    def value(self):
        modifier = self.AbilityScore.modifier
        if self.proficient:
            modifier += PROFICIENCY_BONUS
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
