from abstract_character import AbstractCharacter


class HitDicesPool:
    def __init__(self, character: AbstractCharacter, current_hit_dices_amount: int = None):
        self.__character = character
        self.__hit_dice_type = self.__character.current_game_class.value.hit_dice_type
        self.__current_hit_dices_amount = current_hit_dices_amount or self.max_hit_dices_amount

    @property
    def current_hit_dices_amount(self):
        """Get hit dices amount in pool"""
        return self.__current_hit_dices_amount

    @current_hit_dices_amount.setter
    def current_hit_dices_amount(self, amount: int):
        amount = int(amount)
        """Set hit dices amount in pool"""
        if amount < 0:
            raise ValueError("Hit dices amount cannot be negative")
        elif amount <= self.max_hit_dices_amount:
            self.__current_hit_dices_amount = amount
        else:
            self.__current_hit_dices_amount = self.max_hit_dices_amount

    @property
    def hit_dice_type(self) -> str:
        """Get the number of sides of hit dice"""
        return self.__hit_dice_type

    @property
    def max_hit_dices_amount(self) -> int:
        """Get max hit dices amount"""
        return self.__character.level.value

