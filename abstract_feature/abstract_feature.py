from abc import ABC, abstractmethod

from abstract_character import AbstractCharacter


class AbstractFeature(ABC):
    def __init__(self, character: AbstractCharacter):
        self.__character = character
        self.__name = None
        self.__description = None
        self.__source = None

    @abstractmethod
    def functionality(self):
        """Functionality of feature"""
        pass

    @property
    def name(self) -> str:
        """Get the name of the feature."""
        return self.__name

    @property
    def description(self) -> str:
        """Get the description of the feature."""
        return self.__description

    @property
    def source(self) -> str:
        """Get the source of the feature."""
        return self.__source
