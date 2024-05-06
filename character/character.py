from typing import Dict, List

from abstract_character import AbstractCharacter
from shield import Shield
from character_stats import Ability, Level, ProfBonus, AbilityType, Speed, Biography
from saving_throws import SavingThrow
from skills import Skill
from skills_types import SkillType
from initiative import Initiative
from armor import Armor, EquippedArmor, basic_armor_collection
from armor_class import ArmorClass
from constants import MIN_LEVEL
from utils import SKILLS_TO_ABILITIES, show_all_stats
from health import DeathSaves, HitPoints, HitDicesPool, TemporaryHitPoints
from game_classes import CurrentGameClass, basic_game_classes_collection, GameClassType
from race import basic_races_collection
from character_stats import PassivePerception
from attacks import AttacksList
from character_features import CharacterFeatures


class Character(AbstractCharacter):
    """Represents a character."""

    @property
    def current_game_class(self) -> CurrentGameClass:
        """Get the game class."""
        return self.__current_game_class

    def __init__(self, character_name: str, game_class_type: GameClassType, level: int, background: str,
                 player_name: str, race_name: str, alignment: str, experience_points: int,
                 abilities_scores: Dict[AbilityType, int], saving_throws_proficiencies: List[AbilityType],
                 skills_proficiencies: List[SkillType],
                 equipped_armor: Armor, current_hit_points: int, max_hit_points: int, temporary_hit_points: int,
                 hit_dice: str, hit_dices_left, successful_death_saves: int, failed_death_saves: int, attacks_list: List[List[str, str, bool, str]],
                 inventory: str, features: str):
        """Initialize a Character instance."""
        super().__init__()
        self.__current_game_class = CurrentGameClass(self, basic_game_classes_collection.
                                                     get_game_class_by_type(game_class_type))
        self.__level = Level(self, level)
        self.__prof_bonus = ProfBonus(self)
        self.__abilities = {ability: Ability(self, ability, abilities_scores[ability]) for ability in AbilityType}
        self.__saving_throws = {ability: SavingThrow(self, ability) for ability in AbilityType}
        self.__skills = {skill: Skill(skill, self.abilities[SKILLS_TO_ABILITIES[skill]].modifier) for skill in
                         SKILLS_TO_ABILITIES}
        self.__race = basic_races_collection.get_race(race_name)
        self.__shield = Shield(self)
        self.__equipped_armor = EquippedArmor(self, equipped_armor)
        self.__armor_class = ArmorClass(self)
        self.__initiative = Initiative(self)
        self.__death_saves = DeathSaves(self)
        self.__hit_points = HitPoints(self)
        self.__hit_dices_pool = HitDicesPool(self)
        self.__temporary_hit_points = TemporaryHitPoints(self)
        self.__passive_perception = PassivePerception(self)
        self.__attacks_list = AttacksList(self)
        self.__features = CharacterFeatures(self)
        self.__speed = Speed(self)
        self.__biography = Biography(self, character_name)

    @property
    def level(self) -> Level:
        """Get the level."""
        return self.__level

    @property
    def prof_bonus(self) -> ProfBonus:
        """Get the proficiency bonus."""
        return self.__prof_bonus

    @property
    def abilities(self) -> Dict[AbilityType, Ability]:
        """Get the abilities."""
        return self.__abilities

    @property
    def saving_throws(self) -> Dict[AbilityType, SavingThrow]:
        """Get the saving throws."""
        return self.__saving_throws

    @property
    def skills(self) -> Dict[SkillType, Skill]:
        """Get the skills."""
        return self.__skills

    @property
    def equipped_armor(self) -> EquippedArmor:
        """Get the equipped armor."""
        return self.__equipped_armor

    @property
    def armor_class(self) -> ArmorClass:
        """Get the armor class."""
        return self.__armor_class

    @property
    def shield(self) -> Shield:
        """Get the shield object."""
        return self.__shield

    @property
    def initiative(self) -> Initiative:
        """Get the initiative bonus."""
        return self.__initiative

    @property
    def death_saves(self) -> DeathSaves:
        """Get the death saves."""
        return self.__death_saves

    @property
    def hit_points(self) -> HitPoints:
        """Get the hit points."""
        return self.__hit_points

    @property
    def hit_dices_pool(self) -> HitDicesPool:
        """Get the hit dices pool."""
        return self.__hit_dices_pool

    @property
    def temporary_hit_points(self) -> TemporaryHitPoints:
        """Get the temporary hit points."""
        return self.__temporary_hit_points

    @property
    def race(self):
        """Get race"""
        return self.__race

    @property
    def passive_perception(self) -> PassivePerception:
        """Get passive perception."""
        return self.__passive_perception

    @property
    def attacks_list(self):
        """Get attacks list"""
        return self.__attacks_list

    @property
    def features(self):
        """Get character's features."""
        return self.__features

    def speed(self):
        """Get the movement speed."""
        return self.__speed

