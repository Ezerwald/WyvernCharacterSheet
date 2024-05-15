from character_singleton import CharacterSingleton

character_singleton = CharacterSingleton()

def show_character_info():
    """Prints to console all information about character"""
    character = character_singleton.character
    print(f"-----Showing {character.biography.name} information-----")
    packed_character_data = character_singleton.pack_character_data()
    for data in packed_character_data:
        print(data+":", packed_character_data[data])
