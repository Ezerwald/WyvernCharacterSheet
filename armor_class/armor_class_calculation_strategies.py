from abc import ABC, abstractmethod
from character_stats import AbilityType
from constants.constants import NO_ARMOR_AC
from armor import Armor, calculate_dexterity_bonus
from shield.shield import Shield


class ArmorClassCalculationStrategy(ABC):
    """Abstract base class for armor class calculation strategies."""

    @abstractmethod
    def calculate(self, shield: Shield, armor: Armor, abilities: dict) -> int:
        """Calculate and return the armor class value."""


class DefaultArmorClassCalculationStrategy(ArmorClassCalculationStrategy):
    """Default armor class calculation strategy."""

    def calculate(self, shield: Shield, armor: Armor, abilities: dict) -> int:
        """Calculate and return the armor class value."""
        dexterity_modifier = abilities[AbilityType.DEXTERITY].modifier
        if armor is None:
            armor_class_value = NO_ARMOR_AC + dexterity_modifier
        else:
            armor_class_value = (armor.basic_armor_class + calculate_dexterity_bonus(armor, dexterity_modifier)
                                 + shield.bonus_to_ac)
        return armor_class_value


class BarbarianArmorClassCalculationStrategy(ArmorClassCalculationStrategy):
    """Barbarian-specific armor class calculation strategy."""

    def calculate(self, shield: Shield, armor: Armor, abilities: dict) -> int:
        """Calculate and return the armor class value."""
        armor_class_value = NO_ARMOR_AC + abilities[AbilityType.CONSTITUTION.value].modifier + abilities[
            AbilityType.DEXTERITY.value].modifier + shield.bonus_to_ac
        return armor_class_value


class MonkArmorClassCalculationStrategy(ArmorClassCalculationStrategy):
    """Monk-specific armor class calculation strategy."""

    def calculate(self, shield: Shield, armor: Armor, abilities: dict) -> int:
        """Calculate and return the armor class value."""
        armor_class_value = NO_ARMOR_AC + abilities[AbilityType.DEXTERITY.value].modifier + abilities[
            AbilityType.WISDOM.value].modifier
        return armor_class_value
