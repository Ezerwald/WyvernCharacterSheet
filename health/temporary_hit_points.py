from abstract_character import AbstractCharacter


class TemporaryHitPoints:
    def __init__(self, character: AbstractCharacter, temporary_hit_points: int = 0):
        self.__character = character
        self.__temporary_hit_points = temporary_hit_points

    @property
    def value(self):
        """Set number of temporary hit points."""
        return self.__temporary_hit_points

    @value.setter
    def value(self, value):
        """Get number of temporary hit points."""
        self.__temporary_hit_points = value
