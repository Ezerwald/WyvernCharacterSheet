from abstract_character import AbstractCharacter
from character_stats import AbilityType
from .abilities_names import abilities_names


def show_all_stats(character: AbstractCharacter):
    for ability in AbilityType:
        print(f"{abilities_names[ability]}: {character.abilities[ability].score}")
