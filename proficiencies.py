from abstract_character import AbstractCharacter
from armor import ArmorType
from typing import List


class Proficiencies:
    def __init__(self, character: AbstractCharacter):
        self.__character: AbstractCharacter = character
        self.__armor: List[ArmorType] = []
        self.__weapons: List[str] = []
        self.__languages: List[str] = []
        self.__tools: List[str] = []

    @property
    def armor(self) -> List[ArmorType]:
        """Get armor proficiencies."""
        return self.__armor

    @property
    def weapons(self) -> List[str]:
        """Get weapon proficiencies."""
        return self.__weapons

    @property
    def languages(self) -> List[str]:
        """Get language proficiencies."""
        return self.__languages

    @property
    def tools(self) -> List[str]:
        """Get tools proficiencies."""
        return self.__tools

    def add_armor(self, armor_type: ArmorType):
        """Add new armor proficiencies."""
        self.__armor.append(armor_type)

    def add_weapon(self, weapon_name: str):
        """Add new weapons proficiencies"""
        self.__weapons.append(weapon_name)

    def add_language(self, language: str):
        """Add new language proficiencies."""
        self.__languages.append(language)

    def add_tool(self, tool_name: str):
        """Add new tool proficiencies."""
        self.__tools.append(tool_name)

    def remove_armor(self, armor_type: ArmorType):
        """Remove armor proficiency"""
        if armor_type in self.__armor:
            self.__armor.remove(armor_type)

    def remove_weapon(self, weapon_name: str):
        """Remove weapon proficiency"""
        if weapon_name in self.__weapons:
            self.__weapons.remove(weapon_name)

    def remove_language(self, language: str):
        """Remove language proficiency"""
        if language in self.__languages:
            self.__languages.remove(language)

    def remove_tool(self, tool_name: str):
        """Remove tool proficiency"""
        if tool_name in self.__tools:
            self.__tools.remove(tool_name)
