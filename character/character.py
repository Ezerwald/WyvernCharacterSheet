from typing import Dict, List, Tuple, Any
from abstract_character import AbstractCharacter
from character_notes import Notes
from shield import Shield
from character_stats import (
    Ability, Level, ProfBonus, AbilityType, Speed, Biography, ExperiencePoints, PassivePerception
)
from skills import Skill
from skills_types import SkillType
from initiative import Initiative
from armor import EquippedArmor, basic_armor_collection
from armor_class import ArmorClass
from health import DeathSaves, HitPoints, HitDicesPool, TemporaryHitPoints
from game_classes import CurrentGameClass
from race import CurrentRace, Race
from attacks import AttacksList, Attack
from character_features import CharacterFeatures
from inventory import Inventory
from saving_throws import SavingThrow
from utils import process_attacks_data


class Character(AbstractCharacter):
    """Represents a character in the game."""

    def __init__(self, character_data: Dict[str, Any]):
        """Retrieve attributes from character_data."""
        name: str = character_data['name']
        game_class_type: str = character_data['game_class_type']
        level: int = character_data['level']
        background: str = character_data['background']
        race: str = character_data['race']
        alignment: str = character_data['alignment']
        experience_points: int = character_data['experience_points']
        abilities_scores: Dict[str, int] = character_data['abilities_scores']
        saving_throws_proficiencies: Dict[str, bool] = character_data['saving_throws_proficiencies']
        skills_proficiencies: Dict[str, bool] = character_data['skills_proficiencies']
        shield: bool = character_data['shield']
        equipped_armor_name: str = character_data['equipped_armor_name']
        current_hit_points: int = character_data['current_hit_points']
        max_hit_points: int = character_data['max_hit_points']
        temporary_hit_points: int = character_data['temporary_hit_points']
        current_hit_dices_amount: int = character_data['current_hit_dices_amount']
        successful_death_saves: int = character_data['successful_death_saves']
        failed_death_saves: int = character_data['failed_death_saves']
        attacks_data_list: List[Tuple[str, str, bool, str, int, int]] = character_data['attacks_data_list']
        inventory: str = character_data['inventory']
        features: str = character_data['features']
        notes: str = character_data['notes']
        """Initialize a Character instance."""
        super().__init__()
        self.__initialize_biography(name, background, alignment)
        self.__initialize_game_class(game_class_type)
        self.__initialize_level(level)
        self.__initialize_race(race)
        self.__initialize_experience(experience_points)
        self.__initialize_abilities(abilities_scores)
        self.__initialize_saving_throws(saving_throws_proficiencies)
        self.__initialize_skills(skills_proficiencies)
        self.__initialize_shield(shield)
        self.__initialize_equipped_armor(equipped_armor_name)
        self.__initialize_hit_points(current_hit_points, max_hit_points)
        self.__initialize_temporary_hit_points(temporary_hit_points)
        self.__initialize_hit_dices(current_hit_dices_amount)
        self.__initialize_death_saves(successful_death_saves, failed_death_saves)
        self.__initialize_attacks(attacks_data_list)
        self.__initialize_inventory(inventory)
        self.__initialize_features(features)
        self.__initialize_notes(notes)

        self.__initialize_derived_attributes()

    """Initializers for character attributes"""

    def __initialize_biography(self, character_name: str, background: str, alignment: str):
        """Initialize the character's biography."""
        self.__biography = Biography(self, character_name, background, alignment)

    def __initialize_game_class(self, game_class_name: str):
        """Initialize the character's game class."""
        self.__current_game_class = CurrentGameClass(self, game_class_name)

    def __initialize_level(self, level: int):
        """Initialize the character's level."""
        self.__level = Level(self, level)

    def __initialize_race(self, race: str):
        """Initialize the character's race."""
        self.__race = CurrentRace(self, race)

    def __initialize_experience(self, experience_points: int):
        """Initialize the character's experience points."""
        self.__experience_points = ExperiencePoints(self, experience_points)

    def __initialize_abilities(self, abilities_scores: Dict[str, int]):
        """Initialize the character's abilities."""
        self.__abilities = {ability: Ability(self, ability, abilities_scores[ability.value]) for ability in AbilityType}

    def __initialize_saving_throws(self, saving_throws_proficiencies: Dict[str, bool]):
        """Initialize the character's saving throws."""
        self.__saving_throws = {ability: SavingThrow(self, ability, saving_throws_proficiencies[ability.value]) for
                                ability in AbilityType}

    def __initialize_skills(self, skills_proficiencies: Dict[str, bool]):
        """Initialize the character's skills."""
        self.__skills = {skill: Skill(self, skill, skills_proficiencies[skill.value])
                         for skill in SkillType}

    def __initialize_shield(self, shield: bool):
        """Initialize the character's shield."""
        self.__shield = Shield(self, shield)

    def __initialize_equipped_armor(self, equipped_armor_name: str):
        """Initialize the character's equipped armor."""
        self.__equipped_armor = EquippedArmor(self, basic_armor_collection.get_armor_by_name(equipped_armor_name))

    def __initialize_hit_points(self, current_hit_points: int, max_hit_points: int):
        """Initialize the character's hit points."""
        self.__hit_points = HitPoints(self, current_hit_points, max_hit_points)

    def __initialize_temporary_hit_points(self, temporary_hit_points: int):
        """Initialize the character's temporary hit points."""
        self.__temporary_hit_points = TemporaryHitPoints(self, temporary_hit_points)

    def __initialize_hit_dices(self, hit_dices_left: int):
        """Initialize the character's hit dices."""
        self.__hit_dices_pool = HitDicesPool(self, hit_dices_left)

    def __initialize_death_saves(self, successful_death_saves: int, failed_death_saves: int):
        """Initialize the character's death saves."""
        self.__death_saves = DeathSaves(self, successful_death_saves, failed_death_saves)

    def __initialize_attacks(self, attacks_data_list: List[Tuple[str, str, bool, str, int, int]]):
        """Initialize the character's attacks list."""
        self.__attacks_list = AttacksList(self, process_attacks_data(self, attacks_data_list))

    def __initialize_inventory(self, inventory: str):
        """Initialize the character's inventory."""
        self.__inventory = Inventory(self, inventory)

    def __initialize_features(self, features: str):
        """Initialize the character's features"""
        self.__features = CharacterFeatures(self, features)

    def __initialize_notes(self, notes: str):
        """Initialize the player's notes"""
        self.__notes = Notes(self, notes)

    def __initialize_derived_attributes(self):
        """Calculate and initialize derived attributes."""
        self.__prof_bonus = ProfBonus(self)
        self.__armor_class = ArmorClass(self)
        self.__initiative = Initiative(self)
        self.__passive_perception = PassivePerception(self)
        self.__speed = Speed(self)

    @property
    def biography(self):
        """Get character biography (name, background, alignment, player name)"""
        return self.__biography

    @property
    def current_game_class(self):
        """Get current game class"""
        return self.__current_game_class

    @property
    def level(self) -> Level:
        """Get the level of the character."""
        return self.__level

    @property
    def prof_bonus(self) -> ProfBonus:
        """Get the proficiency bonus of the character."""
        return self.__prof_bonus

    @property
    def abilities(self) -> Dict[AbilityType, Ability]:
        """Get the abilities of the character."""
        return self.__abilities

    @property
    def saving_throws(self) -> Dict[AbilityType, SavingThrow]:
        """Get the saving throws of the character."""
        return self.__saving_throws

    @property
    def skills(self) -> Dict[SkillType, Skill]:
        """Get the skills of the character."""
        return self.__skills

    @property
    def equipped_armor(self) -> EquippedArmor:
        """Get the equipped armor of the character."""
        return self.__equipped_armor

    @property
    def armor_class(self) -> ArmorClass:
        """Get the armor class of the character."""
        return self.__armor_class

    @property
    def shield(self) -> Shield:
        """Get the shield of the character."""
        return self.__shield

    @property
    def initiative(self) -> Initiative:
        """Get the initiative bonus of the character."""
        return self.__initiative

    @property
    def death_saves(self) -> DeathSaves:
        """Get the death saves of the character."""
        return self.__death_saves

    @property
    def hit_points(self) -> HitPoints:
        """Get the hit points of the character."""
        return self.__hit_points

    @property
    def hit_dices_pool(self) -> HitDicesPool:
        """Get the hit dices pool of the character."""
        return self.__hit_dices_pool

    @property
    def temporary_hit_points(self) -> TemporaryHitPoints:
        """Get the temporary hit points of the character."""
        return self.__temporary_hit_points

    @property
    def race(self) -> Race:
        """Get the race of the character."""
        return self.__race

    @property
    def passive_perception(self) -> PassivePerception:
        """Get the passive perception of the character."""
        return self.__passive_perception

    @property
    def attacks_list(self) -> AttacksList:
        """Get the attacks list of the character."""
        return self.__attacks_list

    @property
    def features(self) -> CharacterFeatures:
        """Get the features of the character."""
        return self.__features

    @property
    def speed(self) -> Speed:
        """Get the movement speed of the character."""
        return self.__speed

    @property
    def experience_points(self) -> ExperiencePoints:
        """Get the experience points of the character."""
        return self.__experience_points

    @property
    def inventory(self) -> Inventory:
        """Get the inventory of the character."""
        return self.__inventory

    @property
    def notes(self) -> Notes:
        """Get the notes of the character."""
        return self.__notes
