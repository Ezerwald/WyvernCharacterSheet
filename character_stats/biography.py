from abstract_character import AbstractCharacter


class Biography:
    def __init__(self, character: AbstractCharacter, character_name: str = "", background: str = "", alignment: str = ""):
        self.__character = character
        self.name = character_name
        self.background = background
        self.alignment = alignment

    @property
    def name(self) -> str:
        """Get the character's character_name."""
        return self.__name

    @name.setter
    def name(self, name: str):
        """Set the character's character_name."""
        if name.strip():  # Ensure the character_name is not empty
            self.__name = name.strip()
        else:
            raise ValueError("Name cannot be empty.")

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
