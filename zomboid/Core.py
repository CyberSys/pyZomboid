#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 14:34:06 2018

@author: Fenris_Wolf
"""
import LuaManager
import javaclass

class Core(object):
    def __init__(self):
        pass
    def getScreenWidth(self):
        return 1366
    def getScreenHeight(self):
        return 768
    def getOptionReloadDifficulty(self):
        return 2
    def getGameMode(self):
        return None
    def getVersionNumber(self):
        return 1
    def getScreenModes(self):
        return LuaManager.instance.eval("{}")
    def getDefaultZoomLevels(self):
        return javaclass.JavaArray([50, 100, 150, 200])
    def getObjectHighlitedColor(self):
        return javaclass.Color()
instance = Core()
