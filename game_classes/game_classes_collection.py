from typing import List, Optional

from .game_classes import GameClass
from .game_classes_types import GameClassType


class GameClassCollection:
    def __init__(self):
        self.__game_class_collection: List[GameClass] = []

    def add_game_class(self, game_class: GameClass) -> None:
        """Add game class to the collection."""
        if self.get_game_class_by_type(game_class.type) is not None:
            raise ValueError(f"Game class with type '{game_class.type}' already exists in the collection.")
        self.__game_class_collection.append(game_class)

    def get_game_class_by_type(self, game_class_type: GameClassType) -> Optional[GameClass]:
        """Get game class by its type."""
        for game_class in self.__game_class_collection:
            if game_class.type == game_class_type:
                return game_class
        return None

    def get_game_class_by_name(self, name: str) -> Optional[GameClass]:
        """Get game class by its character_name."""
        for game_class in self.__game_class_collection:
            if game_class.name == name:
                return game_class
        return None

    def get_all_game_classes(self) -> List[tuple[str, GameClassType]]:
        """Get names and types of all game classes in the collection."""
        return [(game_class.name, game_class.type) for game_class in self.__game_class_collection]

    def remove_game_class(self, game_class_type: GameClassType) -> None:
        """Remove game class from the collection by its type."""
        for game_class in self.__game_class_collection:
            if game_class.type == game_class_type:
                self.__game_class_collection.remove(game_class)
                return
        raise ValueError(f"No game class with type '{game_class_type}' found.")
