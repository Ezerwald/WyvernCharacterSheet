from abstract_character import AbstractCharacter


class HitPoints:
    def __init__(self, character: AbstractCharacter):
        self.__character = character
        self.__max_hit_points = self.calc_max_hit_points()
        self.__current_hit_points = self.__max_hit_points

    @property
    def current_hit_points(self):
        """Get current hit points."""
        return self.__current_hit_points

    @current_hit_points.setter
    def current_hit_points(self, value):
        """Set current hit points."""
        if value < 0:
            return
        self.__current_hit_points = min(value, self.__max_hit_points)

    @property
    def max_hit_points(self):
        """Get max hit points."""
        return self.__max_hit_points

    @max_hit_points.setter
    def max_hit_points(self, value):
        """Set max hit points."""
        if value < 0:
            return
        self.__max_hit_points = value
        if value < self.__current_hit_points:
            # If new max hit points are less than current hit points,
            # adjust current hit points to match new max
            self.__current_hit_points = value

    def calc_max_hit_points(self):
        """Calculate max hit points depending on current level and class."""
        hit_dice = self.__character.current_game_class.value.hit_dice
        level = self.__character.level.value
        hit_points = hit_dice + (level - 1) * (hit_dice // 2 + hit_dice % 2)
        return hit_points
