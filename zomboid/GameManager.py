#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:31:15 2018

@author: Fenris_Wolf
"""
import settings
ActiveMods = { }

class Mod(object):
    def __init__(self, path):
        self.dir = path
        #fi = open(path+"mod.info")
    def getWorkshopID(self):
        return None

def addMod(name):
    ActiveMods[name] = Mod(settings.cache+"mods/"+name+"/")
