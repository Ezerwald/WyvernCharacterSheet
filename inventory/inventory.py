class Inventory:
    def __init__(self, character, items: str = None):
        self.__character = character
        self.__items = items

    @property
    def items(self):
        """Get inventory"""
        return self.__items

    @items.setter
    def items(self, value):
        """Set inventory"""
        self.__items = value
