from abc import ABC, abstractmethod
from typing import Dict


class AbstractCharacter(ABC):
    """Abstract base class for __character."""

    def __init__(self):
        self.__biography = None
        self.__current_game_class = None
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
        self.__hit_points = None
        self.__hit_dices_pool = None
        self.__temporary_hit_points = None
        self.__race = None
        self.__passive_perception = None
        self.__attacks_list = None
        self.__features = None
        self.__speed = None
        self.__experience_points = None
        self.__inventory = None
        self.__notes = None
        self.__states = None

    @abstractmethod
    def biography(self):
        """Get the biography of character."""
        pass

    @abstractmethod
    def current_game_class(self):
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

    @abstractmethod
    def hit_points(self):
        """Get the hit points object."""
        pass

    @abstractmethod
    def hit_dices_pool(self):
        """Get the hit dices pool."""
        pass

    @abstractmethod
    def temporary_hit_points(self):
        """Get the temporary hit points object."""
        pass

    @abstractmethod
    def race(self):
        """Get the race."""
        pass

    @abstractmethod
    def passive_perception(self):
        """Get passive perception."""
        pass

    @abstractmethod
    def attacks_list(self):
        """Get the attacks list."""
        pass

    @abstractmethod
    def features(self):
        """Get the features."""
        pass

    @abstractmethod
    def speed(self):
        """Get the speed."""
        pass

    @abstractmethod
    def experience_points(self):
        """Get experience points"""
        pass

    @abstractmethod
    def inventory(self):
        """Get inventory."""
        pass

    @abstractmethod
    def notes(self):
        """Get the notes."""
        pass

    @abstractmethod
    def states(self):
        """Get the character_states."""
        pass
