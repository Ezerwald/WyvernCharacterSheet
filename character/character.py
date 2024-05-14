from typing import Dict, List, Tuple
from abstract_character import AbstractCharacter
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
from game_classes import CurrentGameClass, basic_game_classes_collection, GameClassType
from race import basic_races_collection
from attacks import AttacksList, Attack
from character_features import CharacterFeatures
from inventory import Inventory
from saving_throws import SavingThrow


class Character(AbstractCharacter):
    """Represents a character in the game."""

    def __init__(self, character_name: str,
                 game_class_type: GameClassType,
                 level: int,
                 background: str,
                 race: str,
                 alignment: str,
                 experience_points: int,
                 abilities_scores: Dict[AbilityType, int],
                 saving_throws_proficiencies: List[AbilityType],
                 skills_proficiencies: List[SkillType],
                 shield: bool,
                 equipped_armor: str,
                 current_hit_points: int,
                 max_hit_points: int,
                 temporary_hit_points: int,
                 hit_dices_left: int,
                 successful_death_saves: int,
                 failed_death_saves: int,
                 attacks_data_list: List[Tuple[str, AbilityType, bool, str, int, int]],
                 inventory: str,
                 features: str):
        """Initialize a Character instance."""
        super().__init__()
        self.__initialize_biography(character_name, background, alignment)
        self.__initialize_game_class(game_class_type)
        self.__initialize_level(level)
        self.__initialize_race(race)
        self.__initialize_experience(experience_points)
        self.__initialize_abilities(abilities_scores)
        self.__initialize_saving_throws(saving_throws_proficiencies)
        self.__initialize_skills(skills_proficiencies)
        self.__initialize_shield(shield)
        self.__initialize_equipped_armor(equipped_armor)
        self.__initialize_hit_points(current_hit_points, max_hit_points)
        self.__initialize_temporary_hit_points(temporary_hit_points)
        self.__initialize_hit_dices(hit_dices_left)
        self.__initialize_death_saves(successful_death_saves, failed_death_saves)
        self.__initialize_attacks(attacks_data_list)
        self.__initialize_inventory(inventory)
        self.__initialize_features(features)

        self.__initialize_derived_attributes()

    """Initializers for character attributes"""

    def __initialize_biography(self, character_name: str, background: str, alignment: str):
        """Initialize the character's biography."""
        self.__biography = Biography(self, character_name, background, alignment)

    def __initialize_game_class(self, game_class_type: GameClassType):
        """Initialize the character's game class."""
        self.__current_game_class = CurrentGameClass(self, basic_game_classes_collection.get_game_class_by_type(
            game_class_type))

    def __initialize_level(self, level: int):
        """Initialize the character's level."""
        self.__level = Level(self, level)

    def __initialize_race(self, race: str):
        """Initialize the character's race."""
        self.__race = basic_races_collection.get_race(race)

    def __initialize_experience(self, experience_points: int):
        """Initialize the character's experience points."""
        self.__experience_points = ExperiencePoints(self, experience_points)

    def __initialize_abilities(self, abilities_scores: Dict[AbilityType, int]):
        """Initialize the character's abilities."""
        self.__abilities = {ability: Ability(self, ability, abilities_scores[ability]) for ability in AbilityType}

    def __initialize_saving_throws(self, saving_throws_proficiencies: List[AbilityType]):
        """Initialize the character's saving throws."""
        self.__saving_throws = {ability: SavingThrow(self, ability, (ability in saving_throws_proficiencies)) for
                                ability in AbilityType}

    def __initialize_skills(self, skills_proficiencies: List[SkillType]):
        """Initialize the character's skills."""
        self.__skills = {skill: Skill(self, skill, (skill in skills_proficiencies))
                         for skill in SkillType}

    def __initialize_shield(self, shield: bool):
        """Initialize the character's shield."""
        self.__shield = Shield(self, shield)

    def __initialize_equipped_armor(self, equipped_armor: str):
        """Initialize the character's equipped armor."""
        self.__equipped_armor = EquippedArmor(self,  basic_armor_collection.get_armor_by_name(equipped_armor))

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

    def __initialize_attacks(self, attacks_data_list: List[Tuple[str, AbilityType, bool, str, int, int]]):
        """Initialize the character's attacks list."""
        attacks_list = [Attack(self, *attack_data) for attack_data in attacks_data_list]
        self.__attacks_list = AttacksList(self, attacks_list)

    def __initialize_inventory(self, inventory: str):
        """Initialize the character's inventory."""
        self.__inventory = Inventory(self, inventory)

    def __initialize_features(self, features: str):
        """Initialize the character's features"""
        self.__features = CharacterFeatures(self, features)

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
    def race(self):
        """Get the race of the character."""
        return self.__race

    @property
    def passive_perception(self) -> PassivePerception:
        """Get the passive perception of the character."""
        return self.__passive_perception

    @property
    def attacks_list(self):
        """Get the attacks list of the character."""
        return self.__attacks_list

    @property
    def features(self):
        """Get the features of the character."""
        return self.__features

    @property
    def speed(self):
        """Get the movement speed of the character."""
        return self.__speed

    @property
    def experience_points(self):
        """Get the experience points of the character."""
        return self.__experience_points

    @property
    def inventory(self):
        """Get the inventory of the character."""
        return self.__inventory
