from abstract_character import AbstractCharacter
from character_stats import AbilityType


class HitPoints:
    def __init__(self, character: AbstractCharacter, current_hit_points: int = None, custom_max_hit_points: int = None):
        self.__character = character
        self.__custom_max_hit_points: int = custom_max_hit_points
        self.__current_hit_points: int = current_hit_points

    @property
    def current_hit_points(self):
        """Get current hit points."""
        return self.__current_hit_points

    @current_hit_points.setter
    def current_hit_points(self, value: int):
        """Set current hit points."""
        value = int(value)
        if value is None:
            raise ValueError("Current hit points cannot be None.")
        if value < 0:
            raise ValueError("Current hit points cannot be negative.")
        self.__current_hit_points = min(value, self.__custom_max_hit_points)

    @property
    def max_hit_points(self):
        """Get max hit points"""
        if self.__custom_max_hit_points == 0:
            return self.calc_max_hit_points()
        return self.__custom_max_hit_points

    @max_hit_points.setter
    def max_hit_points(self, value: int):
        """Set max hit points."""
        value = int(value)
        if value is None:
            raise ValueError("Max hit points cannot be None.")
        elif value < 0:
            raise ValueError("Max hit points cannot be negative.")
        else:
            self.__custom_max_hit_points = value

    @property
    def custom_max_hit_points(self):
        """Get custom max hit points."""
        return self.__custom_max_hit_points

    def calc_max_hit_points(self):
        """Calculate max hit points depending on current level and class."""
        hit_dice = self.__character.current_game_class.value.hit_dice_type
        level = self.__character.level.value
        hit_points = (hit_dice + (level - 1) * (hit_dice // 2 + hit_dice % 2) +
                      level * self.__character.abilities[AbilityType.CONSTITUTION].modifier)
        return hit_points
