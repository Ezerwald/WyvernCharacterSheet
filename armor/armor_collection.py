from typing import List, Optional

from .armors import Armor


class ArmorCollection:
    def __init__(self):
        self.__armor_collection: List[Armor] = []

    def add_armor(self, armor: Armor) -> None:
        """Add armor to the collection."""
        if armor in self.__armor_collection:
            raise ValueError(f"Armor with ID '{armor.name}' already exists in the collection.")
        self.__armor_collection.append(armor)

    def get_armor_by_name(self, name: str) -> Optional[Armor]:
        """Get armor by its Name."""
        for armor in self.__armor_collection:
            if armor.name == name:
                return armor
        raise ValueError(f"Armor with name '{name}' does not exist in the collection.")

    def get_all_armors(self) -> list[str]:
        """Get names of all armor types in the collection."""
        return [armor.name for armor in self.__armor_collection]

    def remove_armor(self, armor_name: str) -> None:
        """Remove armor from the collection by its ID."""
        for armor in self.__armor_collection:
            if armor.name == armor_name:
                self.__armor_collection.remove(armor)
                return
        raise ValueError(f"No armor with ID '{armor_name}' found.")
