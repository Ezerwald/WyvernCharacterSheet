from .armor_class_calculation_strategy_factory import ArmorClassCalculationStrategyFactory
from .armor_class_calculator import ArmorClassCalculator
from abstract_character import AbstractCharacter


class ArmorClass:
    """Represents the armor class of a __character."""

    def __init__(self, character: AbstractCharacter, armor_class_value: int):
        """
        Initialize an ArmorClass instance.
        """
        self.__character = character
        self.__armor_class_calculator = ArmorClassCalculator(
            ArmorClassCalculationStrategyFactory.choose_armor_class_calculation_strategy(self.__character)
        )
        self.__armor_class_value = (armor_class_value
                                    or self.__armor_class_calculator.calculate_armor_class(self.__character))

    @property
    def value(self):
        """Calculate and return the armor class value for the character."""
        return self.__armor_class_value

    @value.setter
    def value(self, value):
        value = int(value)
        """Set the armor class value for the character."""
        if value is None:
            raise ValueError("AC cannot be None.")
        elif value < 0:
            raise ValueError("AC cannot be negative.")
        elif value == 0:
            self.__armor_class_value = self.calc_armor_class()
        else:
            self.__armor_class_value = value

    def calc_armor_class(self) -> int:
        self.__armor_class_calculator = ArmorClassCalculator(
            ArmorClassCalculationStrategyFactory.choose_armor_class_calculation_strategy(self.__character)
        )
        value = self.__armor_class_calculator.calculate_armor_class(self.__character)
        return value
