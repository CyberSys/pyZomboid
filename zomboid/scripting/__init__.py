# -*- coding: utf-8 -*-
import logging
import re
import os
#import GameManager
#from .script import Script, LoadedScripts
from .parser import ScriptParser

def init():
    logger.info("Loading media/scripts")
    fp = os.path.join(settings.pzdir, "media/scripts")
    #1for filename in [x for x in os.walk(fp)][0][2]:
        #Script(filename=filename, path="media/scripts", root_path=settings.pzdir)

    #Script('vehiclesitems.txt', settings.pzdir+"media/scripts/vehicles")
    
    #for name, mod in GameManager.ActiveMods.items():
    #    for filename in [x for x in os.walk(mod.dir+"media/scripts")][0][2]:
    pass
