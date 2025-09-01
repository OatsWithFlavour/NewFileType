"""Module for calculating armor values based on heavy armor skill level and various multipliers."""

import math as m


class Armor:
    def __init__(self, heavy_armor_lvl: int):
        self.heavy_armor_lvl = heavy_armor_lvl

        self.ancient_knowledge_flag = True
        self.dark_book_flag = True
        self.juggernaut_flag = True
        self.well_fitted_flag = True
        self.matching_set_flag = True

    def juggernaut_mult(self) -> float:
        """Returns the Juggernaut multiplier: 1 to 2"""
        if self.juggernaut_flag:
            rounded_lvl = 20 * int(self.heavy_armor_lvl/ 20)
            multiplier = 1 + min(100, (rounded_lvl + 20)) / 100
            return multiplier
        else:
            return 1

    def ancient_knowledge_mult(self) -> float:
        """Returns the Ancient Knowledge multiplier: 1 or 1.25"""
        if self.ancient_knowledge_mult:
            return 1.25
        else:
            return 1
    
    def black_book_mult(self) -> float:
        """Returns the Black Book multiplier: 1 or 1.25"""
        if self.dark_book_flag:
            return 1.1
        else:
            return 1

    def level_mult(self) -> float:
        """Returns the armor multiplier based on heavy armor skill level: 1 to 1.4"""
        return 1 + min(100, self.heavy_armor_lvl)/100 * 0.4


    def well_fitted_mult(self) -> float:
        """Returns the well fitted multiplier: 1 or 1.25"""
        if self.well_fitted_flag:
            if self.heavy_armor_lvl >= 30:
                return 1.25
            else:
                return 1
        else:
            return 1

    def matching_set_mult(self) -> float:
        """Returns the matching set multiplier: 1 or 1.25"""
        if self.matching_set_flag:     
            if self.heavy_armor_lvl >= 70:
                return 1.25
            else:
                return 1
        else: 
            return 1
        
    def armor_value(self, shield_base_armor: int, no_shield_base_armor: int) -> int:
        """Returns the total armor value based on heavy armor skill level and base armor values"""
        leveled_shield_armor = m.ceil(shield_base_armor * self.level_mult())
        leveled_no_shield_armor = m.ceil(no_shield_base_armor * self.level_mult())
        addtional_multipliers = self.ancient_knowledge_mult() * self.black_book_mult() * self.well_fitted_mult() * self.matching_set_mult()
        armor = int((leveled_shield_armor * self.juggernaut_mult() + leveled_no_shield_armor) * addtional_multipliers)
        return armor