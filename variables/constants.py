from variables.abilities_types import AbilityType

SKILLS_TO_ABILITIES = {
    'acrobatics': AbilityType.DEXTERITY.value,
    'animal_handling': AbilityType.WISDOM.value,
    'arcana': AbilityType.INTELLIGENCE.value,
    'athletics': AbilityType.STRENGTH.value,
    'deception': AbilityType.CHARISMA.value,
    'history': AbilityType.INTELLIGENCE.value,
    'insight': AbilityType.WISDOM.value,
    'intimidation': AbilityType.CHARISMA.value,
    'investigation': AbilityType.INTELLIGENCE.value,
    'medicine': AbilityType.WISDOM.value,
    'nature': AbilityType.INTELLIGENCE.value,
    'perception': AbilityType.WISDOM.value,
    'performance': AbilityType.CHARISMA.value,
    'religion': AbilityType.INTELLIGENCE.value,
    'sleight_of_hand': AbilityType.DEXTERITY.value,
    'stealth': AbilityType.DEXTERITY.value,
    'survival': AbilityType.WISDOM.value,
}

PROFICIENCY_BONUS = {1: 2,
                     2: 2,
                     3: 2,
                     4: 2,
                     5: 3,
                     6: 3,
                     7: 3,
                     8: 3,
                     9: 4,
                     10: 4,
                     11: 4,
                     12: 4,
                     13: 5,
                     14: 5,
                     15: 5,
                     16: 5,
                     17: 6,
                     18: 6,
                     19: 6,
                     20: 6}

MIN_LEVEL = 1
MAX_LEVEL = 20

MIN_ABILITY_VALUE = 1
MAX_ABILITY_VALUE = 20
