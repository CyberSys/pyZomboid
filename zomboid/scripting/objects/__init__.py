# -*- coding: utf-8 -*-

import re
from .base import BaseScriptObject
from .item import Item
from .model import ModelScript
from .recipe import Recipe
from .uniquerecipe import UniqueRecipe
from .fixing import Fixing
from .sound import GameSoundScript
from .vehicle import VehicleScript
from .template import VehicleTemplate



LINESPLIT_DEFAULT = re.compile("[\t ]*=[\t ]*")


class EvolvedRecipe(BaseScriptObject):
    pass

class MultiStageBuilding(BaseScriptObject):
    pass




