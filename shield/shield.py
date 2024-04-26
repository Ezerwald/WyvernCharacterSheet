from constants.constants import DEFAULT_SHIELD_BONUS_TO_AC


class Shield:
    def __init__(self, character, equipped: bool = False, bonus_to_ac: int = DEFAULT_SHIELD_BONUS_TO_AC):
        self.__character = character
        self.__equipped = equipped
        self.__bonus_to_ac = bonus_to_ac

    @property
    def equipped(self):
        return self.__equipped

    @equipped.setter
    def equipped(self, new_value):
        self.__equipped = new_value

    @property
    def bonus_to_ac(self):
        return self.__bonus_to_ac

    @bonus_to_ac.setter
    def bonus_to_ac(self, new_value):
        self._bonus_to_ac = new_value
