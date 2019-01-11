#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:33:48 2018

@author: Fenris_Wolf
"""
import ScriptManager
import LuaManager
from javaclass import JavaArray

class InventoryItemContainer(object):
    def __init__(self):
        self.items = { }
        self.parent = None
    def getItemsFromType(self, itemType):
        return self.items.get(itemType, JavaArray([]))

    def FindAndReturn(self,itemType):
        stack = self.items.get(itemType)
        if not stack or stack.size() == 0:
            return
        return stack.get(0)

    def hasRoomFor(self, arg1, weight):
        return True

    def getContainingItem(self):
        return self.parent

    def setContainingItem(self, item):
        self.parent = item

    def AddItem(self, item):
        if isinstance(item, (str,unicode)):
            item = CreateItem(item)
            if not item:
                return

        item.container = self
        #name = item.getDisplayName()
        try:
            self.items[item.getType()].add(item)
        except KeyError:
            self.items[item.getType()] = JavaArray([item])
        return item

    def AddItems(self, item, count):
        for i in range(count):
            self.AddItem(item)

    def Remove(self, item):
        try:
            self.items[item.getType()].remove(item)
        except KeyError:
            pass

    def RemoveOneOf(self, itemType):
        try:
            item = self.items[itemType].data.pop(0)
            item.container = None
            return item
        except KeyError:
            pass



class InventoryItem(object):
    def __init__(self, script):
        self.script = ScriptManager.ScriptManager().FindItem(script)
        self.data = {}
        for k,v in self.script.data.items():
            self.data[k] = v
        self.modData = LuaManager.instance.eval("{}")
        self.container = None
        self.condition = self.getConditionMax()
        self.scope = None
        self.sling = None
        self.recoilpad = None
        self.stock = None
        self.canon = None
        self.clip = None

    def __str__(self):
        return self.getFullType()

    def _get(self, key, default=None):
        return self.data.get(key, default)
    def getDisplayName(self):
        return self.script.getDisplayName()
    def getType(self):
        return self.script.type
    def getFullType(self):
        return self.script.module + "." + self.script.type
    def getModule(self):
        return self.script.module
    def getModData(self):
        return self.modData
    def getConditionMax(self):
        return int(self._get("ConditionMax", 100))
    def getCondition(self):
        return self.condition

    def getWeight(self):
        return float(self._get("Weight", 0.1))
    def setWeight(self, value):
        self.data["Weight"] = value
    def getActualWeight(self):
        return float(self._get("Weight", 0.1))
    def setActualWeight(self, value):
        self.data["Weight"] = value

    def getSwingSound(self):
        return self._get("SwingSound")
    def getSoundRadius(self):
        return int(self._get("SoundRadius"))

    def getAmmoType(self):
        return self._get("AmmoType")
    def getClipSize(self):
        return int(self._get("ClipSize"))

    def getMinDamage(self):
        return float(self._get("MinDamage"))
    def setMinDamage(self, value):
        self.data["MinDamage"] = value
    def getMaxDamage(self):
        return float(self._get("MaxDamage"))
    def setMaxDamage(self, value):
        self.data["MaxDamage"] = value
    def getDoorDamage(self):
        return float(self._get("DoorDamage"))
    def setDoorDamage(self, value):
        self.data["DoorDamage"] = value
    def getTreeDamage(self):
        return float(self._get("TreeDamage"))
    def setTreeDamage(self, value):
        self.data["TreeDamage"] = value

    def getMaxHitCount(self):
        return float(self._get("MaxHitCount"))
    def setMaxHitCount(self, value):
        self.data["MaxHitCount"] = value

    def getAimingTime(self):
        return float(self._get("AimingTime"))
    def setAimingTime(self, value):
        self.data["AimingTime"] = value

    def getRecoilDelay(self):
        return int(self._get("RecoilDelay"))
    def setRecoilDelay(self, value):
        self.data["RecoilDelay"] = value

    def getHitChance(self):
        return int(self._get("HitChance"))
    def setHitChance(self, value):
        self.data["HitChance"] = value

    def getCriticalChance(self):
        return int(self._get("CriticalChance"))
    def setCriticalChance(self, value):
        self.data["CriticalChance"] = value


    def setAimingPerkCritModifier(self, value):
        self.data["AimingPerkCritModifier"] = value
    def setAimingPerkHitChanceModifier(self, value):
        self.data["AimingPerkHitChanceModifier"] = value

    def getReloadTime(self):
        return float(self._get("ReloadTime"))
    def setReloadTime(self, value):
        self.data["ReloadTime"] = value

    def getMaxRange(self):
        return float(self._get("MaxRange"))
    def setMaxRange(self, value):
        self.data["MaxRange"] = value
    def getMinRangeRanged(self):
        return float(self._get("MinRangeRanged",0))
    def setMinRangeRanged(self, value):
        self.data["MinRangeRanged"] = value

    def getMinAngle(self):
        return float(self._get("MinAngle"))
    def setMinAngle(self, value):
        self.data["MinAngle"] = value

    def getSwingTime(self):
        return float(self._get("SwingTime"))
    def setSwingTime(self, value):
        self.data["SwingTime"] = value
    def setMinimumSwingTime(self, value):
        self.data["MinimumSwingTime"] = value

    def getPiercingBullets(self):
        return float(self._get("PiercingBullets"))
    def setPiercingBullets(self, value):
        self.data["PiercingBullets"] = value

    def attachWeaponPart(self, part):
        parttype = part.data['PartType'].lower()
        if parttype == 'canon':
            self.canon = part
        elif parttype == 'scope':
            self.scope = part
        elif parttype == 'stock':
            self.stock = part
        elif parttype == 'sling':
            self.sling = part
        elif parttype == 'clip':
            self.clip = part
        elif parttype == 'recoilpad':
            self.recoilpad = part

        pass
    def getCanon(self):
        return self.canon
    def getScope(self):
        return self.scope
    def getStock(self):
        return self.stock
    def getSling(self):
        return self.sling
    def getClip(self):
        return self.clip
    def getRecoilpad(self):
        return self.recoilpad


    def getWeightModifier(self):
        return self.data.get('WeightModifier',0)


# InventoryItemFactory

def CreateItem(itemType):
    item = InventoryItem(itemType)
    return item
