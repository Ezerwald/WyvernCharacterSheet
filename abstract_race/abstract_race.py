from abc import ABC
from typing import Dict
from character_stats import AbilityType


class AbstractRace(ABC):
    def __init__(self, name: str, abilities_bonuses: Dict[AbilityType, int], speed: int, description: str):
        self.__name = name
        self.__abilities_bonuses = abilities_bonuses
        self.__speed = speed
        self.__description = description

    @property
    def name(self) -> str:
        """Get race name"""
        return self.__name

    @property
    def abilities_bonuses(self) -> Dict[AbilityType, int]:
        """Get race abilities bonuses"""
        return self.__abilities_bonuses

    @property
    def speed(self) -> int:
        """Get race speed"""
        return self.__speed

    @property
    def description(self) -> str:
        """Get race description"""
        return self.__description
