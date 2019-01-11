#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 08:35:30 2018

@author: Fenris_Wolf
"""
import random
import javaclass
import ScriptManager
import EventManager
import LuaManager
import settings
import GameManager
import Core
import Character
import TranslationManager
#from TranslationManager import getText, getTextOrNull

# globals



def ZombRand(*args):
    start = 1
    stop = 1

    if len(args) == 2:
        start = args[0]
    stop = args[-1]
    return random.randint(start, stop-1)

def ZombRandFloat(start, stop):
    return random.uniform(start, stop)
def getNumActivePlayers():
    return 1

def getDebug():
    return False
def isDemo():
    return False
def isServer():
    return False
def isClient():
    return False
def getTextManager():
    return javaclass.TextManager()
def getTexture(path):
    return LuaManager.instance.eval(
            "{getWidth = function() return 0 end, getHeight = function() return 0 end,}"
            )

def getSteamModeActive():
    return False
def getModInfoByID(mod, arg2=None): #arg2 is a fix due to tuple expansion and orgm copyprotect?
    return GameManager.ActiveMods.get(mod)
def getScriptManager():
    return ScriptManager.instance

def getSandboxOptions():
    return javaclass.SandboxOptions()

def triggerEvent(event, *args):
    EventManager.Events[event].Trigger(*args)

def getFileReader(filename, create=False):
    return javaclass.BufferedReader(settings.cache +"/Lua/"+filename)

def getCore():
    return Core.instance

def instanceof(item, instance):
    return True

class KahluaObject(object):
    def __init__(self, value):
        self.value = value

    def intValue(self):
        return int(self.value)

def transformIntoKahluaTable(data):
    result = data
    if isinstance(data, dict):
        result =  LuaManager.instance.eval("{}")
        for k,v in data.items():
            result[k] = KahluaObject(v)
    #elif isinstance(data, (list, tuple)):
    return result

def getPlayer():
    return Character.IsoPlayer.instance

def getSpecificPlayer(id):
    return Character.IsoPlayer.instance

def nullFunc(*args):
    pass

def init(lua):

    lua.execute("Keyboard = {}")
    lua.execute("UIFont = { Small = 1, Medium = 1}")
    lua.execute("SimpleDateFormat = { new = function(x) return end }")
    lua.execute("IsoFlagType = { }")
    lua.execute("Vector3f = { new = function(x) return end }")
    #lua.execute("ScriptManager = {instance = {FindItem = function(self, item) return nil end }}")
    lua.execute("string.sort = function(a, b) return a > b end")
    lua.globals().string.contains = lambda x,y: y in x
    lua.globals().string.trim = lambda x: x.strip()

    lua.execute("CGlobalObjects = { getSystemCount = function(self) return 0 end}")
    lua.execute("SGlobalObjects = { getSystemCount = function(self) return 0 end}")
    lua.execute("MapObjects = { OnNewWithSprite = function(x,y,z) end, OnLoadWithSprite = function() end }")
    lua.execute("getActivatedMods = function() return {contains = function(x,y) return false end} end")
    lua.execute("useTextureFiltering = function() return  end")
    lua.execute("getLatestSave = function() return {} end")


    lua.execute("UIElement = { }")
    lua.globals().UIElement.new = lambda x: javaclass.UIElement(x)
    lua.execute("UITransition = { }")
    lua.globals().UITransition.new = javaclass.UITransition


    lua.execute("ColorInfo = { new = function() return end }")
    lua.execute("""ObservationFactory = {
            addObservation = function() end,
            setMutualExclusive = function() end,
            } """)
    lua.execute("""SurvivorFactory = {
            addSurname = function() end,
            addFemaleForename = function() end,
            addMaleForename = function() end,
            } """)
    lua.execute("""SurvivorDesc = {
            addTrouserColor = function() end,
            addHairColor= function() end,
            } """)

    lua.execute("""getFMODSoundBank = function() return {
            addVoice = function() end,
            addFootstep = function() end,
            } end""")
    lua.execute("""getSoundManager = function() return {
            PlayWorldSound = function() end,
            addFootstep = function() end,
            } end""")
    lua.execute("""VoiceManager = {}""")
    lua.globals().VoiceManager.RecordDevices = javaclass.JavaArray
    lua.execute("""SwipeStatePlayer =  {
            instance = function() return True end,
            }""")
    lua.execute("""getPerformance = function() return {
            getSupports3D = function() return True end,
            getModelsEnabled = function() return True end,
            setModelsEnabled = function() end,
            getModels = function() return 8 end,
            setModels = function() end,
            getCorpses3D = function() return True end,
            setCorpses3D = function() end,
            getFramerate = function() return 0 end,
            getLightingQuality = function() return 1 end,
            } end""")

    lua.globals().loadStaticZomboidModel = nullFunc
    lua.globals().getDebug = getDebug
    lua.globals().ZombRand = ZombRand
    lua.globals().ZombRandFloat = ZombRandFloat
    lua.globals().isDemo = isDemo
    lua.globals().isClient = isClient
    lua.globals().isServer = isServer
    lua.globals().getTexture = getTexture
    lua.globals().getTextManager = getTextManager
    lua.globals().getSteamModeActive = getSteamModeActive
    lua.globals().getModInfoByID = getModInfoByID
    lua.globals().getText = TranslationManager.getText
    lua.globals().getTextOrNull = TranslationManager.getTextOrNull
    lua.globals().Translator = TranslationManager
    lua.globals().getSandboxOptions = getSandboxOptions
    lua.globals().ScriptManager = ScriptManager
    lua.globals().getScriptManager = getScriptManager
    lua.globals().triggerEvent = triggerEvent
    lua.globals().transformIntoKahluaTable = transformIntoKahluaTable
    lua.globals().getFileReader = getFileReader
    lua.globals().getCore = getCore
    lua.globals().instanceof = instanceof
    lua.globals().getPlayer = getPlayer
    lua.globals().getSpecificPlayer = getSpecificPlayer
    lua.globals().getNumActivePlayers = getNumActivePlayers
