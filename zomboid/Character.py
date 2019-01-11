#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 12:18:00 2018

@author: Fenris_Wolf
"""
import Inventory
from javaclass import JavaArray
class XP(object):
    def __init__(self):
        pass
    def AddXP(self, perk, value):
        pass

class IsoPlayer(object):
    instance = None
    def __init__(self):
        self.inventory = Inventory.InventoryItemContainer()
        self.inventory.setContainingItem(self)
        self.primary = None
        self.secondary = None
        IsoPlayer.instance = self
    def Say(self, text):
        print ">>>", text
    def playSound(self, *args):
        pass
    def getCurrentState(self):
        return False
    def HasTrait(self, trait):
        return False
    def getJoypadBind(self):
        return -1
    def getCurrentSquare(self):
        return None
    def getSquare(self):
        return None
    def getInventory(self):
        return self.inventory
    def getContainer(self):
        return self.inventory

    def getPrimaryHandItem(self):
        return self.primary

    def setPrimaryHandItem(self, item):
        self.primary = item

    def getSecondaryHandItem(self):
        return self.secondary

    def setSecondaryHandItem(self, item):
        self.secondary = item

    def getXp(self):
        return XP()
    def getPerkLevel(self, perk):
        return 0
    def getCharacterActions(self):
        return JavaArray([])
    def StopAllActionQueue(self):
        return None
    def getRecoilDelay(self):
        return 0
    def DoAttack(self, delta):
        return
    def isBuildCheat(self):
        return False
    def isMechanicsCheat(self):
        return False
    def isHealthCheat(self):
        return False
