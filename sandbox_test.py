from enum import Enum, auto
from typing import Dict


class AbilityType(Enum):
    STRENGTH = "STR"
    DEXTERITY = "DEX"
    CONSTITUTION = "CON"
    INTELLIGENCE = "INT"
    WISDOM = "WIS"
    CHARISMA = "CHA"


print(ability.value for ability in AbilityType)

#
abilities_scores = {
    "STR": 18,
    "DEX": 16,
    "CON": 14,
    "INT": 12,
    "WIS": 10,
    "CHA": 8
}


def __initialize_abilities(abilities_scores: Dict[str, int]):
    """Initialize the character's abilities."""
    print(abilities_scores["STR"])


__initialize_abilities(abilities_scores)
