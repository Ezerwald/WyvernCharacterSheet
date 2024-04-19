from variables import stat_block


class CharacterSheet:
    def __init__(self):
        # column 1
        # basic stats
        self.strength = stat_block.StatBlock()
        self.dexterity = stat_block.StatBlock()
        self.constitution = stat_block.StatBlock()
        self.intelligence = stat_block.StatBlock()
        self.wisdom = stat_block.StatBlock()
        self.charisma = stat_block.StatBlock()

        # column 2
        # inspiration point and proficiency bonus
        self.inspiration = False
        self.prof_bonus = 2

        # saving throws proficiency
        self.strength_saving_throw_prof = False
        self.dexterity_saving_throw_prof = False
        self.constitution_saving_throw_prof = False
        self.intelligence_saving_throw_prof = False
        self.wisdom_saving_throw_prof = False
        self.charisma_saving_throw_prof = False

        # saving throws values
        self.strength_saving_throw = self.strength_mod
        self.dexterity_saving_throw = self.dexterity_mod
        self.constitution_saving_throw = self.constitution_mod
        self.intelligence_saving_throw = self.intelligence_mod
        self.wisdom_saving_throw = self.wisdom_mod
        self.charisma_saving_throw = self.charisma_mod

        # __skills proficiency
        self.acrobatics_prof = False
        self.animal_handling_prof = False
        self.arcana_prof = False
        self.athletics_prof = False
        self.deception_prof = False
        self.history_prof = False
        self.insight_prof = False
        self.intimidation_prof = False
        self.investigation_prof = False
        self.medicine_prof = False
        self.nature_prof = False
        self.perception_prof = False
        self.performance_prof = False
        self.persuasion_prof = False
        self.religion_prof = False
        self.sleight_of_hand_prof = False
        self.stealth_prof = False
        self.survival_prof = False

        # skill modifier
        self.acrobatics = 0
        self.animal_handling = 0
        self.arcana = 0
        self.athletics = 0
        self.deception = 0
        self.history = 0
        self.insight = 0
        self.intimidation = 0
        self.investigation = 0
        self.medicine = 0
        self.nature = 0
        self.perception = 0
        self.performance = 0
        self.persuasion = 0
        self.religion = 0
        self.sleight_of_hand = 0
        self.stealth = 0
        self.survival = 0

        # column 3
        self.armor_class = 8 + self.dexterity_mod
        self.initiative = self.dexterity_mod

        # defined by race and class
        self.speed = 0
        self.hit_points = 0
        self.temp_hit_points = 0
        self.hit_dice = {}
        self.death_saves_success = 0
        self.death_saves_fail = 0

        self.passive_perception = 8 + self.perception
