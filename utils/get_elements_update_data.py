from character_singleton import CharacterSingleton
from constants import LIST_OF_ELEMENTS_TO_UPDATE

character_singleton = CharacterSingleton()


def get_elements_update_data():
    data = {element: character_singleton.get_attribute(element)
            for element in LIST_OF_ELEMENTS_TO_UPDATE}
    return data
