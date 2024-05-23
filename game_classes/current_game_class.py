from abstract_character import AbstractCharacter
from .game_classes_collection_instance import basic_game_classes_collection
from .game_classes import GameClass


class CurrentGameClass:
    def __init__(self, character: AbstractCharacter, game_class_name: str):
        self.character = character
        self.__game_class_name = game_class_name

    @property
    def value(self) -> GameClass:
        """Get the current character game class"""
        return self.get_game_class_from_collection()

    @property
    def name(self) -> str:
        """Get the name of the current character game class"""
        return self.__game_class_name

    @name.setter
    def name(self, value: str):
        """Set the current character game class"""
        if value in basic_game_classes_collection.get_all_game_classes():
            self.__game_class_name = value

    def get_game_class_from_collection(self) -> GameClass:
        return basic_game_classes_collection.get_game_class_by_name(self.__game_class_name)
