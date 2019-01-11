## example.py
# example usage of pyZomboid.
# run this from your interactive python shell

import zomboid.settings as settings
import zomboid.LuaManager as LuaManager
import zomboid.ScriptManager as ScriptManager
import zomboid.EventManager as EventManager
import zomboid.GameManager as GameManager
import zomboid.TranslationManager as TranslationManager
from zomboid.Character import IsoPlayer

settings.pzdir = '/home/wolf/local/Project Zomboid/game/projectzomboid/'
settings.cache = '/home/wolf/Zomboid/'

ScriptManager.init()
LuaManager.init()
TranslationManager.init()

LuaManager.loadSharedLua()
LuaManager.loadClientLua()
EventManager.Trigger('OnLoadSoundBanks')
EventManager.Trigger('OnGameBoot')

LuaManager.loadServerLua()
EventManager.Trigger('OnPreDistributionMerge')
EventManager.Trigger('OnDistributionMerge')
EventManager.Trigger('OnPostDistributionMerge')

# note the emulater isn't complete enough to send the next event...
#EventManager.Trigger('OnGameStart', IsoPlayer())
### 
print
print "*** pyZomboid shell started ***"

### this "would" work, but the scripts/*.txt parser needs a rewrite, to handle
### some of the vanilla files like vehicles. It parses the simple item files
### fine, but for now vanilla txt script parsing is disabled.

# import zomboid.Inventory as InventoryItemFactory
# player = IsoPlayer()
# item = InventoryItemFactory.CreateItem("Base.Hammer")
# player.getInventory().AddItem(item)
# player.setPrimaryHandItem(item)
# EventManager.Trigger('OnEquipPrimary', player, item)
# player.getInventory().AddItems("Base.Nail", 10)
