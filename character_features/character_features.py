from abstract_character import AbstractCharacter


class CharacterFeatures:
    def __init__(self, character: AbstractCharacter, features: str = None):
        """Initializes CharacterFeatures object."""
        self._character: AbstractCharacter = character
        self._all_features = features or (
            f"   {self._character.race.name} race features:\n"
            f"{self._character.race.features}\n"
            f"   {self._character.current_game_class.value.name} class features:\n"
            f"{self._character.current_game_class.value.proficiencies}"
        )

    @property
    def all_features(self) -> str:
        """Get all features."""
        return self._all_features

    @all_features.setter
    def all_features(self, features: str):
        """Set all features."""
        self._all_features = features