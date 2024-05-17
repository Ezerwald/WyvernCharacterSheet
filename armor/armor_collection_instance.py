from .armors import Armor
from .armor_collection import ArmorCollection
from .armor_types import ArmorType
from constants.constants import MAX_MODIFIER_VALUE

basic_armor_collection = ArmorCollection()

# No Armor
basic_armor_collection.add_armor(Armor("None", ArmorType.LIGHT, 8, MAX_MODIFIER_VALUE, False))

# Light Armor
basic_armor_collection.add_armor(Armor("Padded", ArmorType.LIGHT, 11, MAX_MODIFIER_VALUE, True))
basic_armor_collection.add_armor(Armor("Leather", ArmorType.LIGHT, 11, MAX_MODIFIER_VALUE, False))
basic_armor_collection.add_armor(Armor("Studded leather", ArmorType.LIGHT, 12, MAX_MODIFIER_VALUE, False))

# Medium Armor
basic_armor_collection.add_armor(Armor("Hide", ArmorType.MEDIUM, 12, 2, False))
basic_armor_collection.add_armor(Armor("Chain shirt", ArmorType.MEDIUM, 13, 2, False))
basic_armor_collection.add_armor(Armor("Scale mail", ArmorType.MEDIUM, 14, 2, True))
basic_armor_collection.add_armor(Armor("Breastplate", ArmorType.MEDIUM, 14, 2, False))
basic_armor_collection.add_armor(Armor("Half plate", ArmorType.MEDIUM, 15, 2, True))

# Heavy Armor
basic_armor_collection.add_armor(Armor("Ring mail", ArmorType.HEAVY, 14, 0, True))
basic_armor_collection.add_armor(Armor("Chain mail", ArmorType.HEAVY, 16, 0, True))
basic_armor_collection.add_armor(Armor("Splint", ArmorType.HEAVY, 17, 0, True))
basic_armor_collection.add_armor(Armor("Plate", ArmorType.HEAVY, 18, 0, True))
