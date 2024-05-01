from abstract_character import AbstractCharacter


class CharacterFeatures:
    def __init__(self, character: AbstractCharacter):
        """Initializes CharacterFeatures object."""
        self.__character: AbstractCharacter = character
        self.__all_features = (f"   {self.__character.race.name} race features:\n" +
                               f"{self.__character.race.features} \n" +
                               f"   {self.__character.current_game_class.value.name} class features:\n" +
                               f"{self.__character.current_game_class.value.proficiencies}")

    @property
    def all_features(self) -> str:
        """Get all features."""
        return self.__all_features

    @all_features.setter
    def all_features(self, proficiencies: str):
        """Set all features."""
        self.__all_features = proficiencies
