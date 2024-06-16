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
                               subraces: List[Tuple[str, Dict[AbilityType, int], str, Optional[int]]]) -> None:
        """Add a race with its subraces to the collection."""
        for subrace_data in subraces:
            # Unpack each tuple into variables
            subrace_name = subrace_data[0]
            subrace_ability_bonuses = subrace_data[1]
            subrace_features = subrace_data[2]
            if len(subrace_data) == 4 and subrace_data is not None:  # Check if custom subrace speed is provided
                speed = subrace_data[3]
            # Merge text elements
            combined_ability_bonuses = dict(ability_bonuses)
            combined_ability_bonuses.update(subrace_ability_bonuses)
            combined_features = features + subrace_features
            # Create new subrace
            subrace = Race(subrace_name, combined_ability_bonuses, speed, combined_features)
            self.add_race(subrace)

    def remove_race(self, race_name: str) -> None:
        """Remove a race from the collection by its name."""
        if race_name not in self.__races:
            raise ValueError(f"No race '{race_name}' found in the collection.")
        del self.__races[race_name]

    def get_race_by_name(self, race_name: str) -> Optional[Race]:
        """Get a race from the collection by its name."""
        return self.__races.get(race_name)

    def get_all_races(self) -> List[str]:
        """Get all races in the collection."""
        return list(self.__races.keys())


