# Import necessary modules
from .game_classes import GameClass
from .game_classes_collection import GameClassCollection
from .game_classes_types import GameClassType
from skills_types import SkillType
from character_stats import AbilityType

# Create an instance of GameClassCollection
basic_game_classes_collection = GameClassCollection()

# Define and add each class to the collection

# Barbarian
barbarian = GameClass(
    GameClassType.BARBARIAN,
    "Barbarian",
    12,
    [AbilityType.STRENGTH, AbilityType.CONSTITUTION],
    """Armor: Light armor, medium armor, shields
Weapons: Simple weapons, martial weapons
Tools: None""",
    2,
    [
        SkillType.ANIMAL_HANDLING, SkillType.ATHLETICS,
        SkillType.INTIMIDATION, SkillType.NATURE,
        SkillType.PERCEPTION, SkillType.SURVIVAL
    ]
)
basic_game_classes_collection.add_game_class(barbarian)

# Bard
bard = GameClass(
    GameClassType.BARD,
    "Bard",
    8,
    [AbilityType.DEXTERITY, AbilityType.CHARISMA],
    """Armor: Light armor
Weapons: Simple weapons, hand crossbows, longswords, rapiers, shortswords
Tools: Three musical instruments of your choice""",
    3,
    [
        SkillType.ACROBATICS, SkillType.ANIMAL_HANDLING,
        SkillType.ARCANA, SkillType.ATHLETICS,
        SkillType.DECEPTION, SkillType.HISTORY,
        SkillType.INSIGHT, SkillType.INTIMIDATION,
        SkillType.INVESTIGATION, SkillType.MEDICINE,
        SkillType.NATURE, SkillType.PERCEPTION,
        SkillType.PERFORMANCE, SkillType.PERSUASION,
        SkillType.RELIGION, SkillType.SLEIGHT_OF_HAND,
        SkillType.STEALTH, SkillType.SURVIVAL
    ]
)
basic_game_classes_collection.add_game_class(bard)

# Cleric
cleric = GameClass(
    GameClassType.CLERIC,
    "Cleric",
    8,
    [AbilityType.WISDOM, AbilityType.CHARISMA],
    """Armor: Light armor, medium armor, shields
Weapons: Simple weapons
Tools: None""",
    2,
    [
        SkillType.HISTORY, SkillType.INSIGHT,
        SkillType.MEDICINE, SkillType.PERSUASION,
        SkillType.RELIGION
    ]
)
basic_game_classes_collection.add_game_class(cleric)

# Druid
druid = GameClass(
    GameClassType.DRUID,
    "Druid",
    8,
    [AbilityType.INTELLIGENCE, AbilityType.WISDOM],
    """Armor: Light armor, medium armor, shields (druids will not wear armor or use shields made of metal)
Weapons: Clubs, daggers, darts, javelins, maces, quarterstaffs, scimitars, sickles, slings, spears
Tools: Herbalism kit""",
    2,
    [
        SkillType.ARCANA, SkillType.ANIMAL_HANDLING,
        SkillType.INSIGHT, SkillType.MEDICINE,
        SkillType.NATURE, SkillType.PERCEPTION,
        SkillType.RELIGION, SkillType.SURVIVAL
    ]
)
basic_game_classes_collection.add_game_class(druid)

# Fighter
fighter = GameClass(
    GameClassType.FIGHTER,
    "Fighter",
    10,
    [AbilityType.STRENGTH, AbilityType.CONSTITUTION],
    """Armor: All armor, shields
Weapons: Simple weapons, martial weapons""",
    2,
    [
        SkillType.ACROBATICS, SkillType.ANIMAL_HANDLING,
        SkillType.ATHLETICS, SkillType.HISTORY,
        SkillType.INSIGHT, SkillType.INTIMIDATION,
        SkillType.PERCEPTION, SkillType.SURVIVAL
    ]
)
basic_game_classes_collection.add_game_class(fighter)

