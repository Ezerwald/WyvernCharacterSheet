from abstract_character import AbstractCharacter
from .game_classes import GameClass


class CurrentGameClass:
    def __init__(self, character: AbstractCharacter, game_class: GameClass):
        self.character = character
        self.__game_class = game_class

    @property
    def value(self) -> GameClass:
        """Get the current character game class"""
        return self.__game_class

    @value.setter
    def value(self, new_value):
        """Set the current character game class"""
        self.__game_class = new_value
