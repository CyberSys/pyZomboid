#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 09:53:48 2018

@author: Fenris_Wolf
"""
class ConfigOption(object):
    def __init__(self):
        pass
    def getTooltip(self):
        return ""
    def getType(self):
        return 'string'
    def getValueAsString(self):
        return 'string'
    def getName(self):
        return 'string'

    def getTranslatedName(self):
        return 'string'
    def getValue(self):
        return 'string'

class ServerOption(object):
    def __init__(self):
        pass
    def asConfigOption(self):
        return ConfigOption()

class ServerOptions(object):
    def __init__(self, args):
        pass

    def getNumOptions(self):
        return 0
    def getOptionByName(self, name):
        return ServerOption()

class SandboxOptions(object):
    def __init__(self):
        pass

    def getNumOptions(self):
        return 0
    def getOptionByName(self, name):
        return ConfigOption()

class Font(object):
    def __init__(self):
        pass

    def getLineHeight(self):
        return 10

class TextManager(object):
    def __init__(self):
        pass

    def getFontHeight(self, font):
        return 10
    def getFontFromEnum(self, font):
        return Font()
    def MeasureStringX(self, text, font):
        return 5
    def MeasureStringY(self, text, font):
        return 5

class JavaArray(object):
    def __init__(self,data=None):
        if data is None:
            data = []
        self.data = data
    def add(self, value):
        self.data.append(value)
    def remove(self, value):
        self.data.remove(value)
    def get(self, index):
        return self.data[index]
    def size(self):
        return len(self.data)
    def contains(self, value):
        return (value in self.data)
    def isEmpty(self):
        return len(self.data) > 0

class BufferedReader(object):
    def __init__(self, path):
        self.io = open(path)
    def readLine(self):
        self.io.readline()
    def close(self):
        self.io.close()

class Color(object):
    def __init__(self, r=0, g=0, b=0, a=0):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
    def getR(self):
        return self.r
    def getG(self):
        return self.g
    def getB(self):
        return self.b
    def getA(self):
        return self.a

class UITransition(object):
    def __init__(self):
        pass

class UIElement(object):
    def __init__(self, luaObject):
        self.luaObject = luaObject
        self.x = 0
        self.y = 0
        self.h = 0
        self.w = 0
        self.scrollHeight = 0
    def setX(self, x):
        self.x = x
    def getX(self):
        return self.x
    def setY(self, x):
        self.y = x
    def getY(self):
        return self.y

    def setHeight(self, x):
        self.h = x
    def getHeight(self):
        return self.h
    def setWidth(self, x):
        self.w = x
    def getWidth(self):
        return self.w
    def setAnchorLeft(self, x):
        pass
    def setAnchorRight(self, x):
        pass
    def setAnchorTop(self, x):
        pass
    def setAnchorBottom(self, x):
        pass

    def AddChild(self, *args):
        pass
    def setVisible(self, *args):
        pass
    def onResize(self, *args):
        pass
    def ignoreWidthChange(self, *args):
        pass
    def ignoreHeightChange(self, *args):
        pass
    def setScrollChildren(self, *args):
        pass
    def setScrollWithParent(self, *args):
        pass
    def getYScroll(self):
        return 0
    def setYScroll(self, value):
        return 0
    def getScrollHeight(self):
        return self.scrollHeight
    def setScrollHeight(self, value):
        self.scrollHeight = value
    def setAlwaysOnTop(self, *args):
        return
    def setCapture(self, *args):
        return
