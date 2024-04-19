from abilities_types import AbilityType
from typing import List, Dict

DEFAULT = 0
PROFICIENCY_BONUS = 2


class SavingThrows:
    __saving_throws: List[int]
    __proficient_saving_throws: List[int]

    def __init__(self):
        self.__saving_throws = []
        self.__proficient_saving_throws = []

    def add_saving_throw(self, saving_throw_type: AbilityType):
        self.__saving_throws.append(saving_throw_type.value)

    def add_proficient_throw(self, saving_throw_type: AbilityType):
        self.__proficient_saving_throws.append(saving_throw_type.value)

    def get_all_saving_throws(self) -> Dict[int, int]:
        out = {}

        for s in AbilityType:
            out[s.value] = (DEFAULT + PROFICIENCY_BONUS) if s.value in self.__proficient_saving_throws else DEFAULT
        return out


saving_throws = SavingThrows()
saving_throws.add_saving_throw(AbilityType.STRENGTH)
saving_throws.add_proficient_throw(AbilityType.STRENGTH)
