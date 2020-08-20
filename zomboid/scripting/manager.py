#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:04:21 2020

@author: wolf
"""
import logging
import re

logger = logging.getLogger(__name__)

RE_MODULE = re.compile(r"module\s+([^{]+?)\s*{(.*)}", flags=re.DOTALL | re.M)

from .module import ScriptModule, ModuleMap
from .parser import ScriptParser


class ScriptManager:

    @classmethod
    def FindItem(cls, full_type):
        try:
            module, item_type = full_type.split('.',1)
            return ModuleMap[module].items[item_type]

        except KeyError:
            return None

        return None


    @classmethod
    def ParseScript(cls, lines):
        tokens = ScriptParser.parseTokens(lines)
        for token in tokens:
            cls.CreateFromToken(token)

        
    @classmethod
    def LoadFile(cls, filename, boolean):
        this = open(filename)
        lines = this.read()
        this.close()
        lines = ScriptParser.stripComments(lines)
        cls.ParseScript(lines)


    @classmethod
    def CreateFromToken(cls, data):
        match = RE_MODULE.match(data)
        if not match:
            return
        module_name = match.group(1)
        data = match.group(2)
        if module_name not in ModuleMap:
            logger.debug("Adding new module: %s", module_name)
            ModuleMap[module_name] = ScriptModule()

        ModuleMap[module_name].Load(module_name, data)


instance = ScriptManager()