# Monk
monk = GameClass(
    GameClassType.MONK,
    "Monk",
    8,
    [AbilityType.DEXTERITY, AbilityType.WISDOM],
    """Armor: None
Weapons: Simple weapons, shortswords""",
    2,
    [
        SkillType.ACROBATICS, SkillType.ATHLETICS,
        SkillType.HISTORY, SkillType.INSIGHT,
        SkillType.RELIGION, SkillType.STEALTH
    ]
)
basic_game_classes_collection.add_game_class(monk)

# Paladin
paladin = GameClass(
    GameClassType.PALADIN,
    "Paladin",
    10,
    [AbilityType.WISDOM, AbilityType.CHARISMA],
    """Armor: All armor, shields
Weapons: Simple weapons, martial weapons""",
    2,
    [
        SkillType.ATHLETICS, SkillType.INSIGHT,
        SkillType.INTIMIDATION, SkillType.MEDICINE,
        SkillType.PERSUASION, SkillType.RELIGION
    ]
)
basic_game_classes_collection.add_game_class(paladin)

# Ranger
ranger = GameClass(
    GameClassType.RANGER,
    "Ranger",
    10,
    [AbilityType.DEXTERITY, AbilityType.WISDOM],
    """Armor: Light armor, medium armor, shields
Weapons: Simple weapons, martial weapons""",
    3,
    [
        SkillType.ANIMAL_HANDLING, SkillType.ATHLETICS,
        SkillType.INSIGHT, SkillType.INVESTIGATION,
        SkillType.NATURE, SkillType.PERCEPTION,
        SkillType.STEALTH, SkillType.SURVIVAL
    ]
)
basic_game_classes_collection.add_game_class(ranger)

# Rogue
rogue = GameClass(
    GameClassType.ROGUE,
    "Rogue",
    8,
    [AbilityType.DEXTERITY, AbilityType.INTELLIGENCE],
    """Armor: Light armor
Weapons: Simple weapons, hand crossbows, longswords, rapiers, shortswords""",
    4,
    [
        SkillType.ACROBATICS, SkillType.ATHLETICS,
        SkillType.DECEPTION, SkillType.INSIGHT,
        SkillType.INTIMIDATION, SkillType.INVESTIGATION,
        SkillType.PERCEPTION, SkillType.PERFORMANCE,
        SkillType.PERSUASION, SkillType.SLEIGHT_OF_HAND,
        SkillType.STEALTH
    ]
)
basic_game_classes_collection.add_game_class(rogue)

# Sorcerer
sorcerer = GameClass(
    GameClassType.SORCERER,
    "Sorcerer",
    6,
    [AbilityType.CONSTITUTION, AbilityType.CHARISMA],
    """Armor: None
Weapons: Daggers, darts, slings, quarterstaffs, light crossbows""",
    2,
    [
        SkillType.ARCANA, SkillType.DECEPTION,
        SkillType.INSIGHT, SkillType.INTIMIDATION,
        SkillType.PERSUASION, SkillType.RELIGION
    ]
)
basic_game_classes_collection.add_game_class(sorcerer)

# Warlock
warlock = GameClass(
    GameClassType.WARLOCK,
    "Warlock",
    8,
    [AbilityType.WISDOM, AbilityType.CHARISMA],
    """Armor: Light armor
Weapons: Simple weapons""",
    2,
    [
        SkillType.ARCANA, SkillType.DECEPTION,
        SkillType.HISTORY, SkillType.INTIMIDATION,
        SkillType.INVESTIGATION, SkillType.NATURE,
        SkillType.RELIGION
    ]
)
basic_game_classes_collection.add_game_class(warlock)

# Wizard
wizard = GameClass(
    GameClassType.WIZARD,
    "Wizard",
    6,
    [AbilityType.INTELLIGENCE, AbilityType.WISDOM],
    """Armor: None
Weapons: Daggers, darts, slings, quarterstaffs, light crossbows""",
    2,
    [
        SkillType.ARCANA, SkillType.HISTORY,
        SkillType.INSIGHT, SkillType.INVESTIGATION,
        SkillType.MEDICINE, SkillType.RELIGION
    ]
)
basic_game_classes_collection.add_game_class(wizard)

