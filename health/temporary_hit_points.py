from abstract_character import AbstractCharacter


class TemporaryHitPoints:
    def __init__(self, character: AbstractCharacter):
        self.__character = character
        self.__temporary_hit_points = 0

    @property
    def value(self):
        """Set number of temporary hit points."""
        return self.__temporary_hit_points

    @value.setter
    def value(self, value):
        """Get number of temporary hit points."""
        self.__temporary_hit_points = value
