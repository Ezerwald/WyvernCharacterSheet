from typing import Any
from armor import Armor
from shield.shield import Shield


class ArmorClassCalculator:
    """Calculates armor class based on different strategies."""

    def __init__(self, strategy: Any) -> None:
        """Initialize with the given strategy."""
        self.__strategy = strategy

    def set_strategy(self, strategy: Any) -> None:
        """Set a new strategy for calculating armor class."""
        self.__strategy = strategy

    def calculate_armor_class(self, shield: Shield, armor: Armor, abilities: dict) -> int:
        """Calculate armor class based on the current strategy."""
        return self.__strategy.calculate(shield, armor, abilities)
