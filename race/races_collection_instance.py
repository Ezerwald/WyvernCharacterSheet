from .races_collection import RaceCollection
from character_stats import AbilityType
from .races import Race

basic_races_collection = RaceCollection()

# Human
human_ability_bonuses = {
    AbilityType.STRENGTH: 1,
    AbilityType.DEXTERITY: 1,
    AbilityType.CONSTITUTION: 1,
    AbilityType.WISDOM: 1,
    AbilityType.INTELLIGENCE: 1,
    AbilityType.CHARISMA: 1
}
human_features = ("Languages: Common, one additional language\n"
                  "Ability Score Increase: Your ability scores each increase by 1.")
basic_races_collection.add_race(Race("Human", human_ability_bonuses, 30, human_features))

# Dwarf
dwarf_ability_bonuses = {AbilityType.CONSTITUTION: 2}
dwarf_features = ("Languages: Common, Dwarvish\n"
                  "Darkvision: 60 feet\n"
                  "Ability Score Increase: Constitution score increases by 2,")
dwarf_subraces = [
    ("Mountain Dwarf", {AbilityType.STRENGTH: 2},
     "Strength score increases by 2\nDwarven Armor Training: you have proficiency with light and medium armor"),
    ("Hill Dwarf", {AbilityType.WISDOM: 1},
     "Wisdom score increases by 1\nDwarven Toughness: Your hit point maximum increases by 1, and it increases "
     "by 1 every time you gain a level.")
]
basic_races_collection.add_race_with_subraces(dwarf_ability_bonuses, 25, dwarf_features, dwarf_subraces)
# Elf
elf_ability_bonuses = {AbilityType.DEXTERITY: 2}
elf_features = ("Languages: Common, Elvish\n"
                "Darkvision: 60 feet\n"
                "Ability Score Increase: Dexterity score increases by 2,")
elf_subraces = [
    ("High Elf", {AbilityType.INTELLIGENCE: 1},
     "Intelligence score increases by 1\nKeen Senses: Proficiency in the Perception skill.\n"
     "Fey Ancestry: Advantage on saving throws against being charmed, and magic can't put you to sleep.\n"
     "Trance: Meditate for 4 hours instead of sleeping."),
    ("Wood Elf", {AbilityType.WISDOM: 1},
     "Wisdom score increases by 1\nFleet of Foot: Base walking speed increases to 35 feet.\n"
     "Mask of the Wild: You can attempt to hide even when you are only lightly "
     "obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.", 35),
    ("Drow", {AbilityType.CHARISMA: 1},
     "Charisma score increases by 1\nSuperior Darkvision: 120 feet\n"
     "Sunlight Sensitivity: You have disadvantage on attack rolls and Wisdom (Perception) "
     "checks that rely on sight when you, the target of your attack, or whatever you are "
     "trying to perceive is in direct sunlight.\n"
     "Drow Magic: You know the dancing lights cantrip. When you reach 3rd level, you can "
     "cast the faerie fire spell once per day. When you reach 5th level, you can also cast "
     "the darkness spell once per day. Charisma is your spellcasting ability for these "
     "spells.")
]
basic_races_collection.add_race_with_subraces(elf_ability_bonuses, 30, elf_features, elf_subraces)

# Halfling
halfling_ability_bonuses = {AbilityType.DEXTERITY: 2}
halfling_features = ("Languages: Common, Halfling\n"
                     "Lucky: When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the "
                     "die and must use the new roll.\n"
                     "Ability Score Increase: Your Dexterity score increases by 2 and ")
halfling_subraces = [
    ("Lightfoot Halfling", {AbilityType.CHARISMA: 1},
     "Your Charisma score increases by 1\nNaturally Stealthy: You can attempt to hide even when you are obscured only "
     "by a creature that is at least one size larger than you."),
    ("Stout Halfling", {AbilityType.CONSTITUTION: 1},
     "Your Constitution score increases by 1\nStout Resilience: You have advantage on saving throws against poison, "
     "and you have resistance against poison damage.")
]
basic_races_collection.add_race_with_subraces(halfling_ability_bonuses, 25, halfling_features, halfling_subraces)

