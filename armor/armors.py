from uuid import uuid4
from .armor_types import ArmorType


class Armor:
    """Represents a piece of armor."""

    def __init__(self, name: str, armor_type: ArmorType, basic_armor_class: int,
                 max_dexterity_bonus: int, stealth_disadvantage: bool):
        """Initialize an Armor instance."""
        self.__id = uuid4()
        self.__name = name
        self.__armor_type = armor_type
        self.__basic_armor_class = basic_armor_class
        self.__max_dexterity_bonus = max_dexterity_bonus
        self.__stealth_disadvantage = stealth_disadvantage

    @property
    def id(self) -> int:
        """Get the unique identifier of the armor."""
        return int(self.__id)

    @property
    def name(self) -> str:
        """Get the character_name of the armor."""
        return self.__name

    @property
    def armor_type(self) -> ArmorType:
        """Get the type of armor."""
        return self.__armor_type

    @property
    def basic_armor_class(self) -> int:
        """Get t base armor class provided by the armor."""
        return self.__basic_armor_class

    @property
    def max_dexterity_bonus(self) -> int:
        """Get the maximum dexterity bonus that can be applied."""
        return self.__max_dexterity_bonus

    @property
    def stealth_disadvantage(self) -> bool:
        """Indicates if the armor imposes disadvantage on stealth checks."""
        return self.__stealth_disadvantage

    def __str__(self) -> str:
        """A string representation of the armor."""
        return f"Armor(id='{self.id}', character_name='{self.name}', armor_type='{self.armor_type}', " \
               f"basic_armor_class={self.basic_armor_class}, " \
               f"max_dexterity_bonus={self.max_dexterity_bonus}, " \
               f"stealth_disadvantage={self.stealth_disadvantage})"
