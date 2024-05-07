from typing import Dict, List
from abstract_character import AbstractCharacter
from shield import Shield
from character_stats import (
    Ability, Level, ProfBonus, AbilityType, Speed, Biography, ExperiencePoints, PassivePerception
)
from skills import Skill
from skills_types import SkillType
from initiative import Initiative
from armor import Armor, EquippedArmor
from armor_class import ArmorClass
from utils import SKILLS_TO_ABILITIES
from health import DeathSaves, HitPoints, HitDicesPool, TemporaryHitPoints
from game_classes import CurrentGameClass, basic_game_classes_collection, GameClassType
from race import basic_races_collection
from attacks import AttacksList, Attack
from character_features import CharacterFeatures
from inventory import Inventory
from saving_throws import SavingThrow


class Character(AbstractCharacter):
    """Represents a character in the game."""

    def __init__(self, character_name: str, game_class_type: GameClassType, level: int, background: str,
                 player_name: str, race: str, alignment: str, experience_points: int,
                 abilities_scores: Dict[AbilityType, int], saving_throws_proficiencies: List[AbilityType],
                 skills_proficiencies: List[SkillType], shield: bool,
                 equipped_armor: Armor, current_hit_points: int, max_hit_points: int, temporary_hit_points: int,
                 hit_dices_left: int, successful_death_saves: int, failed_death_saves: int,
                 attacks_list: List[Attack], inventory: str, features: str):
        """Initialize a Character instance."""
        super().__init__()
        self.__biography = Biography(self, character_name, background, alignment, player_name)
        self.__current_game_class = CurrentGameClass(self, basic_game_classes_collection.get_game_class_by_type(
            game_class_type))
        self.__level = Level(self, level)
        self.__race = basic_races_collection.get_race(race)
        self.__experience_points = ExperiencePoints(self, experience_points)
        self.__abilities = {ability: Ability(self, ability, abilities_scores[ability]) for ability in AbilityType}
        self.__saving_throws = {ability: SavingThrow(self, ability, (ability in saving_throws_proficiencies)) for
                                ability in AbilityType}
        self.__skills = {skill: Skill(skill, self.abilities[SKILLS_TO_ABILITIES[skill]].modifier,
                                      (SKILLS_TO_ABILITIES[skill] in skills_proficiencies)) for skill in
                         SKILLS_TO_ABILITIES}
        self.__shield = Shield(self, shield)
        self.__equipped_armor = EquippedArmor(self, equipped_armor)
        self.__hit_points = HitPoints(self, current_hit_points, max_hit_points)
        self.__temporary_hit_points = TemporaryHitPoints(self, temporary_hit_points)
        self.__hit_dices_pool = HitDicesPool(self, hit_dices_left)
        self.__death_saves = DeathSaves(self, successful_death_saves, failed_death_saves)
        self.__attacks_list = AttacksList(self, attacks_list)
        self.__inventory = Inventory(self, inventory)

        self.__prof_bonus = ProfBonus(self)
        self.__armor_class = ArmorClass(self)
        self.__initiative = Initiative(self)
        self.__passive_perception = PassivePerception(self)
        self.__features = CharacterFeatures(self)
        self.__speed = Speed(self)

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

