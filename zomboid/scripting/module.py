# -*- coding: utf-8 -*-
import logging
from zomboid.java import ArrayList, HashMap

from .parser import ScriptParser
from .objects import Item, Recipe, Fixing, ModelScript, GameSoundScript, VehicleScript, UniqueRecipe, EvolvedRecipe 
#from .objects.item import Item
#from .objects.recipe import Recipe
import re
RE_HEADER = re.compile(r"([^\s]+)\s+([\S][^{]*?)?\s*{(.*)}", flags=re.DOTALL | re.M)

logger = logging.getLogger(__name__)
ModuleMap = { }

class ScriptModule:
    name : str = None
    value : str = None
    Imports : ArrayList = None
    ItemMap : HashMap = None
    ModelScriptMap : HashMap = None
    GameSoundMap : HashMap = None
    GameSoundList : ArrayList = None
    RecipeMap : ArrayList = None
    RecipesWithDotInName : HashMap = None
    UniqueRecipeMap : ArrayList = None
    EvolvedRecipe : ArrayList = None
    FixingMap : HashMap = None
    
    def __init__(self):
        self.Imports = ArrayList()
        self.ItemMap = HashMap()
        self.ModelScriptMap = HashMap()
        self.GameSoundMap = HashMap()
        self.GameSoundList = ArrayList()
        self.RecipeMap = ArrayList()
        self.RecipesWithDotInName = HashMap()
        self.UniqueRecipeMap = ArrayList()
        self.EvolvedRecipe = ArrayList()
        self.FixingMap = HashMap()


    def Load(self, name : str, data : str) -> None:
        self.name = name
        self.value = data
        self.ParseScriptPP(self.value)
        self.ParseScript(self.value)
        self.value = ""


    def ParseScriptPP(self, data : str) -> None:
        tokens = ScriptParser.parseTokens(data)
        for token in tokens:
            self.CreateFromTokenPP(token)


    def ParseScript(self, data : str) -> None:
        tokens = ScriptParser.parseTokens(data)
        for token in tokens:
            self.CreateFromToken(token)


    def CreateFromTokenPP(self, data : str) -> None:
        data = data.strip()
        match = RE_HEADER.match(data)
        if not match:
            return

        key, name, data = match.groups()
        if key == "item":
            self.ItemMap[name] = Item()

        elif key == "model": 
            if name in self.ModelScriptMap:
                self.ModelScriptMap[name].reset()
            else:
                self.ModelScriptMap[name] = ModelScript()

        elif key == "sound":
            if name in self.GameSoundMap:
                self.GameSoundMap[name].reset()
            else:
                self.GameSoundMap[name] = GameSoundScript()
                self.GameSoundList.add(self.GameSoundMap[name])

        elif key == "vehicle":
            self.VehicleMap[name] = VehicleScript()

        elif key == "template":
            pass


    def CreateFromToken(self, data : str) -> None:
        data = data.strip()
        match = RE_HEADER.match(data)
        if not match:
            return

        key, name, block_data = match.groups()
        this = None
        block_data = block_data.split(",")
        if key == "imports":
            self.Imports += [s.strip() for s in block_data if s.strip()] # todo: check for self importing

        elif key == "item":
            this = self.ItemMap[name]

        elif key == "recipe":
            this = Recipe()
            self.RecipeMap.add(this)
            if '.' in name:
                self.RecipesWithDotInName[name] = this

        elif key == "uniquerecipe":
            this = UniqueRecipe(name)
            self.UniqueRecipeMap.add(this)

        elif key == "evolvedrecipe":
            this = [r for r in self.EvolvedRecipeMap if r.name == name]
            if this:
                this = this[0]

            else:
                this = EvolvedRecipe(name)

        elif key == "fixing":
            this = Fixing()

        elif key == "multistagebuild":
            pass # TODO: MultiStageBuilding stuff
            #(new MultiStageBuilding()).getClass(); 
            #MultiStageBuilding.Stage stage = new MultiStageBuilding.Stage(new MultiStageBuilding());
            #stage.Load(str, arrayOfString2);
            #MultiStageBuilding.addStage(stage);
      
        elif key == "model":
            this = self.ModelScriptMap[name]
            block_data = data

        elif key == "sound":
            this = self.GameSoundMap[name]
            block_data = data#match.group(3)#

        elif key == "vehicle":
            this = self.VehicleMap[name]
            block_data = data

        if not this:
            return

        # Load the object
        this.module = self
        this.Load(name, block_data)

