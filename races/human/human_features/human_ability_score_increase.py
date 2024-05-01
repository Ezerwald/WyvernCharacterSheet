from abstract_character import AbstractCharacter
from abstract_feature import AbstractFeature
from utils import ability_score_increase
from character_stats import AbilityType


class HumanAbilityScoreIncrease(AbstractFeature):
    def __init__(self, character: AbstractCharacter):
        super().__init__(character)
        self.__character = character
        self.__name = None
        self.__description = None
        self.__source = None
        self.__ability_bonuses = {AbilityType.STRENGTH: 1,
                                  AbilityType.DEXTERITY: 1,
                                  AbilityType.CONSTITUTION: 1,
                                  AbilityType.WISDOM: 1,
                                  AbilityType.INTELLIGENCE: 1,
                                  AbilityType.CHARISMA: 1
                                  }

    def functionality(self):
        """Functionality of feature"""
        ability_score_increase(self.__character, self.__ability_bonuses)

    @property
    def name(self) -> str:
        """Get the name of the feature."""
        return self.__name

    @property
    def description(self) -> str:
        """Get the description of the feature."""
        return self.__description

    @property
    def source(self) -> str:
        """Get the source of the feature."""
        return self.__source
