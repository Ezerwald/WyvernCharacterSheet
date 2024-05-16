from constants.constants import MIN_ABILITY_VALUE, MAX_ABILITY_VALUE
from .abilities_types import AbilityType
from abstract_character import AbstractCharacter


class Ability:
    """Class to represent an ability of a character."""

    def __init__(self, character: AbstractCharacter, ability_type: AbilityType, score: int):
        """
        Initialize an Ability instance.

        Parameters:
        - character (AbstractCharacter): The character to which this ability belongs.
        - ability_type (AbilityType): The type of ability (e.g., Strength, Dexterity).
        - score (int): The initial score of the ability.
        """
        self.__character = character
        self.__ability_type = ability_type
        self.__score = score

    @property
    def score(self) -> int:
        """Get the score of the ability."""
        return self.__score

    @score.setter
    def score(self, new_score: int) -> None:
        """Set the score of the ability, validating the input."""
        new_score = int(new_score)
        if MIN_ABILITY_VALUE <= new_score <= MAX_ABILITY_VALUE:
            self.__score = new_score
        else:
            raise ValueError("Invalid Ability Value")

    @property
    def modifier(self) -> int:
        """Calculate and return the modifier for the ability."""
        modifier = (self.__score - 10) // 2
        return modifier
