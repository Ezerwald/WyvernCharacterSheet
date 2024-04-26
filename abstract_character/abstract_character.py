from abc import ABC, abstractmethod
from typing import Dict


class AbstractCharacter(ABC):
    """Abstract base class for character."""

    def __init__(self):
        self.__game_class = None
        self.__level = None
        self.__prof_bonus = None
        self.__abilities = None
        self.__saving_throws = None
        self.__skills = None
        self.__shield = None
        self.__equipped_armor = None
        self.__armor_class = None
        self.__initiative = None
        self.__death_saves = None

    @abstractmethod
    def game_class(self):
        """Get the game class."""
        pass

    @abstractmethod
    def level(self):
        """Get the __level."""
        pass

    @abstractmethod
    def prof_bonus(self):
        """Get the proficiency bonus."""
        pass

    @abstractmethod
    def abilities(self) -> Dict:
        """Get the __abilities."""
        pass

    @abstractmethod
    def saving_throws(self) -> Dict:
        """Get the saving throws."""
        pass

    @abstractmethod
    def skills(self) -> Dict:
        """Get the skills."""
        pass

    @abstractmethod
    def equipped_armor(self):
        """Get the equipped armor."""
        pass

    @abstractmethod
    def armor_class(self):
        """Get the armor class."""
        pass

    @abstractmethod
    def shield(self):
        """Get the __shield object."""
        pass

    @abstractmethod
    def initiative(self):
        """Get the initiative bonus."""
        pass

    @abstractmethod
    def death_saves(self):
        """Get the death saves object."""
        pass
