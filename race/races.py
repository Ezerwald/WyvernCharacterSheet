from character_stats import AbilityType


class Race:
    def __init__(self, name: str, abilities_bonuses: dict[AbilityType, int], speed: int, features: str):
        self.__name = name
        self.__abilities_bonuses = abilities_bonuses
        self.__speed = speed
        self.__features = features

    @property
    def name(self) -> str:
        """Get race character_name"""
        return self.__name

    @property
    def abilities_bonuses(self) -> dict[AbilityType, int]:
        """Get race abilities bonuses"""
        return self.__abilities_bonuses

    @property
    def speed(self) -> int:
        """Get race speed"""
        return self.__speed

    @property
    def features(self) -> str:
        """Get race description"""
        return self.__features
