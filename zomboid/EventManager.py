#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:24:28 2018

@author: Fenris_Wolf
"""
_eventnames = [
    "OnJoypadActivate",
    "OnJoypadActivateUI",
    "OnRenderTick",
    'OnDeviceText',
    "OnGameStart",
    "OnGameBoot",

    "OnCoopJoinFailed",
    "OnCreateSurvivor",
    "OnPlayerUpdate",
    "OnWeaponSwingHitPoint",

    "OnLoadSoundBanks",

    "OnServerStarted",
    "OnGameTimeLoaded",
    "OnAddBuilding",
    "OnNewSurvivorGroup",
    "OnFillWorldObjectContextMenu",
    "OnTick",
    "OnPostSave",
    "EveryTenMinutes",
    "OnNewGame",
    "OnAdminMessage",
    "OnSafehousesChanged",
    'ViewTickets',
    'OnScoreboardUpdate',
    'OnMiniScoreboardUpdate',
    'OnGetTableResult',
    'OnGetDBSchema',
    'OnCustomUIKey',
    'OnKeyPressed',
    'OnContainerUpdate',
    'OnPlayerDeath',
    'OnServerStartSaving',
    'OnServerFinishSaving',
    'RequestTrade',
    'AcceptedTrade',
    'TradingUIAddItem',
    'TradingUIRemoveItem',
    'TradingUIUpdateState',
    'OnKeyStartPressed',
    'OnCreatePlayer',
    'OnResolutionChange',
    'MngInvReceiveItems',
    'OnReceiveUserlog',
    'SyncFaction',
    'ReceiveFactionInvite',
    'AcceptedFactionInvite',
    'OnChallengeQuery',
    'OnInitWorld',
    'OnLoginState',
    'OnLoginStateSuccess',
    'OnMainMenuEnter',
    'OnResetLua',
    'OnAcceptInvite',
    'OnSteamGameJoin',
    'OnDisconnect',
    'OnConnected',
    'OnConnectFailed',
    'ServerPinged',
    'OnConnectionStateChanged',
    'OnEquipPrimary',
    'OnEquipSecondary',
    'OnKeyKeepPressed',
    'OnPostUIDraw',
    'OnEnterVehicle',
    'OnMechanicActionDone',
    'OnClothingUpdated',
    'OnFillInventoryObjectContextMenu',
    'OnFillContainer',

    'OnDoTileBuilding2',
    'OnDoTileBuilding3',
    'OnDestroyIsoThumpable',
    'OnWaterAmountChange',
    'OnClientCommand',
    'OnObjectAdded',
    'OnRightMouseDown',
    'DoSpecialTooltip',
    'OnServerCommand',
    'OnObjectLeftMouseButtonUp',
    'OnObjectLeftMouseButtonUp',
    'OnObjectLeftMouseButtonDown',
    'OnObjectRightMouseButtonUp',
    'OnObjectRightMouseButtonDown',
    'OnPreDistributionMerge',
    'OnDistributionMerge',
    'OnPostDistributionMerge',
    'OnTriggerNPCEvent',
    'OnMultiTriggerNPCEvent',
    'OnPlayerSetSafehouse',
    'SendCustomModData',
    'EveryDays',
    'EveryHours',
    'OnPlayerMove',
    'OnWeaponHitTree',
    'AddXP',
    'LevelPerk',
    'OnCreateUI',
    'OnLoadMapZones',


    'OnCGlobalObjectSystemInit',
    'OnChatWindowInit',
    'OnObjectAboutToBeRemoved',
    'OnSGlobalObjectSystemInit',

    'OnClimateManagerInit',
]

_hooknames = ['Attack']

Events = None
class Event(object):
    def __init__(self, name):
        self.name = name
        self.queue = []
    def Add(self, callback):
        #print "Adding Event to", self.name
        self.queue.append(callback)
    def Remove(self, callback):
        pass
    def Trigger(self, *args):
        print "Triggering Event " + self.name
        for func in self.queue:
            func(*args)


def init(lua):
    global Events
    lua.execute("Events = { }; Hook = { };")
    Events = lua.globals().Events
    for x in _eventnames:
        Events[x] = Event(x)
    #_ehandler = lua.eval("function (name, value) Events[name] = value end")
    #[_ehandler(x, Event(x)) for x in _eventnames]

    Hook = lua.globals().Hook
    for x in _hooknames:
        Hook[x] = Event(x)


def AddEvent(event):
    print 'Adding Unknown Event:', event
    #ehandler = lua.eval("function (name, value) Events[name] = value end")
    #_ehandler(event, Event(event))
    Events[event] = Event(event)

def Trigger(event, *args):
    Events[event].Trigger(*args)
