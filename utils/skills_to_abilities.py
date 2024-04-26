from character_stats import AbilityType
from skills_types import SkillType


SKILLS_TO_ABILITIES = {
    SkillType.ACROBATICS: AbilityType.DEXTERITY,
    SkillType.ANIMAL_HANDLING: AbilityType.WISDOM,
    SkillType.ARCANA: AbilityType.INTELLIGENCE,
    SkillType.ATHLETICS: AbilityType.STRENGTH,
    SkillType.DECEPTION: AbilityType.CHARISMA,
    SkillType.HISTORY: AbilityType.INTELLIGENCE,
    SkillType.INSIGHT: AbilityType.WISDOM,
    SkillType.INTIMIDATION: AbilityType.CHARISMA,
    SkillType.INVESTIGATION: AbilityType.INTELLIGENCE,
    SkillType.MEDICINE: AbilityType.WISDOM,
    SkillType.NATURE: AbilityType.INTELLIGENCE,
    SkillType.PERCEPTION: AbilityType.WISDOM,
    SkillType.PERFORMANCE: AbilityType.CHARISMA,
    SkillType.RELIGION: AbilityType.INTELLIGENCE,
    SkillType.SLEIGHT_OF_HAND: AbilityType.DEXTERITY,
    SkillType.STEALTH: AbilityType.DEXTERITY,
    SkillType.SURVIVAL: AbilityType.WISDOM,
}
