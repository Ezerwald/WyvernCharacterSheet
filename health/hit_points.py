from abstract_character import AbstractCharacter
from character_stats import AbilityType


class HitPoints:
    def __init__(self, character: AbstractCharacter, current_hit_points: int = None, max_hit_points: int = None):
        self.__character = character
        self.__max_hit_points: int = max_hit_points or self.calc_max_hit_points()
        self.__current_hit_points: int = current_hit_points or self.__max_hit_points

    @property
    def current_hit_points(self):
        """Get current hit points."""
        return self.__current_hit_points

    @current_hit_points.setter
    def current_hit_points(self, value: int):
        value = int(value)
        """Set current hit points."""
        if value is None:
            raise ValueError("Current hit points cannot be None.")
        if value < 0:
            raise ValueError("Current hit points cannot be negative.")
        self.__current_hit_points = min(value, self.__max_hit_points)

    @property
    def max_hit_points(self):
        """Get max hit points."""
        if self.__max_hit_points == 0:
            return self.calc_max_hit_points()
        return self.__max_hit_points

    @max_hit_points.setter
    def max_hit_points(self, value: int):
        value = int(value)
        """Set max hit points."""
        if value is None:
            raise ValueError("Max hit points cannot be None.")
        elif value < 0:
            raise ValueError("Max hit points cannot be negative.")
        else:
            self.__max_hit_points = value

    def calc_max_hit_points(self):
        """Calculate max hit points depending on current level and class."""
        hit_dice = self.__character.current_game_class.value.hit_dice_type
        level = self.__character.level.value
        hit_points = (hit_dice + (level - 1) * (hit_dice // 2 + hit_dice % 2) +
                      level * self.__character.abilities[AbilityType.CONSTITUTION].modifier)
        return hit_points