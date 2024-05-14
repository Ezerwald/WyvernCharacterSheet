import json
from pathlib import Path
from typing import Dict
from character_stats import AbilityType
from skills_types import SkillType
from .character_attribute_enum import CharacterAttribute
from .character import Character
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
                json.dump(self.pack_character_data(self.__instance.__character), file, indent=4)
                print(f"Saved {filename}")
        except FileNotFoundError as e:
            print(f"Error saving character data: {e}")
        # except Exception as e:
        #     print(f"Error saving character data: {e}")

    def create_character(self, character_creation_data: tuple):
        """Create a new instance of the Character object."""
        self.__instance.__character = Character(*character_creation_data)

    def load_character(self, filename: Path):
        """Load character data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                character_data = json.load(file)
                self.create_character(character_data)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"Invalid JSON format in '{filename}'.")

    def pack_character_data(self, character: AbstractCharacter) -> Dict[CharacterAttribute, any]:
        """Pack character data into a dictionary."""
        packed_data = {
            CharacterAttribute.NAME: character.biography.name,
            CharacterAttribute.GAME_CLASS_TYPE: character.current_game_class.value.name,
            CharacterAttribute.LEVEL: character.level.value,
            CharacterAttribute.BACKGROUND: character.biography.background,
            CharacterAttribute.RACE: character.race.name,
            CharacterAttribute.ALIGNMENT: character.biography.alignment,
            CharacterAttribute.EXPERIENCE_POINTS: character.experience_points.value,
            CharacterAttribute.ABILITIES_SCORES: {ability.value: character.abilities[ability].score
                                                  for ability in AbilityType},
            CharacterAttribute.SAVING_THROWS_PROFICIENCIES: {ability.value: character.saving_throws[ability].proficiency
                                                             for ability in AbilityType},
            CharacterAttribute.SKILLS_PROFICIENCIES: {skill.value: character.skills[skill].proficiency
                                                      for skill in SkillType},
            CharacterAttribute.SHIELD: character.shield.equipped,
            CharacterAttribute.EQUIPPED_ARMOR: character.equipped_armor.armor.name,
            CharacterAttribute.CURRENT_HIT_POINTS: character.hit_points.current_hit_points.value,
            CharacterAttribute.MAX_HIT_POINTS: character.hit_points.max_hit_points,
            CharacterAttribute.TEMPORARY_HIT_POINTS: character.hit_points.temporary_hit_points,
            CharacterAttribute.HIT_DICES_LEFT: character.hit_dices_pool.hit_dices_left,
            CharacterAttribute.SUCCESSFUL_DEATH_SAVES: character.death_saves.successful_saves,
            CharacterAttribute.FAILED_DEATH_SAVES: character.death_saves.failed_saves,
            CharacterAttribute.ATTACKS_LIST: {attack.name: [attack.main_ability.value,
                                                            attack.proficiency,
                                                            attack.basic_damage,
                                                            attack.extra_attack_bonus,
                                                            attack.extra_damage_bonus]
                                              for attack in character.attacks_list.get_all_attacks()},
            CharacterAttribute.INVENTORY: character.inventory.items,
            CharacterAttribute.FEATURES: character.features.all_features
        }
        return packed_data

    @property
    def character(self) -> Character:
        """Get the character object."""
        return self.__instance.__character

    @character.setter
    def character(self, character: AbstractCharacter):
        """Set the character object."""
        self.__instance.__character = character
