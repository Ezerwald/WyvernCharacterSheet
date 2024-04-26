from .armor_class_calculation_strategy_factory import ArmorClassCalculationStrategyFactory
from .armor_class_calculator import ArmorClassCalculator
from abstract_character import AbstractCharacter


class ArmorClass:
    """Represents the armor class of a __character."""

    def __init__(self, character: AbstractCharacter):
        """
        Initialize an ArmorClass instance.
        """
        self.__character = character
        self.__armor_class_calculator = ArmorClassCalculator(
            ArmorClassCalculationStrategyFactory.choose_armor_class_calculation_strategy(
                self.__character.game_class, self.__character.equipped_armor.armor, self.__character.shield
            )
        )

    @property
    def value(self):
        """Calculate and return the armor class value for the __character."""
        value = self.__armor_class_calculator.calculate_armor_class(
            self.__character.shield,
            self.__character.equipped_armor.armor,
            self.__character.abilities
        )
        return value
