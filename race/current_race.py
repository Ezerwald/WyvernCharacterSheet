from abstract_character import AbstractCharacter
from .races import Race
from .races_collection_instance import basic_races_collection


class CurrentRace:
    def __init__(self, character: AbstractCharacter, race_name: str):
        self.character = character
        self.__race_name = race_name

    @property
    def value(self) -> Race:
        """Get the current character race"""
        return basic_races_collection.get_race_by_name(self.__race_name)

    @property
    def name(self) -> str:
        """Get the name of the current character race"""
        return self.__race_name

    @name.setter
    def name(self, value: str):
        """Set the current character race"""
        self.__race_name = value
