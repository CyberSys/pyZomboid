## example_orgm.py
# example usage of pyZomboid, with ORGM.
# run this from your interactive python shell

import zomboid.settings as settings
import zomboid.LuaManager as LuaManager
import zomboid.ScriptManager as ScriptManager
import zomboid.EventManager as EventManager
import zomboid.GameManager as GameManager
import zomboid.TranslationManager as TranslationManager
from zomboid.Character import IsoPlayer

# utilities for dealing with orgm
from zomboid.orgmutil import spawnFirearm, firearmTest


settings.pzdir = '/home/wolf/local/Project Zomboid/game/projectzomboid/'
settings.cache = '/home/wolf/Zomboid/'

## this expects the mod to be in the cache dir above. Only a single mod can be
## loaded atm, and most will probably crash due to missing java api calls
GameManager.addMod('ORGM')

ScriptManager.init()
LuaManager.init()
TranslationManager.init()

LuaManager.loadSharedLua()
LuaManager.loadClientLua()
EventManager.Trigger('OnLoadSoundBanks')
EventManager.Trigger('OnGameBoot')
#
LuaManager.loadServerLua()
EventManager.Trigger('OnPreDistributionMerge')
EventManager.Trigger('OnDistributionMerge')
EventManager.Trigger('OnPostDistributionMerge')
#EventManager.Trigger('OnGameStart', IsoPlayer())

ORGM = LuaManager.instance.globals().ORGM
#Reloadable = ORGM.ReloadableWeapon
#
print
print "*** pyZomboid shell started ***"
if ORGM:
    print "(ORGM version is %s)" % ORGM.BUILD_HISTORY[ORGM.BUILD_ID]
    print "ORGM Stats:"
    print len([x for x in ORGM.Firearm.getTable().keys()]), "Firearms"
    print len([x for x in ORGM.Magazine.getTable().keys()]), "Magazines"
    print len([x for x in ORGM.Ammo.getTable().keys()]), "Caliber/Bullet Combos"
    print len([x for x in ORGM.Component.getTable().keys()]), "Components/Attachments"
    print len([x for x in ORGM.Maintance.getTable().keys()]), "Maintance Kits"

    Firearm = ORGM.Firearm

    player = IsoPlayer()
    # add a raging bull and some ammo, note this defaults to spawning loaded.
    player.getInventory().AddItems("ORGM.Ammo_454Casull_HP", 2)
    item1 = spawnFirearm("Taurus454", defaultBarrel=True,components=[])
    player.getInventory().AddItem(item1)
    firearmTest(item1, player, 10) # lets pull the trigger 10 times


    ############################################################################
    # add a 1911
    item2 = spawnFirearm("M1911", defaultBarrel=True,ammo=None,components=[])
    player.getInventory().AddItem(item2)

    # directly call ORGM's magazine spawning function. This function is in
    # server/1LoadOrder/ORGMServerSpawn.lua, and defined as:
    # function(container, gunType, ammoType, chance, max, isLoaded)
    ORGM.Server.Spawn.magazine(player.getInventory(), "M1911", "Ammo_45ACP_HP", 1000, 10, True)
    # print the current ammo count store in each mags mod data.
    print "######################################"
    print "spare 1911 magazines:"
    print [x.modData.currentCapacity for x in player.getInventory().items['M1911Mag'].data]
    firearmTest(item2, player, 15) # lets pull the trigger 10 times
