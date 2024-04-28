
class GameClass:
    def __init__(self, game_class):
        self.__game_class = game_class

    @property
    def value(self):
        return self.__game_class

    @value.setter
    def value(self, new_value):
        self.__game_class = new_value
