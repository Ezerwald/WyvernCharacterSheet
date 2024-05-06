from abstract_character import AbstractCharacter


class Speed:
    def __init__(self, character: AbstractCharacter):
        self.__character = character
        self.__speed = character.race.speed

    @property
    def speed(self):
        """Get movement speed value"""
        return self.__speed

    @speed.setter
    def speed(self, speed):
        """Set movement speed value"""
        self.__speed = speed
