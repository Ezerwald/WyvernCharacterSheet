class Inventory:
    def __init__(self, character, inventory: str = None):
        self.__character = character
        self.__inventory = inventory

    @property
    def inventory(self):
        """Get inventory"""
        return self.__inventory

    @inventory.setter
    def inventory(self, inventory):
        """Set inventory"""
        self.__inventory = inventory
