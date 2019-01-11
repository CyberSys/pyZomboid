#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 11:32:52 2018

@author: Fenris_Wolf
"""

from javaclass import JavaArray
Professions = { }
class Profession(object):
    def __init__(self, name, displayName, icon, points):
        self.name = name
        self.displayName = displayName
        self.icon = icon
        self.points = points
        self.desc = ""
        self.xp = { }
        self.recipes = JavaArray()
        self.traits =  JavaArray()

    def getType(self):
        return self.name
    def addXPBoost(self, perk, value):
        self.xp[perk] = value
    def addFreeTrait(self, trait):
        self.traits.add(trait)

    def getFreeRecipes(self):
        return self.recipes
    def getDescription(self):
        return self.desc
    def setDescription(self, desc):
        self.desc = desc
    def getXPBoostMap(self):
        return self.xp
    def getFreeTraits(self):
        return self.traits


def addProfession(name, displayName, icon, points):
    print "Adding Profession", name
    Professions[name] = Profession(name, displayName, icon, points)
    return Professions[name]

def getProfessions():
    return JavaArray(Professions.values())
