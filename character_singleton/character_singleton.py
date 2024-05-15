import json
from pathlib import Path
from typing import Dict, Tuple
from character_stats import AbilityType
from skills_types import SkillType
from character.character_attribute_enum import CharacterAttribute
from character.character import Character
from abstract_character import AbstractCharacter
from utils import get_default_downloads_folder


class CharacterSingleton:
    """A class to manage a single instance of a Character object."""

    __instance = None

    def __new__(cls, *args, **kwargs):
        """Create a new instance of the class if it doesn't exist."""
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            cls.__instance.__character = None
        return cls.__instance

    def save_character(self, filename: Path = None):
        """Save the character data to a JSON file. If not provided, the default downloads folder is used."""
        if filename is None:
            filename = get_default_downloads_folder() / "character_saved_data.json"
        try:
            with open(filename, 'w') as file:
                json.dump(self.pack_character_data(), file, indent=4)
                print(f"Saved {filename}")
        except FileNotFoundError as e:
            print(f"Error saving character data: {e}")
        # except Exception as e:
        #     print(f"Error saving character data: {e}")

    def create_character(self, character_data: tuple):
        """Create a new instance of the Character object."""
        print("Created from data:", character_data)
        self.__instance.__character = Character(*character_data)

    def load_character(self, filename: Path):
        """Load character data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                character_data = json.load(file)
                unpacked_character_data = self.unpack_character_data(character_data)
                self.create_character(unpacked_character_data)
                print(f"Loaded {filename}")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"Invalid JSON format in '{filename}'.")

    def pack_character_data(self) -> Dict[str, any]:
        """Pack character data into a dictionary."""
        character = self.__instance.__character

        name = character.biography.name
        game_class_type = character.current_game_class.value.name
        level = character.level.value
        background = character.biography.background
        race = character.race.name
        alignment = character.biography.alignment
        experience_points = character.experience_points.value
        abilities_scores = {ability.value: character.abilities[ability].score for ability in AbilityType}
        saving_throws_proficiencies = {ability.value: character.saving_throws[ability].proficiency for ability in
                                       AbilityType}
        skills_proficiencies = {skill.value: character.skills[skill].proficiency for skill in SkillType}
        shield = character.shield.equipped
        equipped_armor = character.equipped_armor.armor.name
        current_hit_points = character.hit_points.current_hit_points
        max_hit_points = character.hit_points.max_hit_points
        temporary_hit_points = character.temporary_hit_points.value
        hit_dices_left = character.hit_dices_pool.hit_dices_left
        successful_death_saves = character.death_saves.successful_saves
        failed_death_saves = character.death_saves.failed_saves
        attacks_list = [(attack.name,
                         attack.main_ability.value,
                         attack.proficiency,
                         attack.basic_damage,
                         attack.extra_attack_bonus,
                         attack.extra_damage_bonus)
                        for attack in character.attacks_list.get_all_attacks()]
        inventory = character.inventory.items
        features = character.features.all_features
        notes = character.notes.notes

        # Create the dictionary with the defined variables
        packed_data = {
            CharacterAttribute.NAME.value: name,
            CharacterAttribute.GAME_CLASS_TYPE.value: game_class_type,
            CharacterAttribute.LEVEL.value: level,
            CharacterAttribute.BACKGROUND.value: background,
            CharacterAttribute.RACE.value: race,
            CharacterAttribute.ALIGNMENT.value: alignment,
            CharacterAttribute.EXPERIENCE_POINTS.value: experience_points,
            CharacterAttribute.ABILITIES_SCORES.value: abilities_scores,
            CharacterAttribute.SAVING_THROWS_PROFICIENCIES.value: saving_throws_proficiencies,
            CharacterAttribute.SKILLS_PROFICIENCIES.value: skills_proficiencies,
            CharacterAttribute.SHIELD.value: shield,
            CharacterAttribute.EQUIPPED_ARMOR.value: equipped_armor,
            CharacterAttribute.CURRENT_HIT_POINTS.value: current_hit_points,
            CharacterAttribute.MAX_HIT_POINTS.value: max_hit_points,
            CharacterAttribute.TEMPORARY_HIT_POINTS.value: temporary_hit_points,
            CharacterAttribute.HIT_DICES_LEFT.value: hit_dices_left,
            CharacterAttribute.SUCCESSFUL_DEATH_SAVES.value: successful_death_saves,
            CharacterAttribute.FAILED_DEATH_SAVES.value: failed_death_saves,
            CharacterAttribute.ATTACKS_LIST.value: attacks_list,
            CharacterAttribute.INVENTORY.value: inventory,
            CharacterAttribute.FEATURES.value: features,
            CharacterAttribute.NOTES.value: notes
        }
        return packed_data

    def unpack_character_data(self, packed_data: Dict[str, any]) -> Tuple:
        """Unpack character data from a dictionary into a tuple of values."""
        unpacked_data: Tuple = tuple(packed_data.values())
        return unpacked_data

    @property
    def character(self) -> Character:
        """Get the character object."""
        return self.__instance.__character

    @character.setter
    def character(self, character: AbstractCharacter):
        """Set the character object."""
        self.__instance.__character = character