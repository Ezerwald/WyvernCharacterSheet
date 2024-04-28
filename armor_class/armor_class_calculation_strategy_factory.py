from character_stats import GameClass
from .armor_class_calculation_strategies import (
    ArmorClassCalculationStrategy,
    DefaultArmorClassCalculationStrategy,
    BarbarianArmorClassCalculationStrategy,
    MonkArmorClassCalculationStrategy
)
from armor import Armor
from shield import Shield


class ArmorClassCalculationStrategyFactory:
    @staticmethod
    def choose_armor_class_calculation_strategy(game_class: GameClass, armor: Armor, shield: Shield) -> ArmorClassCalculationStrategy:
        """Choose the appropriate armor class calculation strategy based on the game class."""
        if not isinstance(game_class, GameClass):
            raise ValueError("Invalid input: '__game_class' must be an instance of GameClassTypes enum")

        if game_class == GameClass.BARBARIAN and armor is None:
            return BarbarianArmorClassCalculationStrategy()
        elif game_class == GameClass.MONK and armor is None and shield.equipped is False:
            return MonkArmorClassCalculationStrategy()
        else:
            return DefaultArmorClassCalculationStrategy()
