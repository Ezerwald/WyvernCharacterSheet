from abstract_character import AbstractCharacter


class DeathSaves:
    def __init__(self, character: AbstractCharacter):
        self.character = character
        self.__successful_saves = 0
        self.__failed_saves = 0

    @property
    def successful_saves(self):
        """Gets successful saves"""
        return self.__successful_saves

    @successful_saves.setter
    def successful_saves(self, value):
        """Sets successful saves"""
        self.__successful_saves = value

    @property
    def failed_saves(self):
        """Gets failed saves"""
        return self.__failed_saves

    @failed_saves.setter
    def failed_saves(self, value):
        """Sets failed saves"""
        self.__failed_saves = value
