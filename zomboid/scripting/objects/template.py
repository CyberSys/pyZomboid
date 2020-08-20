# -*- coding: utf-8 -*-
from .base import BaseScriptObject
from .vehicle import VehicleScript

class VehicleTemplate(BaseScriptObject):
    name : str = None
    body : str = None
    script : VehicleScript = None
    
    def __init__(self, module, name : str, data : str): # cant use hints due to import recursion. ..module.ScriptModue
        from ..manager import instance
        if instance.currentFileName not in instance.scriptsWithVehicleTemplates:
            instance.scriptsWithVehicleTemplates.add(instance.currentFileName);

        self.module = module
        self.name = name
        self.body = data


    def getScript(self):
        if self.script is None:
            self.script = VehicleScript()
            self.script.module = self.module
            self.script.Load(self.name, self.body)

        return self.script

