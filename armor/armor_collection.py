from typing import List, Optional, Tuple

from armor import Armor


class ArmorCollection:
    def __init__(self):
        self.__armor_collection: List[Armor] = []

    def add_armor(self, armor: Armor) -> None:
        """Add armor to the collection."""
        if self.get_armor_by_id(armor.id) is not None:
            raise ValueError(f"Armor with ID '{armor.id}' already exists in the collection.")
        self.__armor_collection.append(armor)

    def get_armor_by_id(self, armor_id: int) -> Optional[Armor]:
        """Get armor by its ID."""
        for armor in self.__armor_collection:
            if armor.id == armor_id:
                return armor
        return None

    def get_armor_by_name(self, name: str) -> Optional[Armor]:
        """Get armor by its ID."""
        for armor in self.__armor_collection:
            if armor.name == name:
                return armor
        return None

    def get_all_armors(self) -> list[tuple[str, int]]:
        """Get names of all armor types in the collection."""
        return [(armor.name, armor.id) for armor in self.__armor_collection]

    def remove_armor(self, armor_id: int) -> None:
        """Remove armor from the collection by its ID."""
        for armor in self.__armor_collection:
            if armor.id == armor_id:
                self.__armor_collection.remove(armor)
                return
        raise ValueError(f"No armor with ID '{armor_id}' found.")