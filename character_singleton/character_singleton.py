import json
from pathlib import Path
from typing import Dict, Tuple, Any
from character_stats import AbilityType
from skills_types import SkillType
from character.character_attribute_enum import CharacterAttribute
from character.character import Character
from abstract_character import AbstractCharacter
from utils import get_default_downloads_folder


class CharacterSingleton:
    """A class to manage a single instance of a Character object."""

    __instance = None

    def __init__(self):
        # Creates dictionary which assigns element_id to certain character attribute
        self.__input_id_to_object: Dict[str, Tuple[Any, str]] = {}

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
        self.update_id_to_object_list()

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

    def pack_character_data(self) -> Dict[str, Any]:
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

    def unpack_character_data(self, packed_data: Dict[str, Any]) -> Tuple:
        """Unpack character data from a dictionary into a tuple of values."""
        unpacked_data: Tuple = tuple(packed_data.values())
        return unpacked_data

    @property
    def character(self) -> AbstractCharacter:
        """Get the character object."""
        return self.__instance.__character

    @character.setter
    def character(self, character: AbstractCharacter):
        """Set the character object."""
        self.__instance.__character = character
        self.update_id_to_object_list()

    def update_id_to_object_list(self):
        self.__input_id_to_object = {
            # biography
            "character-name": (self.character.biography, 'name'),
            "character-class": (self.character.current_game_class.value, 'name'),
            "character-race": (self.character.race, 'name'),
            "character-level": (self.character.level, 'value'),
            "character-background": (self.character.biography, 'background'),
            "character-alignment": (self.character.biography, 'alignment'),
            "character-experience": (self.character.experience_points, 'value'),
            # notes
            "notes": (self.character.notes, 'notes'),
            # proficiency bonus
            "prof-bonus": (self.character.prof_bonus, 'value'),
            # abilities scores
            'strength-score': (self.character.abilities[AbilityType.STRENGTH], 'score'),
            'dexterity-score': (self.character.abilities[AbilityType.DEXTERITY], 'score'),
            'constitution-score': (self.character.abilities[AbilityType.CONSTITUTION], 'score'),
            'intelligence-score': (self.character.abilities[AbilityType.INTELLIGENCE], 'score'),
            'wisdom-score': (self.character.abilities[AbilityType.WISDOM], 'score'),
            'charisma-score': (self.character.abilities[AbilityType.CHARISMA], 'score'),
            # abilities modifiers
            'strength-modifier': (self.character.abilities[AbilityType.STRENGTH], 'modifier'),
            'dexterity-modifier': (self.character.abilities[AbilityType.DEXTERITY], 'modifier'),
            'constitution-modifier': (self.character.abilities[AbilityType.CONSTITUTION], 'modifier'),
            'intelligence-modifier': (self.character.abilities[AbilityType.INTELLIGENCE], 'modifier'),
            'wisdom-modifier': (self.character.abilities[AbilityType.WISDOM], 'modifier'),
            'charisma-modifier': (self.character.abilities[AbilityType.CHARISMA], 'modifier'),
            # saving throws
            'strength-saving-throw-bonus': (self.character.saving_throws[AbilityType.STRENGTH], 'value'),
            'dexterity-saving-throw-bonus': (self.character.saving_throws[AbilityType.DEXTERITY], 'value'),
            'constitution-saving-throw-bonus': (self.character.saving_throws[AbilityType.CONSTITUTION], 'value'),
            'intelligence-saving-throw-bonus': (self.character.saving_throws[AbilityType.INTELLIGENCE], 'value'),
            'wisdom-saving-throw-bonus': (self.character.saving_throws[AbilityType.WISDOM], 'value'),
            'charisma-saving-throw-bonus': (self.character.saving_throws[AbilityType.CHARISMA], 'value'),
            # initiative
            'initiative': (self.character.initiative, 'value'),
            # skills proficiencies
            'acrobatics-proficiency': (self.character.skills[SkillType.ACROBATICS], 'proficiency'),
            # skills bonuses
            'acrobatics-skill-bonus': (self.character.skills[SkillType.ACROBATICS], 'value'),
            'animal-handling-skill-bonus': (self.character.skills[SkillType.ANIMAL_HANDLING], 'value'),
            'arcana-skill-bonus': (self.character.skills[SkillType.ARCANA], 'value'),
            'athletics-skill-bonus': (self.character.skills[SkillType.ATHLETICS], 'value'),
            'deception-skill-bonus': (self.character.skills[SkillType.DECEPTION], 'value'),
            'history-skill-bonus': (self.character.skills[SkillType.HISTORY], 'value'),
            'insight-skill-bonus': (self.character.skills[SkillType.INSIGHT], 'value'),
            'intimidation-skill-bonus': (self.character.skills[SkillType.INTIMIDATION], 'value'),
            'investigation-skill-bonus': (self.character.skills[SkillType.INVESTIGATION], 'value'),
            'medicine-skill-bonus': (self.character.skills[SkillType.MEDICINE], 'value'),
            'nature-skill-bonus': (self.character.skills[SkillType.NATURE], 'value'),
            'perception-skill-bonus': (self.character.skills[SkillType.PERCEPTION], 'value'),
            'performance-skill-bonus': (self.character.skills[SkillType.PERFORMANCE], 'value'),
            'persuasion-skill-bonus': (self.character.skills[SkillType.PERSUASION], 'value'),
            'religion-skill-bonus': (self.character.skills[SkillType.RELIGION], 'value'),
            'sleight-of-hand-skill-bonus': (self.character.skills[SkillType.SLEIGHT_OF_HAND], 'value'),
            'stealth-skill-bonus': (self.character.skills[SkillType.STEALTH], 'value'),
            'survival-skill-bonus': (self.character.skills[SkillType.SURVIVAL], 'value')
        }

    def set_attribute(self, element_id: str, attribute_value: Any) -> None:
        # Access the object and attribute using the key, then update the attribute value
        object_instance, attribute_name = self.__input_id_to_object[element_id]
        setattr(object_instance, attribute_name, attribute_value)

        print(f"{attribute_name} was updated with value {attribute_value}")

        self.save_character("saved_characters/character_saved_data.json")

    def get_attribute(self, element_id: str) -> Any:
        # Access the object and attribute using the key, then return the attribute value
        object_instance, attribute_name = self.__input_id_to_object[element_id]
        return getattr(object_instance, attribute_name)
