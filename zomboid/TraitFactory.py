#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 09:35:30 2018

@author: Fenris_Wolf
"""
from javaclass import JavaArray
Traits = { }
class Trait(object):
    def __init__(self, name, displayName, cost, desc, profession, disableMP=True):
        self.name = name
        self.displayName = displayName
        self.cost = cost
        self.desc = desc
        self.profession = profession
        self.disableMP = disableMP
        self.xp = { }
        self.recipes = JavaArray()
        self.exclusive = JavaArray()

    def addXPBoost(self, perk, value):
        self.xp[perk] = value

    def getFreeRecipes(self):
        return self.recipes
    def getDescription(self):
        return self.desc
    def setDescription(self, desc):
        self.desc = desc
    def getLabel(self):
        return self.displayName
    def getXPBoostMap(self):
        return self.xp

def setMutualExclusive(trait1, trait2):
    Traits[trait1].exclusive.add(trait2)
    Traits[trait2].exclusive.add(trait1)


def addTrait(name, displayName, cost, desc, profession, disableMP=True):
    print "Adding Trait", name
    Traits[name] = Trait(name, displayName, cost, desc, profession, disableMP)
    return Traits[name]

def sortList():
    pass

def getTraits():
    return JavaArray(Traits.values())

def getTrait(name):
    return Traits[name]
