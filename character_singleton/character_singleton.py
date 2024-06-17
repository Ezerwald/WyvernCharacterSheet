import json
from pathlib import Path
from typing import Dict, Tuple, Any

from character_stats import AbilityType
from skills_types import SkillType
from character.character_attribute_enum import CharacterAttribute
from character.character import Character
from abstract_character import AbstractCharacter


class CharacterSingleton:
    """A class to manage a single instance of a Character object."""

    __instance = None

    def __init__(self):
        """Initializes dictionary which assigns element_id to certain character attribute"""
        self.__input_id_to_object: Dict[str, Tuple[Any, str]] = {}

    def __new__(cls, *args, **kwargs):
        """Create a new instance of the class if it doesn't exist."""
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            cls.__instance.__character = None

        return cls.__instance

    @property
    def character(self) -> AbstractCharacter:
        """Get the character object."""
        return self.__instance.__character

    @character.setter
    def character(self, character: AbstractCharacter):
        """Set the character object."""
        self.__instance.__character = character

    def save_character_to_path(self, path: Path = None):
        """Save the character data to a JSON file to specific directory"""
        try:
            with path.open('w') as file:
                json.dump(self.pack_character_data(), file, indent=4)
                print(f"Saved {path}")
        except IOError as e:
            print(f"Error saving character data: {e}")
            raise e

    def create_character(self, character_data: Dict[str, Any]):
        """Create a new instance of the Character object."""
        print("Created from data:", character_data)
        self.__instance.__character = Character(character_data)

    def load_character_from_path(self, path: Path):
        """Load character data from specific directory."""
        try:
            with open(path, 'r') as file:
                # Retrieve data from file
                character_data = json.load(file)
                # Create data from retrieved data
                self.create_character(character_data)
                print(f"Loaded from path: {path}")
        except FileNotFoundError as e:
            print(f"File '{path}' not found.")
            raise e
        except json.JSONDecodeError as e:
            print(f"Invalid JSON format in '{path}'.")
            raise e

    def load_character_from_json(self, data: dict):
        """Load character data from a JSON file"""
        # Use the provided dictionary directly
        character_data = data
        # Create character from retrieved data
        self.create_character(character_data)
        print(f"Loaded character from storage data: {data}")

    def pack_character_data(self) -> Dict[str, Any]:
        """
        Pack all character's data into a dictionary.
        Write here data that can be inputted by user on website
        """
        character = self.__instance.__character

        name = character.biography.name
        game_class_type = character.current_game_class.value.name
        level = character.level.value
        background = character.biography.background
        race = character.race.value.name
        alignment = character.biography.alignment
        experience_points = character.experience_points.value
        abilities_scores = {ability.value: character.abilities[ability].score for ability in AbilityType}
        saving_throws_proficiencies = {ability.value: character.saving_throws[ability].proficiency for ability in
                                       AbilityType}
        skills_proficiencies = {skill.value: character.skills[skill].proficiency for skill in SkillType}
        shield = character.shield.equipped
        equipped_armor = character.equipped_armor.armor.name
        custom_armor_class = character.armor_class.custom_armor_class
        current_hit_points = character.hit_points.current_hit_points
        custom_max_hit_points = character.hit_points.custom_max_hit_points
        temporary_hit_points = character.temporary_hit_points.value
        hit_dices_left = character.hit_dices_pool.current_hit_dices_amount
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
        speed = character.speed.value
        notes = character.notes.notes
        states = character.states.states

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
            CharacterAttribute.CUSTOM_ARMOR_CLASS.value: custom_armor_class,
            CharacterAttribute.CURRENT_HIT_POINTS.value: current_hit_points,
            CharacterAttribute.CUSTOM_MAX_HIT_POINTS.value: custom_max_hit_points,
            CharacterAttribute.TEMPORARY_HIT_POINTS.value: temporary_hit_points,
            CharacterAttribute.CURRENT_HIT_DICES_AMOUNT.value: hit_dices_left,
            CharacterAttribute.SUCCESSFUL_DEATH_SAVES.value: successful_death_saves,
            CharacterAttribute.FAILED_DEATH_SAVES.value: failed_death_saves,
            CharacterAttribute.ATTACKS_LIST.value: attacks_list,
            CharacterAttribute.INVENTORY.value: inventory,
            CharacterAttribute.FEATURES.value: features,
            CharacterAttribute.SPEED.value: speed,
            CharacterAttribute.NOTES.value: notes,
            CharacterAttribute.STATES.value: states
        }
        return packed_data

    def get_id_to_object_list(self) -> Dict[str, Tuple[Any, str]]:
        """
        Return dictionary of character's attributes bounded to their corresponding input id.
        Is used to display all character data on frontend
        """
        self.__input_id_to_object = {
            **self.update_biography_mapping(),
            **self.update_notes_mapping(),
            **self.update_abilities_scores_mapping(),
            **self.update_abilities_modifiers_mapping(),
            **self.update_proficiency_bonus_mapping(),
            **self.update_saving_throws_proficiencies_mapping(),
            **self.update_saving_throws_bonuses_mapping(),
            **self.update_skills_proficiencies_mapping(),
            **self.update_skills_bonuses_mapping(),
            **self.update_battle_stats_mapping(),
            **self.update_health_mapping(),
            **self.update_passive_perception_mapping(),
            **self.update_inventory_mapping(),
            **self.update_features_mapping(),
            **self.update_states_mapping()
        }
        return self.__input_id_to_object

    # Separate mapping for update_id_to_object_list()
    def update_biography_mapping(self) -> Dict[str, Tuple[Any, str]]:
        return {
            "character-name": (self.character.biography, 'name'),
            "character-class": (self.character.current_game_class, 'name'),
            "character-race": (self.character.race, 'name'),
            "character-level": (self.character.level, 'value'),
            "character-background": (self.character.biography, 'background'),
            "character-alignment": (self.character.biography, 'alignment'),
            "character-experience": (self.character.experience_points, 'value'),
        }

    def update_notes_mapping(self) -> Dict[str, Tuple[Any, str]]:
        return {
            "notes": (self.character.notes, 'notes'),
        }

    def update_abilities_scores_mapping(self) -> Dict[str, Tuple[Any, str]]:
        return {
            'strength-score': (self.character.abilities[AbilityType.STRENGTH], 'score'),
            'dexterity-score': (self.character.abilities[AbilityType.DEXTERITY], 'score'),
            'constitution-score': (self.character.abilities[AbilityType.CONSTITUTION], 'score'),
            'intelligence-score': (self.character.abilities[AbilityType.INTELLIGENCE], 'score'),
            'wisdom-score': (self.character.abilities[AbilityType.WISDOM], 'score'),
            'charisma-score': (self.character.abilities[AbilityType.CHARISMA], 'score'),
        }

    def update_abilities_modifiers_mapping(self) -> Dict[str, Tuple[Any, str]]:
        return {
            'strength-modifier': (self.character.abilities[AbilityType.STRENGTH], 'modifier'),
            'dexterity-modifier': (self.character.abilities[AbilityType.DEXTERITY], 'modifier'),
            'constitution-modifier': (self.character.abilities[AbilityType.CONSTITUTION], 'modifier'),
            'intelligence-modifier': (self.character.abilities[AbilityType.INTELLIGENCE], 'modifier'),
            'wisdom-modifier': (self.character.abilities[AbilityType.WISDOM], 'modifier'),
            'charisma-modifier': (self.character.abilities[AbilityType.CHARISMA], 'modifier'),
        }

    def update_proficiency_bonus_mapping(self) -> Dict[str, Tuple[Any, str]]:
        return {
            'prof-bonus': (self.character.prof_bonus, 'value'),
        }

    def update_saving_throws_proficiencies_mapping(self) -> Dict[str, Tuple[Any, str]]:
        return {
            'strength-saving-throw-prof': (self.character.saving_throws[AbilityType.STRENGTH], 'proficiency'),
            'dexterity-saving-throw-prof': (self.character.saving_throws[AbilityType.DEXTERITY], 'proficiency'),
            'constitution-saving-throw-prof': (self.character.saving_throws[AbilityType.CONSTITUTION], 'proficiency'),
            'intelligence-saving-throw-prof': (self.character.saving_throws[AbilityType.INTELLIGENCE], 'proficiency'),
            'wisdom-saving-throw-prof': (self.character.saving_throws[AbilityType.WISDOM], 'proficiency'),
            'charisma-saving-throw-prof': (self.character.saving_throws[AbilityType.CHARISMA], 'proficiency'),
        }

    def update_saving_throws_bonuses_mapping(self) -> Dict[str, Tuple[Any, str]]:
        return {
            'strength-saving-throw-bonus': (self.character.saving_throws[AbilityType.STRENGTH], 'value'),
            'dexterity-saving-throw-bonus': (self.character.saving_throws[AbilityType.DEXTERITY], 'value'),
            'constitution-saving-throw-bonus': (self.character.saving_throws[AbilityType.CONSTITUTION], 'value'),
            'intelligence-saving-throw-bonus': (self.character.saving_throws[AbilityType.INTELLIGENCE], 'value'),
            'wisdom-saving-throw-bonus': (self.character.saving_throws[AbilityType.WISDOM], 'value'),
            'charisma-saving-throw-bonus': (self.character.saving_throws[AbilityType.CHARISMA], 'value'),
        }

    def update_skills_proficiencies_mapping(self) -> Dict[str, Tuple[Any, str]]:
        return {
            'acrobatics-skill-prof': (self.character.skills[SkillType.ACROBATICS], 'proficiency'),
            'animal-handling-skill-prof': (self.character.skills[SkillType.ANIMAL_HANDLING], 'proficiency'),
            'arcana-skill-prof': (self.character.skills[SkillType.ARCANA], 'proficiency'),
            'athletics-skill-prof': (self.character.skills[SkillType.ATHLETICS], 'proficiency'),
            'deception-skill-prof': (self.character.skills[SkillType.DECEPTION], 'proficiency'),
            'history-skill-prof': (self.character.skills[SkillType.HISTORY], 'proficiency'),
            'insight-skill-prof': (self.character.skills[SkillType.INSIGHT], 'proficiency'),
            'intimidation-skill-prof': (self.character.skills[SkillType.INTIMIDATION], 'proficiency'),
            'investigation-skill-prof': (self.character.skills[SkillType.INVESTIGATION], 'proficiency'),
            'medicine-skill-prof': (self.character.skills[SkillType.MEDICINE], 'proficiency'),
            'nature-skill-prof': (self.character.skills[SkillType.NATURE], 'proficiency'),
            'perception-skill-prof': (self.character.skills[SkillType.PERCEPTION], 'proficiency'),
            'performance-skill-prof': (self.character.skills[SkillType.PERFORMANCE], 'proficiency'),
            'persuasion-skill-prof': (self.character.skills[SkillType.PERSUASION], 'proficiency'),
            'religion-skill-prof': (self.character.skills[SkillType.RELIGION], 'proficiency'),
            'sleight-of-hand-skill-prof': (self.character.skills[SkillType.SLEIGHT_OF_HAND], 'proficiency'),
            'stealth-skill-prof': (self.character.skills[SkillType.STEALTH], 'proficiency'),
            'survival-skill-prof': (self.character.skills[SkillType.SURVIVAL], 'proficiency'),
        }

    def update_skills_bonuses_mapping(self) -> Dict[str, Tuple[Any, str]]:
        return {
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
            'survival-skill-bonus': (self.character.skills[SkillType.SURVIVAL], 'value'),
        }

    def update_battle_stats_mapping(self) -> Dict[str, Tuple[Any, str]]:
        return {
            'armor-class': (self.character.armor_class, 'armor_class'),
            'initiative': (self.character.initiative, 'value'),
            'speed': (self.character.speed, 'value'),
        }

    def update_health_mapping(self) -> Dict[str, Tuple[Any, str]]:
        return {
            'current-hit-points': (self.character.hit_points, 'current_hit_points'),
            'max-hit-points': (self.character.hit_points, 'max_hit_points'),
            'temporary-hit-points': (self.character.temporary_hit_points, 'value'),
            'hit-dice-type': (self.character.hit_dices_pool, 'hit_dice_type'),
            'current-hit-dices-amount': (self.character.hit_dices_pool, 'current_hit_dices_amount'),
            'max-hit-dices-amount': (self.character.hit_dices_pool, 'max_hit_dices_amount'),
            'successful-death-saves': (self.character.death_saves, 'successful_saves'),
            'failed-death-saves': (self.character.death_saves, 'failed_saves'),
        }

    def update_passive_perception_mapping(self) -> Dict[str, Tuple[Any, str]]:
        return {
            'passive-perception': (self.character.passive_perception, 'value'),
        }

    def update_inventory_mapping(self) -> Dict[str, Tuple[Any, str]]:
        return {
            "inventory": (self.character.inventory, 'items'),
        }

    def update_features_mapping(self) -> Dict[str, Tuple[Any, str]]:
        return {
            'features': (self.character.features, 'all_features')
        }

    def update_states_mapping(self) -> Dict[str, Tuple[Any, str]]:
        return {
            'states': (self.character.states, 'states'),
        }

    # Managing attributes
    def set_attribute(self, element_id: str, attribute_value: Any) -> None:
        if attribute_value == 'on':
            attribute_value = True
        elif attribute_value == 'off':
            attribute_value = False
        # Access the object and attribute using the key, then update the attribute value
        object_instance, attribute_name = self.__input_id_to_object[element_id]
        setattr(object_instance, attribute_name, attribute_value)

        print(f'"{element_id}" was updated with value {attribute_value}')

    def get_attribute(self, element_id: str) -> Any:
        # Access the object and attribute using the key, then return the attribute value
        object_instance, attribute_name = self.__input_id_to_object[element_id]
        return getattr(object_instance, attribute_name)
