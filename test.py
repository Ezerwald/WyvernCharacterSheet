from attacks import Attack
from character import Character
from character import CharacterSingleton
from character_stats import AbilityType
from game_classes import GameClassType
from skills_types import SkillType

character_singleton = CharacterSingleton()

character_data = (
    "Aragorn",
    GameClassType.FIGHTER,
    5,
    "Noble",
    "Human",
    "Neutral Good",
    5000,
    {
        AbilityType.STRENGTH: 18,
        AbilityType.DEXTERITY: 16,
        AbilityType.CONSTITUTION: 14,
        AbilityType.INTELLIGENCE: 12,
        AbilityType.WISDOM: 10,
        AbilityType.CHARISMA: 8
    },
    [AbilityType.STRENGTH, AbilityType.DEXTERITY],
    [SkillType.ACROBATICS, SkillType.SURVIVAL],
    True,
    "Plate",
    45,
    60,
    0,
    2,
    2,
    1,
    [("Longsword", AbilityType.STRENGTH, True, "1d10", 5, 2)],
    "Longsword, Backpack, Rations",
    "Favored Enemy: Orcs, Second Wind"
)

character_singleton.create_character(character_data)
character = character_singleton.character
character_singleton.save_character()


