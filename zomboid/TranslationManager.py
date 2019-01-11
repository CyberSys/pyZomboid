#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 12:11:46 2018

@author: Fenris_Wolf
"""

import LuaManager
import GameManager
import javaclass

Text = { }

def getText(text, *args):
    return Text.get(text, unicode(text)) # maybe add a % args

def getTextOrNull(text):
    return Text.get(text, None)

def getAvailableLanguage():
    return javaclass.JavaArray([
            LuaManager.instance.eval('{ text = function() return "EN" end }' )
            ])


def loadFile(path):
    try:
        fi = open(path)
        lines = fi.read()
        fi.close()
        table_name, junk = lines.split(' ',1)
        LuaManager.instance.execute(lines)
        table = LuaManager.instance.globals()[table_name]
        for k, v in table.items():
            Text[k] = v

    except IOError:
        pass

def init():
    # skip loading vanilla stuff for now
    filenames = ["Items_EN", "IG_UI_EN"]
    for name, mod in GameManager.ActiveMods.items():
        for f in filenames:
            loadFile(mod.dir + "/media/lua/shared/Translate/EN/%s.txt" % f)
