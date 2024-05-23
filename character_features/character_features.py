from abstract_character import AbstractCharacter


class CharacterFeatures:
    def __init__(self, character: AbstractCharacter, features: str = None):
        """Initializes CharacterFeatures object."""
        self.__character: AbstractCharacter = character
        self.__all_features = features or self.get_default_features()

    @property
    def all_features(self) -> str:
        """Get all features."""
        return self.__all_features

    @all_features.setter
    def all_features(self, features: str):
        """Set all features."""
        if features == "":
            self.__all_features = self.get_default_features()
        else:
            self.__all_features = features

    def get_default_features(self):
        features = (
            f"* {self.__character.race.value.name} race features:\n"
            f"{self.__character.race.value.features}\n\n"
            f"* {self.__character.current_game_class.value.name} class features:\n"
            f"{self.__character.current_game_class.value.proficiencies}\n\n"
        )
        return features