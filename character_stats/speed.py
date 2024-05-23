from abstract_character import AbstractCharacter


class Speed:
    def __init__(self, character: AbstractCharacter):
        self.__character = character
        self.__speed = character.race.value.speed

    @property
    def value(self):
        """Get movement speed value"""
        return self.__speed

    @value.setter
    def value(self, speed):
        """Set movement speed value"""
        self.__speed = speed
