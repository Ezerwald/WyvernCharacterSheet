from abstract_character import AbstractCharacter


class HitDicesPool:
    def __init__(self, character: AbstractCharacter):
        self.__character = character
        self.__hit_dice = self.__character.current_game_class.value.hit_dice
        self.__max_hit_dices_amount = self.calc_max_hit_dices_amount()
        self.__hit_dices_amount = self.__max_hit_dices_amount

    @property
    def hit_dices_amount(self):
        """Get hit dices amount in pool"""
        return self.__hit_dices_amount

    @hit_dices_amount.setter
    def hit_dices_amount(self, amount):
        """Set hit dices amount in pool"""
        if amount < 0:
            return
        elif amount < self.__max_hit_dices_amount:
            self.__hit_dices_amount = amount
        else:
            self.__hit_dices_amount = self.__max_hit_dices_amount

    @property
    def hit_dice(self):
        """Get the number of sides of hit dice"""
        return self.__hit_dice

    @property
    def max_hit_dices_amount(self):
        """Get max hit dices amount"""
        return self.__max_hit_dices_amount

    def calc_max_hit_dices_amount(self):
        """Calculate max hit dices amount depending on character level"""
        value = self.__character.level.value
        return value
