from character_stats.abilities_types import AbilityType
from character_stats.skills_types import SkillType

SKILLS_TO_ABILITIES = {
    SkillType.ACROBATICS.value: AbilityType.DEXTERITY.value,
    SkillType.ANIMAL_HANDLING.value: AbilityType.WISDOM.value,
    SkillType.ARCANA.value: AbilityType.INTELLIGENCE.value,
    SkillType.ATHLETICS.value: AbilityType.STRENGTH.value,
    SkillType.DECEPTION.value: AbilityType.CHARISMA.value,
    SkillType.HISTORY.value: AbilityType.INTELLIGENCE.value,
    SkillType.INSIGHT.value: AbilityType.WISDOM.value,
    SkillType.INTIMIDATION.value: AbilityType.CHARISMA.value,
    SkillType.INVESTIGATION.value: AbilityType.INTELLIGENCE.value,
    SkillType.MEDICINE.value: AbilityType.WISDOM.value,
    SkillType.NATURE.value: AbilityType.INTELLIGENCE.value,
    SkillType.PERCEPTION.value: AbilityType.WISDOM.value,
    SkillType.PERFORMANCE.value: AbilityType.CHARISMA.value,
    SkillType.RELIGION.value: AbilityType.INTELLIGENCE.value,
    SkillType.SLEIGHT_OF_HAND.value: AbilityType.DEXTERITY.value,
    SkillType.STEALTH.value: AbilityType.DEXTERITY.value,
    SkillType.SURVIVAL.value: AbilityType.WISDOM.value,
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

MAX_MODIFIER_VALUE = 5

NO_ARMOR_AC = 10
MIN_DEXTERITY_BONUS_TO_AC = 10

DEFAULT_SHIELD_BONUS_TO_AC = 2
