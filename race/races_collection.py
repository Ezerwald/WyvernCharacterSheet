from typing import Dict, Optional, List, Tuple
from .races import Race
from character_stats import AbilityType


class RaceCollection:
    def __init__(self):
        self.__races: Dict[str, Race] = {}

    def add_race(self, race: Race) -> None:
        """Add a race to the collection."""
        race_name = race.name
        if race_name in self.__races:
            raise ValueError(f"Race '{race_name}' already exists in the collection.")
        self.__races[race_name] = race

    def add_race_with_subraces(self, ability_bonuses: Dict[AbilityType, int], speed: int, features: str,
                               subraces: List[Tuple[str, Dict[AbilityType, int], str]]) -> None:
        """Add a race with its subraces to the collection."""
        for subrace_name, subrace_ability_bonuses, subrace_features in subraces:
            combined_ability_bonuses = dict(ability_bonuses)
            combined_ability_bonuses.update(subrace_ability_bonuses)
            combined_features = features + subrace_features
            subrace = Race(subrace_name, combined_ability_bonuses, speed, combined_features)
            self.add_race(subrace)

    def remove_race(self, race_name: str) -> None:
        """Remove a race from the collection by its character_name."""
        if race_name not in self.__races:
            raise ValueError(f"No race '{race_name}' found in the collection.")
        del self.__races[race_name]

    def get_race(self, race_name: str) -> Optional[Race]:
        """Get a race from the collection by its character_name."""
        return self.__races.get(race_name)

    def get_all_races(self) -> Dict[str, Race]:
        """Get all races in the collection."""
        return self.__races.copy()
