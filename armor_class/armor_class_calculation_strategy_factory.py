from game_classes import GameClass, GameClassType
from .armor_class_calculation_strategies import (
    ArmorClassCalculationStrategy,
    DefaultArmorClassCalculationStrategy,
    BarbarianArmorClassCalculationStrategy,
    MonkArmorClassCalculationStrategy
)
from abstract_character import AbstractCharacter


class ArmorClassCalculationStrategyFactory:
    @staticmethod
    def choose_armor_class_calculation_strategy(character: AbstractCharacter) -> ArmorClassCalculationStrategy:
        """Choose the appropriate armor class calculation strategy based on the game class."""
        game_class_type = character.current_game_class.value.type
        armor_name = character.equipped_armor.armor.name
        shield = character.shield
        if not isinstance(game_class_type, GameClassType):
            raise ValueError("Invalid input: 'game_class_type' must be an instance of GameClassType enum")
        if game_class_type == GameClassType.BARBARIAN and armor_name == "None":
            return BarbarianArmorClassCalculationStrategy()
        elif game_class_type == GameClassType.MONK and armor_name == "None" and shield.equipped is False:
            return MonkArmorClassCalculationStrategy()
        else:
            return DefaultArmorClassCalculationStrategy()
