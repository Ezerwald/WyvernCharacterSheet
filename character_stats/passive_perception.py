from abstract_character import AbstractCharacter
from skills_types import SkillType


class PassivePerception:
    def __init__(self, character: AbstractCharacter):
        self.__character = character

    @property
    def value(self) -> int:
        """Get the passive perception value."""
        perception_skill = self.__character.skills[SkillType.PERCEPTION]
        return 10 + perception_skill.value

