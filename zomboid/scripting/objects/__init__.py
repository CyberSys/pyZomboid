# -*- coding: utf-8 -*-

import re
from zomboid.java import Enum
from .base import BaseScriptObject
from .item import Item
from .recipe import Recipe
from .uniquerecipe import UniqueRecipe
from .fixing import Fixing
from .sound import GameSoundScript


class Type(Enum):
    Normal = 0
    Weapon = 1
    Food = 2
    Literature = 3
    Drainable = 4
    Clothing = 5
    Container = 6
    WeaponPart = 7
    Key = 8
    KeyRing = 9
    Moveable = 10
    Radio = 11
    AlarmClock = 12
    AlarmClockClothing = 13


LINESPLIT_DEFAULT = re.compile("[\t ]*=[\t ]*")


class EvolvedRecipe(BaseScriptObject):
    pass

class MultiStageBuilding(BaseScriptObject):
    pass

class ModelScript(BaseScriptObject):
    def reset(self):
        pass


class VehicleScript(BaseScriptObject):
    pass



