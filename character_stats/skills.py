class Skill:
    def __init__(self, character, skill_type: int, proficiency=False):
        self.__skill_type = skill_type
        self.__character = character
        self.__proficiency = proficiency

    @property
    def value(self):
        value = self.__character.abilities[self.__skill_type].modifier
        if self.__proficiency:
            value += self.__character.prof_bonus.value
        return value