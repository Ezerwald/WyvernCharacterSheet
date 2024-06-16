from abstract_character import AbstractCharacter


class CharacterStates:
    def __init__(self, character: AbstractCharacter, states: str = None):
        """Initialize the character's states."""
        self.__character: AbstractCharacter = character
        self.__states: str = states

    @property
    def states(self) -> str:
        """Get the character's states."""
        return self.__states

    @states.setter
    def states(self, value: str):
        """Set the character's states."""
        self.__states = value
