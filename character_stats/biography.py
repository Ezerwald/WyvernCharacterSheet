from abstract_character import AbstractCharacter


class Biography:
    def __init__(self, character: AbstractCharacter, character_name: str = "", background: str = "",
                 alignment: str = "", player_name: str = ""):
        self.__player_name = player_name
        self.__character = character
        self.__character_name = character_name
        self.__background = background
        self.__alignment = alignment

    @property
    def __character_name(self) -> str:
        """Get the character's name."""
        return self.__name

    @__character_name.setter
    def __character_name(self, name: str):
        """Set the character's name."""
        if name.strip():  # Ensure the character_name is not empty
            self.__name = name.strip()
        else:
            raise ValueError("Name cannot be empty.")

    @property
    def __background(self) -> str:
        """Get the character's background."""
        return self.__background

    @__background.setter
    def __background(self, background: str):
        """Set the character's background."""
        self.__background = background.strip()

    @property
    def __alignment(self) -> str:
        """Get the character's alignment."""
        return self.__alignment

    @__alignment.setter
    def __alignment(self, alignment: str):
        """Set the character's alignment."""
        self.__alignment = alignment.strip()

    @property
    def player_name(self):
        return

