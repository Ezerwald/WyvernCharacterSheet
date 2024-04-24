class SavingThrow:
    def __init__(self, character, ability_type: int, proficiency=False):
        self.__ability_type = ability_type
        self.__proficiency = proficiency
        self.__character = character

    @property
    def value(self):
        value = self.__character.abilities[self.__ability_type].modifier
        if self.__proficiency:
            value += self.__character.prof_bonus.value
        return value

    def set_proficiency(self, proficiency: bool):
        self.__proficiency = proficiency
