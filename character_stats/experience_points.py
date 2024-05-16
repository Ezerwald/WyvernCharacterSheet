from abstract_character import AbstractCharacter

class ExperiencePoints:
    def __init__(self, character: AbstractCharacter, experience_points: int = 0):
        self.__character = character
        self.__experience_points = experience_points


    @property
    def value(self):
        """Get current experience points."""
        return self.__experience_points

    @value.setter
    def value(self, experience_points: int):
        experience_points = int(experience_points)
        if experience_points >= 0:
            self.__experience_points = experience_points
        else:
            raise ValueError("Experience points cannot be negative.")

