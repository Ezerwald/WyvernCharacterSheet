from typing import Dict

from abstract_character import AbstractCharacter
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
from health import DeathSaves
from game_classes import CurrentGameClass


class Character(AbstractCharacter):
    """Represents a __character."""
    __abilities: Dict[AbilityType, Ability]
    __saving_throws: Dict[AbilityType, SavingThrow]
    __skills: Dict[SkillType, Skill]

    def __init__(self, abilities_scores: Dict[AbilityType, int], game_class: GameClassType, level: int = MIN_LEVEL,
                 equipped_armor: Armor = None):
        """Initialize a Character instance."""
        super().__init__()
        self.__game_class = CurrentGameClass(self, )
        self.__level = Level(self, level)
        self.__prof_bonus = ProfBonus(self)
        self.__abilities = {ability: Ability(ability, abilities_scores[ability])
                            for ability in AbilityType}
        self.__saving_throws = {ability: SavingThrow(self, ability)
                                for ability in AbilityType}
        self.__skills = {skill: Skill(skill, self.abilities[SKILLS_TO_ABILITIES[skill]].modifier)
                         for skill in SKILLS_TO_ABILITIES}
        self.__shield = Shield(self)
        self.__equipped_armor = EquippedArmor(self, equipped_armor)
        self.__armor_class = ArmorClass(self)
        self.__initiative = Initiative(self)
        self.__death_saves = DeathSaves(self)

    @property
    def game_class(self) -> CurrentGameClass:
        """Get the game class."""
        return self.__game_class

    @property
    def level(self) -> Level:
        """Get the __level."""
        return self.__level

    @property
    def prof_bonus(self) -> ProfBonus:
        """Get the proficiency bonus."""
        return self.__prof_bonus

    @property
    def abilities(self) -> Dict[AbilityType, Ability]:
        """Get the __abilities."""
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
        """Get the __shield object."""
        return self.__shield

    @property
    def initiative(self) -> Initiative:
        """Get the initiative bonus."""
        return self.__initiative

    @property
    def death_saves(self) -> DeathSaves:
        return self.__death_saves


# Execution
swanchick = Character({
    AbilityType.STRENGTH: 16,
    AbilityType.DEXTERITY: 12,
    AbilityType.CONSTITUTION: 9,
    AbilityType.INTELLIGENCE: 11,
    AbilityType.WISDOM: 20,
    AbilityType.CHARISMA: 16
}, CurrentGameClass.BARBARIAN.value, 1, basic_armor_collection.get_armor_by_name("Hide"))

print("Your STR mod: ", swanchick.abilities[AbilityType.STRENGTH].modifier)
print(f"Your proficiency bonus on level {swanchick.level.value} is: ", swanchick.prof_bonus.value)
swanchick.saving_throws[AbilityType.STRENGTH].proficiency = True
print("Your STR saving throw is:", swanchick.saving_throws[AbilityType.STRENGTH].value)
print("Your Armor Class is:", swanchick.armor_class.value)
