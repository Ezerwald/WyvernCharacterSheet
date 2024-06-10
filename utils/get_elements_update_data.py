from character_singleton import CharacterSingleton

character_singleton = CharacterSingleton()


def get_elements_update_data():
    """Get all elements that should be updated and their new data."""
    data = {element: character_singleton.get_attribute(element)
            for element in character_singleton.get_input_id_to_object()}
    return data
