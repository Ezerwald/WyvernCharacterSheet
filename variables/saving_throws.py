from character import Character


class SavingThrow:
    def __init__(self, ability_type: int, proficiency=False):
        self.__ability_type = ability_type
        self.__proficiency = proficiency

    @property
    def value(self):
        value = Character.abilities[self.__ability_type].modifier
        if self.__proficiency:
            value += Character.prof_bonus
        return value
