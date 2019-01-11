#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 22:23:48 2018

@author: Fenris_Wolf
"""
import LuaManager
import zomboid.Inventory as InventoryItemFactory
import zomboid.ScriptManager as ScriptManager

def getState(item):
    data = item.modData
    #ammo = lambda item, data: "%s/%s+%s" % ((data.emptyShellChambered > 0 and 'X' or data.roundChambered))
    return "Ammo: %s/%s%s,   Cocked: %s,   Open: %s" % (
            data.currentCapacity,
            data.maxCapacity,
            ((not data.emptyShellChambered is None and data.emptyShellChambered > 0)
                    and '+X' or (not data.roundChambered is None and '+'+str(data.roundChambered) or '')),
            data.hammerCocked,
            data.isOpen,
            )


def firearmTest(item, player, count=1):

    ORGM = LuaManager.instance.globals().ORGM
    Reloadable = ORGM.ReloadableWeapon
    Firearm = ORGM.Firearm

    data = item.modData
    print "######################################"
    print
    print "Live Fire Testing:", item.getDisplayName()

    print "\t\t", getState(item)
    for i in range(count):
        if not Firearm.isLoaded(item):
            if Reloadable.Reload.valid(data, player):
                if data.containsClip != None:
                    print "Ejecting Mag..\t",
                    Reloadable.Reload.start(data, player, item)
                    Reloadable.Reload.perform(data, player, item)
                    print getState(item)
                    if Reloadable.Reload.valid(data, player):
                        print "Inserting Mag..\t",
                        Reloadable.Reload.start(data, player, item)
                        Reloadable.Reload.perform(data, player, item)
                        print getState(item)
                else:
                    Reloadable.Reload.start(data, player, item)
                    while Reloadable.Reload.valid(data, player) and data.currentCapacity < data.maxCapacity:
                        Reloadable.Reload.perform(data, player, item)
                        #printState(item)
                        print "Inserting Round.."

        if Reloadable.Rack.valid(data, player):
            print "Racking..\t\t",
            Reloadable.Rack.start(data, player, item)
            Reloadable.Rack.perform(data, player, item)
            print getState(item)

        if Reloadable.Fire.valid(data) and Reloadable.Fire.pre(data, player, item):
            Reloadable.Fire.post(data, player, item)
            print "Bang!..\t\t", getState(item)
        else: # dryfire
            Reloadable.Fire.dry(data, player, item)
            print "Click!..\t\t", getState(item)


def getMagazineData(item, display=False):
    #ORGM = LuaManager.instance.globals().ORGM
    data = item.modData
    results = [data.magazineData[i+1] for i in range(data.maxCapacity)]
    if display:
        results = [x and ScriptManager.instance.FindItem(u"ORGM."+ x).getDisplayName() or None for x in results ]
    return results

def spawnFirearm(name, defaultBarrel=False, loaded=True, ammo=None, semiAutoMode=True, components=None):
    ORGM = LuaManager.instance.globals().ORGM
    Firearm = ORGM.Firearm
    Ammo = ORGM.Ammo

    if components is None:
        components = []
    item = InventoryItemFactory.CreateItem("ORGM."+ name)
    gunData = Firearm.getData(item)
    Firearm.setup(gunData, item)
    data = item.getModData()
    if defaultBarrel == True:
        data.barrelLength = gunData.barrelLength
    elif defaultBarrel == False:
        pass
    elif isinstance(defaultBarrel,(int,float)) and defaultBarrel > 0:
        data.barrelLength = defaultBarrel

    if Firearm.isSelectFire(item) and semiAutoMode:
        data.selectFire = 0
    if loaded:
        if ammo is None:
            ammo = Ammo.itemGroup(item, True)[1]
        data.lastRound = ammo
        for i in range(data.maxCapacity):
            data.magazineData[i+1] = ammo
        data.currentCapacity = data.maxCapacity
    for comp in components:
        comp = InventoryItemFactory.CreateItem("ORGM."+ comp)
        item.attachWeaponPart(comp)

    Firearm.Stats.set(item)
    return item
