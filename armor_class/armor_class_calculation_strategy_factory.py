from game_classes import GameClass, GameClassType
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
    def choose_armor_class_calculation_strategy(game_class: GameClass, armor: Armor, shield: Shield) \
            -> ArmorClassCalculationStrategy:
        """Choose the appropriate armor class calculation strategy based on the game class."""
        game_class_type = game_class.type
        if not isinstance(game_class_type, GameClassType):
            raise ValueError("Invalid input: 'game_class_type' must be an instance of GameClassType enum")

        if game_class_type == GameClassType.BARBARIAN and armor.name == "None":
            return BarbarianArmorClassCalculationStrategy()
        elif game_class_type == GameClassType.MONK and armor.name == "None" and shield.equipped is False:
            return MonkArmorClassCalculationStrategy()
        else:
            return DefaultArmorClassCalculationStrategy()
