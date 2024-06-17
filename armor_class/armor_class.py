from .armor_class_calculation_strategy_factory import ArmorClassCalculationStrategyFactory
from .armor_class_calculator import ArmorClassCalculator
from abstract_character import AbstractCharacter


class ArmorClass:
    """Represents the armor class of a __character."""

    def __init__(self, character: AbstractCharacter, custom_armor_class: int):
        """
        Initialize an ArmorClass instance.
        """
        self.__character = character
        self.__armor_class_calculator = ArmorClassCalculator(
            ArmorClassCalculationStrategyFactory.choose_armor_class_calculation_strategy(self.__character)
        )
        self.__custom_armor_class = custom_armor_class

    @property
    def armor_class(self):
        """Calculate and return the armor class value for the character."""
        if self.__custom_armor_class == 0:
            return self.calc_armor_class()
        return self.__custom_armor_class

    @armor_class.setter
    def armor_class(self, value):
        """Set the armor class value for the character."""
        value = int(value)
        if value is None:
            raise ValueError("AC cannot be None.")
        elif value < 0:
            raise ValueError("AC cannot be negative.")
        else:
            self.__custom_armor_class = value

    @property
    def custom_armor_class(self):
        """Get custom armor class value for the character."""
        return self.__custom_armor_class

    def calc_armor_class(self) -> int:
        self.__armor_class_calculator = ArmorClassCalculator(
            ArmorClassCalculationStrategyFactory.choose_armor_class_calculation_strategy(self.__character)
        )
        value = self.__armor_class_calculator.calculate_armor_class(self.__character)
        return value
