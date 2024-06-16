from abstract_character import AbstractCharacter


class Biography:
    def __init__(self, character: AbstractCharacter, name: str = "", background: str = "",
                 alignment: str = ""):
        self.__name = name
        self.__character = character
        self.__background = background
        self.__alignment = alignment

    @property
    def name(self) -> str:
        """Get the character's name."""
        return self.__name

    @name.setter
    def name(self, name: str):
        """Set the character's name."""
        self.__name = name.strip()

    @property
    def background(self) -> str:
        """Get the character's background."""
        return self.__background

    @background.setter
    def background(self, background: str):
        """Set the character's background."""
        self.__background = background.strip()

    @property
    def alignment(self) -> str:
        """Get the character's alignment."""
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        """Set the character's alignment."""
        self.__alignment = alignment.strip()

