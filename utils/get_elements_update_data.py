from character_singleton import CharacterSingleton

character_singleton = CharacterSingleton()


def get_elements_update_data():
    data = {element: character_singleton.get_attribute(element)
            for element in CharacterSingleton.input_id_to_object}
    return data
