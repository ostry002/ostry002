'''
File: ostry002_assignment2_oop.py
Description: Implementing the behaviour of an alchemist who is owned by a laboratory
Author: Roger Osterdahl
StudentID: 110410137
EmailID: ostry002
This is my own work as defined by the University's Academic Misconduct Policy.
'''

import pytest


class Alchemist(pytest.TestCase):
    def __init__(self, attack, strength, defense, magic, ranged, necromancy, laboratory, recipes):
        self.__attack = attack
        self.__strength = strength
        self.__defense = defense
        self.__magic = magic 
        self.__ranged = ranged 
        self.__necromancy = necromancy
        self.__laboratory = laboratory
        self.__recipes = []
    
    def testGetLaboratory():
        with pytest.raises(TypeError):
            Laboratory(True)
        

    def testGetReceipes(self):
        return self.__recipes
    
    def testMixPotion(self, recipe):
        self.__laboratory.mixPotion(recipe, self)

    def testDrinkPotion(self, potion):
        pass

    def testCollectReagent(self, reagent, amount):
        self.__laboratory.addReagent(reagent, amount)
    
    def testRefineReagents(self):
        pass

    

class Laboratory: 
    def __init__(self, potions, herbs, catalysts):
        self.__potions = potions 
        self.__herbs = herbs 
        self.__catalysts = catalysts

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        pass

    def addReagent(self, reagent, amount):
        pass

class Potion: 
    def __init__(self, name, stat, boost):
        self.__name = name
        self.__stat = stat 
        self.__boost = boost
    
    def calculateBoost(self):
        pass

    def getName(self):
        return self.__name
    
    def getStat(self):
        return self.__stat
    
    def getBoost(self):
        return self.__boost
    
    def setBoost(self):
        pass

class Reagent:
    def __init__(self, name, potency):
        self.__name = name
        self.__potency = potency 
    
    def refine(self):
        pass

    def getName(self):
        return self.__name
    
    def getPotency(self):
        return self.__potency 
    
    def setPotency(self):
        pass 

class SuperPotion(Potion):
    def __init__(self, name, stat, boost, herb, catalyst):
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst 
    
    def calculateBoost(self):
        return super().calculateBoost()
    
    def getHerb(self):
        return self.__herb 
    
    def getCatalyst(self):
        return self.__catalyst 

class ExtremePotion(Potion):
    def __init__(self, name, stat, boost, reagent, potion):
        super().__init__(name, stat, boost)
        self.__reagent = reagent 
        self.__potion = potion 

    def calculateBoost(self):
        return super().calculateBoost()
    
    def getReagent(Reagent):
        return Reagent
    
    def getPotion(Potion):
        return Potion

class Herb(Reagent):
    def __init__(self, name, potency, grimy):
        super().__init__(name, potency)
        self.__grimy = grimy 

    def refine(self):
        return super().refine()

    def getGrimy(self):
        return self.__grimy 
    
    def setGrimy(self):
        pass

class Catalyst(Reagent):
    def __init__(self, name, potency, quality):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        return super().refine()
    
    def getQuality(self):
        return self.__quality 
