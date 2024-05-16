# from character_singleton import CharacterSingleton
# from character_stats import AbilityType
# from game_classes import GameClassType
# from skills_types import SkillType
# from utils import get_default_downloads_folder
# from show_character_info import show_character_info
#
# character_singleton = CharacterSingleton()
#
# character_data = (
#     "Aragorn",
#     GameClassType.FIGHTER.value,
#     5,
#     "Noble",
#     "Human",
#     "Neutral Good",
#     5000,
#     {
#         "STR": 18,
#         "DEX": 16,
#         "CON": 14,
#         "INT": 12,
#         "WIS": 10,
#         "CHA": 8
#     },
#     {ability.value: (ability.value in ("STR", "DEX")) for ability in AbilityType},
#     {skill.value: skill in (SkillType.ACROBATICS, SkillType.SURVIVAL) for skill in SkillType},
#     True,
#     "Plate",
#     45,
#     60,
#     0,
#     2,
#     2,
#     1,
#     [("Longsword", "STR", True, "1d10", 5, 2)],
#     "Longsword, Backpack, Rations",
#     "Favored Enemy: Orcs, Second Wind",
#     ""
# )
#
# character_singleton.create_character(character_data)
# character = character_singleton.character
# print("Prof bonus",character.prof_bonus.value)
