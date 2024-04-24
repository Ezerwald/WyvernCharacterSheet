from .armor_types import ArmorType
from .armors import Armor


def calculate_dexterity_bonus(armor: Armor, dexterity_modifier: int) -> int:
    """Calculate the dexterity bonus to armor class."""
    if armor.armor_type == ArmorType.HEAVY:
        return 0
    return min(dexterity_modifier, armor.max_dexterity_bonus)
