from abc import ABC, abstractmethod

from abstract_character import AbstractCharacter
from character_stats import AbilityType
from constants.constants import NO_ARMOR_AC
from armor import Armor, calculate_dexterity_bonus
from shield.shield import Shield


class ArmorClassCalculationStrategy(ABC):
    """Abstract base class for armor class calculation strategies."""

    @abstractmethod
    def calculate(self, character: AbstractCharacter) -> int:
        """Calculate and return the armor class value."""


class DefaultArmorClassCalculationStrategy(ArmorClassCalculationStrategy):
    """Default armor class calculation strategy."""

    def calculate(self, character: AbstractCharacter) -> int:
        """Calculate and return the armor class value."""
        shield = character.shield
        armor = character.equipped_armor.armor
        dexterity_modifier = character.abilities[AbilityType.DEXTERITY].modifier
        if armor is None:
            armor_class_value = NO_ARMOR_AC + dexterity_modifier
        else:
            armor_class_value = (armor.basic_armor_class + calculate_dexterity_bonus(armor, dexterity_modifier)
                                 + shield.bonus_to_ac)
        return armor_class_value


class BarbarianArmorClassCalculationStrategy(ArmorClassCalculationStrategy):
    """Barbarian-specific armor class calculation strategy."""

    def calculate(self, character: AbstractCharacter) -> int:
        """Calculate and return the armor class value."""
        shield = character.shield
        abilities = character.abilities
        armor_class_value = NO_ARMOR_AC + abilities[AbilityType.CONSTITUTION].modifier + abilities[
            AbilityType.DEXTERITY].modifier + shield.bonus_to_ac
        return armor_class_value


class MonkArmorClassCalculationStrategy(ArmorClassCalculationStrategy):
    """Monk-specific armor class calculation strategy."""

    def calculate(self, character: AbstractCharacter) -> int:
        """Calculate and return the armor class value."""
        abilities = character.abilities
        armor_class_value = NO_ARMOR_AC + abilities[AbilityType.DEXTERITY].modifier + abilities[
            AbilityType.WISDOM].modifier
        return armor_class_value
