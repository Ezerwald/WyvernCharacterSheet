class Level:
    def __init__(self, character, level):
        self.__character = character
        self.__level = level

    @property
    def value(self):
        return self.__level

    @value.setter
    def value(self, new_level: int):
        if MIN_LEVEL <= new_level <= MAX_LEVEL:
            self.__level = new_level
            self.__character.prof_bonus.value = self.__character.prof_bonus.calc_prof_bonus(self.__level)
        else:
            raise ValueError("Invalid Level")
