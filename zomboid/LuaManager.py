#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 08:01:36 2018

@author: Fenris_Wolf
"""
import os
import settings
import lupa
instance = None
import GameManager

def loadFolderLua(folder, root=None):
    Queue = []
    if root is None:
        root = settings.pzdir
    path = root + 'media/lua/'+folder
    olddir = os.getcwd()
    os.chdir(root + "media/lua")

    for data in os.walk(path):
        d = data[0].replace(path, '')
        if d.startswith('/'):
            d = d[1:]
        for fi in data[2]:
            if fi and fi.endswith(".lua"):
                fi = fi[0:-4]
                Queue.append(d and d+ "/" +fi or fi)
    Queue.sort()
    for filename in Queue:
        print "Loading", folder+"/"+ filename +".lua"
        instance.execute('require "%s"' % filename)
    os.chdir(olddir)

def loadModLua(mod, folder):
    global instance
    print "*** Loading Mod:", mod, folder, "files"
    loadFolderLua(folder, settings.cache + "mods/%s/" % mod)

def loadSharedLua():
    print "*** Loading Shared Lua..."
    loadFolderLua('shared')
    for name, mod in GameManager.ActiveMods.items():
        loadFolderLua('shared', mod.dir)

def loadClientLua():
    print "*** Loading Client Lua..."
    loadFolderLua('client')
    for name, mod in GameManager.ActiveMods.items():
        loadFolderLua('client', mod.dir)

def loadServerLua():
    print "*** Loading Server Lua..."
    loadFolderLua('server')
    for name, mod in GameManager.ActiveMods.items():
        loadFolderLua('server', mod.dir)


def init():
    global instance
    # delayed imports
    import Globals
    import EventManager
    import Inventory
    import javaclass
    import ProfessionFactory
    import TraitFactory
    import Perks
    #os.chdir(settings.pzdir + "media/lua")
    instance = lupa.LuaRuntime(unpack_returned_tuples=True)
    _G = instance.globals()
    _G.package.path = './server/?.lua;./client/?.lua;./shared/?.lua;' + _G.package.path

    EventManager.init(instance)

    Globals.init(instance)

    ServerOptions = instance.eval('{ }')
    ServerOptions.new = javaclass.ServerOptions

    _G.ServerOptions = ServerOptions
    _G.LuaEventManager = EventManager
    _G.InventoryItemFactory = Inventory
    _G.TraitFactory = TraitFactory
    _G.Perks = Perks
    _G.PerkFactory = Perks
    _G.ProfessionFactory = ProfessionFactory
