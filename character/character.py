from typing import Dict

from abstract_character import AbstractCharacter
from health.hit_dices_pool import HitDicesPool
from shield import Shield
from character_stats import Ability, Level, ProfBonus, AbilityType
from saving_throws import SavingThrow
from skills import Skill
from skills_types import SkillType
from initiative import Initiative
from armor import Armor, EquippedArmor, basic_armor_collection
from armor_class import ArmorClass
from constants import MIN_LEVEL
from utils import SKILLS_TO_ABILITIES
from health import DeathSaves, HitPoints, HitDicesPool
from game_classes import CurrentGameClass, basic_game_classes_collection, GameClassType


class Character(AbstractCharacter):
    """Represents a __character."""

    def __init__(self, abilities_scores: Dict[AbilityType, int], game_class_type: GameClassType, level: int = MIN_LEVEL,
                 equipped_armor: Armor = None):
        """Initialize a Character instance."""
        super().__init__()
        self.__current_game_class = CurrentGameClass(self,
                                                     basic_game_classes_collection.get_game_class_by_type(game_class_type))
        self.__level = Level(self, level)
        self.__prof_bonus = ProfBonus(self)
        self.__abilities = {ability: Ability(ability, abilities_scores[ability]) for ability in AbilityType}
        self.__saving_throws = {ability: SavingThrow(self, ability) for ability in AbilityType}
        self.__skills = {skill: Skill(skill, self.abilities[SKILLS_TO_ABILITIES[skill]].modifier) for skill in
                         SKILLS_TO_ABILITIES}
        self.__shield = Shield(self)
        self.__equipped_armor = EquippedArmor(self, equipped_armor)
        self.__armor_class = ArmorClass(self)
        self.__initiative = Initiative(self)
        self.__death_saves = DeathSaves(self)
        self.__hit_points = HitPoints(self)
        self.__hit_dices_pool = HitDicesPool(self)

    @property
    def current_game_class(self) -> CurrentGameClass:
        """Get the game class."""
        return self.__current_game_class

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


# Execution
swanchick = Character({
    AbilityType.STRENGTH: 16,
    AbilityType.DEXTERITY: 12,
    AbilityType.CONSTITUTION: 9,
    AbilityType.INTELLIGENCE: 11,
    AbilityType.WISDOM: 20,
    AbilityType.CHARISMA: 16
}, GameClassType.BARBARIAN, 1, basic_armor_collection.get_armor_by_name("Hide"))

print("Your STR mod:", swanchick.abilities[AbilityType.STRENGTH].modifier)
print(f"Your proficiency bonus at level {swanchick.level.value} is:", swanchick.prof_bonus.value)
swanchick.saving_throws[AbilityType.STRENGTH].proficiency = True
print("Your STR saving throw is:", swanchick.saving_throws[AbilityType.STRENGTH].value)
print("Your Armor Class is:", swanchick.armor_class.value)
print(basic_game_classes_collection.get_all_game_classes())

gey_338 = Character({
    AbilityType.STRENGTH: 20,
    AbilityType.DEXTERITY: 20,
    AbilityType.CONSTITUTION: 20,
    AbilityType.INTELLIGENCE: 19,
    AbilityType.WISDOM: 19,
    AbilityType.CHARISMA: 18
}, GameClassType.BARBARIAN, 15, basic_armor_collection.get_armor_by_name("Chain mail"))

print(gey_338.current_game_class.value.proficiencies)
gey_338.skills[SkillType.ANIMAL_HANDLING]