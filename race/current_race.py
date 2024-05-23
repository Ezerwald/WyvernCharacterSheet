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
        return self.get_race_from_collection()

    @property
    def name(self) -> str:
        """Get the name of the current character race"""
        return self.__race_name

    @name.setter
    def name(self, value: str):
        """Set the current character race"""
        if value in basic_races_collection.get_all_races():
            self.__race_name = value

    def get_race_from_collection(self) -> Race:
        return basic_races_collection.get_race_by_name(self.__race_name)
