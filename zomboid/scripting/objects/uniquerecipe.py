# -*- coding: utf-8 -*-
import re
from zomboid.java import ArrayList
from .base import BaseScriptObject 


class UniqueRecipe(BaseScriptObject):
    name : str = None
    baseRecipe : str = None
    items : ArrayList = None
    hungerBonus : int = 0
    hapinessBonus : int = 0 # not a typo. least not by me
    boredomBonus : int = 0
    
    def __init__(self, name : str):
        self.name = name
        self.items = ArrayList()

    def Load(self, name, data : list) -> None:
        for line in data:
            line = line.strip()
            if not line:
                continue
            
            match = re.match(r"([^:]+)\s*:\s*(.+)\s*", line, flags=re.DOTALL | re.M)
            if not match:
                continue

            key, value = match.groups()
            if key == 'baseRecipe':
                self.baseRecipe = value

            elif key == 'Item':
                self.items.add(value)

            elif key == 'Hunger':
                self.hungerBonus = int(value)

            elif key == 'Hapiness':
                self.hapinessBonus = int(value)

            elif key == 'Boredom':
                self.boredomBonus = int(value)


    def getName(self) -> str:
        return self.name


    def setName(self, name : str) -> None:
        self.name = name


    def getBaseRecipe(self) -> str:
        return self.baseRecipe


    def setBaseRecipe(self, value : str) -> None:
        self.baseRecipe = value


    def getHungerBonus(self) -> int:
        return self.hungerBonus


    def setHungerBonus(self, value : int) -> None:
        self.hungerBonus = value


    def getHapinessBonus(self) -> int:
        return self.hapinessBonus


    def setHapinessBonus(self, value : int) -> None:
        self.hapinessBonus = value


    def getBoredomBonus(self) -> int:
        return self.boredomBonus


    def setBoredomBonus(self, value : int) -> None:
        self.boredomBonus = value


