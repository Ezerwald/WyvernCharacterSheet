from abstract_character import AbstractCharacter


class Speed:
    def __init__(self, character: AbstractCharacter, speed: int) -> None:
        self.__character: AbstractCharacter = character
        self.__speed: int = speed or self.__character.race.value.speed

    @property
    def value(self) -> int:
        """Get movement speed value"""
        return self.__speed

    @value.setter
    def value(self, value):
        """Set movement speed value"""
        value = int(value)
        if value is None:
            raise ValueError("Speed cannot be None.")
        elif value < 0:
            raise ValueError("Speed cannot be negative.")
        elif value == 0:
            self.__speed = self.__character.race.value.speed
        else:
            self.__speed = value