# Gnome
gnome_ability_bonuses = {AbilityType.INTELLIGENCE: 2}
gnome_features = ("Languages: Common, Gnomish\n"
                  "Darkvision: Accustomed to life underground, you have superior vision in dark and dim conditions. "
                  "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it "
                  "were dim light. You can’t discern color in darkness, only shades of gray.\n"
                  "Gnome Cunning: You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic."
                  "Ability Score Increase: Your Intelligence score increases by 2 and ")

gnome_subraces = [
    ("Forest Gnome", {AbilityType.DEXTERITY: 1},
     "Your Dexterity score increases by 1.\nNatural Illusionist: You know the minor illusion cantrip. "
     "Intelligence is your spellcasting ability for it.\n"
     "Speak with Small Beasts: Through sounds and gestures, you can communicate simple ideas with Small or smaller beasts."),
    ("Rock Gnome", {AbilityType.CONSTITUTION: 1},
     "Your Constitution score increases by 1.\n"
     "Artificer's Lore: Whenever you make an Intelligence (History) check related to magic items, alchemical objects, or technological devices, you can add twice your proficiency bonus, instead of any proficiency bonus you normally apply.\n"
     "Tinker: You have proficiency with artisan’s tools (tinker’s tools). "
     "Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp).")
]
basic_races_collection.add_race_with_subraces(gnome_ability_bonuses, 25, gnome_features, gnome_subraces)

# Dragonborn
dragonborn_ability_bonuses = {AbilityType.STRENGTH: 2, AbilityType.CHARISMA: 1}
dragonborn_features = ("Languages: Common, Draconic\n"
                       "Breath Weapon: Choose acid, cold, fire, lightning, or poison. Your breath weapon deals damage "
                       "of the chosen type in a 5 by 30 feet line (Dex save for half damage).\n"
                       "Ability Score Increase: Your Strength score increases by 2, "
                       "and your Charisma score increases by 1.")
basic_races_collection.add_race(Race("Dragonborn", dragonborn_ability_bonuses, 30, dragonborn_features))

# Tiefling
tiefling_ability_bonuses = {AbilityType.INTELLIGENCE: 1, AbilityType.CHARISMA: 2}
tiefling_features = ("Languages: Common, Infernal\n"
                     "Darkvision: 60 feet\n"
                     "Hellish Resistance: Resistance to fire damage.\n"
                     "Ability Score Increase: Your Intelligence score increases by 1, and your Charisma score "
                     "increases by 2.")
basic_races_collection.add_race(Race("Tiefling", tiefling_ability_bonuses, 30, tiefling_features))

# Half-Orc
half_orc_ability_bonuses = {AbilityType.STRENGTH: 2, AbilityType.CONSTITUTION: 1}
half_orc_features = ("Languages: Common, Orcish\n"
                     "Relentless Endurance: When you are reduced to 0 hit points but not killed outright, "
                     "you can drop to 1 hit point instead once per long rest.\n"
                     "Savage Attacks: When you score a critical hit with a melee weapon attack, "
                     "you can roll one of the weapon's damage dice one additional time and "
                     "add it to the extra damage of the critical hit.\n"
                     "Ability Score Increase: Your Strength score increases by 2, and your Constitution score increases by 1.")
basic_races_collection.add_race(Race("Half-Orc", half_orc_ability_bonuses, 30, half_orc_features))

# Half-Elf
half_elf_ability_bonuses = {AbilityType.CHARISMA: 2}  # Note: Half-Elves get +1 to two other abilities of your choice
half_elf_features = (
    "Languages: Common, Elvish, one extra language of your choice\n"
    "Darkvision: Thanks to your elf blood, you have superior vision in dark and dim conditions. "
    "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. "
    "You can’t discern color in darkness, only shades of gray.\n"
    "Fey Ancestry: You have advantage on saving throws against being charmed, and magic can’t put you to sleep.\n"
    "Skill Versatility: You gain proficiency in two skills of your choice.\n"
    "Ability Score Increase: Your Charisma score increases by 2, and two other abilities of your choice increase by 1.\n"
)
basic_races_collection.add_race(Race("Half-Elf", half_elf_ability_bonuses, 30, half_elf_features))