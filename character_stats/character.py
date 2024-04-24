from typing import Dict

from armor_class.shield import Shield
from character_stats import Ability, SavingThrow, Skill, Level, ProfBonus, GameClass, AbilityType
from armor import Armor, EquippedArmor, basic_armor_collection
from armor_class import ArmorClass
from constants import MIN_LEVEL, SKILLS_TO_ABILITIES


class Character:
    """Represents a __character."""

    def __init__(self, abilities_scores: Dict[int, int], game_class: int, level: int = MIN_LEVEL,
                 equipped_armor: Armor = None):
        """Initialize a Character instance."""
        self.__game_class = GameClass(game_class)
        self.__level = Level(self, level)
        self.__prof_bonus = ProfBonus(self)
        self.__abilities = {ability.value: Ability(ability.value, abilities_scores[ability.value])
                            for ability in AbilityType}
        self.__saving_throws = {ability.value: SavingThrow(self, ability.value)
                                for ability in AbilityType}
        self.__skills = {skill: Skill(skill, self.abilities[SKILLS_TO_ABILITIES[skill]].modifier)
                         for skill in SKILLS_TO_ABILITIES}
        self.__shield = Shield(self)
        self.__equipped_armor = EquippedArmor(self, equipped_armor)
        self.__armor_class = ArmorClass(self)

    @property
    def game_class(self) -> GameClass:
        """Get the game class."""
        return self.__game_class

    @property
    def level(self) -> Level:
        """Get the level."""
        return self.__level

    @property
    def prof_bonus(self) -> ProfBonus:
        """Get the proficiency bonus."""
        return self.__prof_bonus

    @property
    def abilities(self) -> Dict[int, Ability]:
        """Get the abilities."""
        return self.__abilities

    @property
    def saving_throws(self) -> Dict[int, SavingThrow]:
        """Get the saving throws."""
        return self.__saving_throws

    @property
    def skills(self) -> Dict[int, Skill]:
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
        """Get the shield."""
        return self.__shield


# Execution
swanchick = Character({
    AbilityType.STRENGTH.value: 16,
    AbilityType.DEXTERITY.value: 12,
    AbilityType.CONSTITUTION.value: 9,
    AbilityType.INTELLIGENCE.value: 11,
    AbilityType.WISDOM.value: 20,
    AbilityType.CHARISMA.value: 16
}, GameClass.BARBARIAN.value, 1, basic_armor_collection.get_armor_by_name("Hide"))

print("Your STR mod: ", swanchick.abilities[AbilityType.STRENGTH.value].modifier)
print(f"Your proficiency bonus on level {swanchick.level.value} is: ", swanchick.prof_bonus.value)
swanchick.saving_throws[AbilityType.STRENGTH.value].set_proficiency(True)
print("Your STR saving throw is:", swanchick.saving_throws[AbilityType.STRENGTH.value].value)
print("Your Armor Class is:", swanchick.armor_class.value)
print(basic_armor_collection.get_all_armors())
