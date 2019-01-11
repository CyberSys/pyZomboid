#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 08:25:25 2018

@author: Fenris_Wolf
"""

import re
import os
import GameManager
LoadedScripts = []
ModuleMap = { }
#LINESPLIT_DEFAULT = re.compile("\W*=\W*")
LINESPLIT_DEFAULT = re.compile("[\t ]*=[\t ]*")


class ScriptManager(object):
    def __init__(self):
        pass
    def FindItem(self, fullType):
        try:
            module, itemType = fullType.split('.',1)
            item = Item(module, itemType, ModuleMap[module].items[itemType])
            item.module = module
            item.type = itemType
        except ValueError:
            return None
        except KeyError:
            return None
        return item
instance = ScriptManager()

class Block(list):
    def __init__(self, type, name, data):
        list.__init__(self, data)
        self.type = type
        self.name = name
        self.data = data


class Module(object):
    def __init__(self, name):
        self.name = name
        self.items = { }
        self.recipes = []
        ModuleMap[name] = self



class Item(object):
    def __init__(self, module, type, elements):
        self.elements = elements
        self.data = {}
        for k, v in elements:
            self.data[k] = v
        self.module = module
        self.type = type
    def getDisplayName(self):
        import TranslationManager
        result = self.data.get("DisplayName")

        return TranslationManager.Text.get("DisplayName_%s" % result, result)

    def getAmmoType(self):
        return self.data.get("AmmoType")
    def getSwingSound(self):
        return self.data.get("SwingSound")
    def getCount(self):
        return self.data.get("Count", 1)
    def getActualWeight(self):
        return self.data.get("Weight", 0.1)


class Script(object):
    path = None
    def __init__(self, filename, path):
        self.filename = filename
        self.path = path

        thisFile = open(path + '/'+ filename)
        self.lines = thisFile.read()
        thisFile.close()
        self.lines = re.sub('/\*.*?\*/', '', self.lines, flags=re.DOTALL)
        #lines = [x.strip() for x in lines]
        self.blocks = self.getTokens(self.lines)
        LoadedScripts.append(self)

        for block in self.blocks:
            if block.type != 'module':
                continue
            if not ModuleMap.has_key(block.name):
                ModuleMap[block.name] = Module(block.name)
            for block2 in block.data:
                if block2.type == 'item':
                    ModuleMap[block.name].items[block2.name] = block2.data

    def getTokens(self, lines):
        #lines = self.lines
        tokens = []
        depth,nextOpen,nextClosed = 0,0,0
        while True:
            depth,nextOpen,nextClosed = 0,0,0
            if lines.find("}", nextOpen+1) == -1:
                break
            while True:
                nextOpen = lines.find("{", nextOpen + 1)
                nextClosed = lines.find("}", nextClosed + 1)
                if (((nextClosed < nextOpen) and (nextClosed != -1)) or (nextOpen == -1)):
                    nextOpen = nextClosed
                    depth -= 1
                elif (nextOpen != -1):
                    nextClosed = nextOpen
                    depth += 1
                if depth <= 0:
                    break
            tokens.append(lines[0:nextOpen+1])
            lines = lines[nextOpen+1:]
        result = []
        for x in tokens:
            result.append(self.parseToken(x))
        lines = lines.strip()
        if len(lines) > 0:
            for line in re.split(",", lines):
                line = line.strip()
                if len(line) > 0:
                    result.append(LINESPLIT_DEFAULT.split(line))
        #self.tokens = result
        return result

    def parseToken(self, token):
        token = token.strip()
        firstopen = token.find("{")
        lastClose = token.rfind("}")
        points = re.split("[{}]", token)
        header = points[0]
        header = header.strip()
        try:
            tokType, name = re.split("\W+", header, 1)
        except ValueError:
            tokType, name = header, None
        text = token[firstopen + 1: lastClose].strip()
        result = self.getTokens(text)
        return Block(tokType, name, result)



def init():
    # TODO: load default scripts...
    for name, mod in GameManager.ActiveMods.items():
        print mod.dir+"/media/scripts"
        for filename in [x for x in os.walk(mod.dir+"media/scripts")][0][2]:
            print filename, mod.dir+"media/scripts"
            Script(filename, mod.dir+"media/scripts")
#==============================================================================
#
# def printToken(token, depth=0):
#     print "  "*depth +"Type:", token.type + (token.name and ", Name: " + token.name or "")
#     print "  "*depth +"Data:"
#     for d in token.data:
#         if isinstance(d, Block):
#             printToken(d, depth+1)
#         else:
#             #print "    "*depth +str(d)
#             pass
#     print
#
#
# def parse2(text):
#     oIndexes = [ ]
#     pos = 0
#     for i in range(text.count("{")):
#         oIndexes.append(text.index("{", pos))
#         pos = 1 + oIndexes[-1]
#     print oIndexes
#
#     cIndexes = [ ]
#     pos = 0
#     for i in range(text.count("}")):
#         cIndexes.append(text.index("}", pos))
#         pos = 1 + cIndexes[-1]
#     print cIndexes
#     for o in oIndexes:
#         for c in cIndexes:
#             pass
# testscript = """
# module Base
# {
#         import
#         {
#             X,
#         }
#         item Test
#         {
#             weight = 40,
#             type = normal,
#         }
# }
# module Base2
# {
#         import
#         {
#             Y,
#         }
#         item Test2
#         {
#             weight = 40,
#             type = normal,
#         }
# }
# """
#
#==============================================================================
#parse2(testscript)
