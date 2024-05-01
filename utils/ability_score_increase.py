from character_stats import AbilityType
from typing import Dict
from abstract_character import AbstractCharacter


# function for increasing chosen abilities scores by some number

def ability_score_increase(character: AbstractCharacter, abilities_scores: Dict[AbilityType, int]):
    for ability in abilities_scores:
        character.abilities[ability].score += abilities_scores[ability]
