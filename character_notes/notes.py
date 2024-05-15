from abstract_character import AbstractCharacter


class Notes:
    def __init__(self, character: AbstractCharacter, notes: str = ""):
        self.__character: AbstractCharacter = character
        self.__notes: str = notes

    @property
    def notes(self) -> str:
        """Get notes text"""
        return self.__notes

    @notes.setter
    def notes(self, notes: str):
        """Set notes text"""
        self.__notes = notes
