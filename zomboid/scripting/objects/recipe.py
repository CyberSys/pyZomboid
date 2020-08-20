""" python port of zombie/scripting/objects/Recipe.class

    Original code copyright TheIndieStone.
    python port by Fenris_Wolf

"""
import re
from zomboid.java import ArrayList, HashMap
from .base import BaseScriptObject 

class Result:
    type : str = None
    count : int = 1
    drainableCount : int = 0
    module : str = None

    def getType(self) -> str:
        return self.type
    
    def getCount(self) -> int:
        return self.count

    def getModule(self) -> str:
        return self.module

    def getFullType(self) -> str:
        return f"{self.module}.{self.type}"

    def getDrainableCount(self) -> int:
        return self.drainableCount


class Source:
    keep : bool = False
    items : ArrayList = None
    destroy : bool = False
    count : float = 1
    use : float = 0

    def __init__(self):
        self.items = ArrayList()

    def isDestroy(self) -> bool:
        return self.destroy

    def isKeep(self) -> bool:
        return self.keep

    def getCount(self) -> int:
        return self.count

    def getUse(self) -> int:
        return self.use

    def getItems(self) -> ArrayList:
        return self.items


class Recipe(BaseScriptObject):
    canBeDoneFromFloor : bool = False
    AnimNode : str = None
    Prop1 : str = None
    Prop2 : str = None
    TimeToMake : float = 0.0
    Sound : str = None
    LuaTest : str = None
    LuaCreate : str = None
    LuaGrab : str = None
    NeedToBeLearn : bool = False # this field is actually needToBeLearn, but theres also a method by this exact name....
    removeResultItem : bool = False
    skillRequired : HashMap = None
    heat : float = 0.0
    NoBrokenItems : bool = False # this field is actually NoBrokenItems, but theres also a method by this exact name....
    name : str = 'recipe'
    originalname : str = 'recipe'
    Result : Result = None
    Source : ArrayList = None
    nearItem : str = None

    def __init__(self):
        super().__init__()
        self.Source = ArrayList()


    def setCanBeDoneFromFloor(self, value : bool) -> None:
        self.canBeDoneFromFloor = value


    def isCanBeDoneFromFloor(self) -> bool:
        return self.canBeDoneFromFloor
    

    def FindIndexOf(self, item : str) -> int:
        return -1


    def getSource(self) -> Source:
        return self.Source


    def getNumberOfNeededItems(self) -> int:
        count = 0
        for source in self.Source:
            if source.items:
                count += source.count

        return count


    def getTimeToMake(self) -> float:
        return self.TimeToMake


    def getName(self) -> str:
        return self.name


    def getFullType(self) -> str:
        return f"{self.module}.{self.originalname}"


    def Load(self, name : str, data : list) -> None:
        self.name = name # TODO: Translator.getRecipeName
        self.originalname = name
        override = False
        for line in data:
            line = line.strip()
            if not line:
                continue

            match = re.match(r"([^:]+)\s*:\s*(.+)\s*", line, flags=re.DOTALL | re.M)
            if not match:
                self.DoSource(line)

            else:
                key, value = match.groups()
                #key = key.lower() # NOTE ALL THESE KEYS ARE ACTUALLY CASE_SENSITIVE!!!!
                value = value.strip()
                if key == "Override":
                    override = value.lower() == 'true'

                elif key == "AnimNode":
                    self.AnimNode = value

                elif key == "Prop1":
                    self.Prop1 = value

                elif key == "Prop2":
                    self.Prop2 = value

                elif key == "Time":
                    self.TimeToMake = float(value)

                elif key == "Sound":
                    self.Sound = value

                elif key == "Result":
                    self.DoResult(value)

                elif key == "OnTest":
                    self.LuaTest = value

                elif key == "OnCreate":
                    self.LuaCreate = value

                elif key == "OnGrab":
                    self.LuaGrab = value

                elif key.lower() == "needtobelearn": # case insensitive
                    self.setNeedToBeLearn(value.lower() == 'true')

                elif key.lower() == "category": # case insensitive
                    self.setCategory(value)

                elif key == "RemoveResultItem":
                    self.removeResultItem = value.lower() == 'true'

                elif key == "CanBeDoneFromFloor":
                    self.setCanBeDoneFromFloor(value.lower() == 'true')

                elif key == "NearItem":
                    self.setNearItem(value)

                elif key == "SkillRequired":
                    self.skillRequired = HashMap()
                    skills = value.split(";")
                    for sk in skills:
                        if not sk:
                            continue
                        sk, val = sk.split("=",1)
                        self.skillRequired[sk] = int(val)

                elif key == "OnGiveXP":
                    self.OnGiveXP = value

                elif key == "Obsolete":
                    if value.lower() == "true":
                        self.module.RecipeMap.remove(self)
                        self.module.RecipesWithDotInName.remove(self)
                        return

                elif key == "Heat":
                    self.heat = float(value)

                elif key == "NoBrokenItems":
                    self.NoBrokenItems = value.lower() == 'true'

        if override:
            recipe = self.module.getRecipe(name)
            if recipe and recipe != self:
                self.module.RecipeMap.remove(self)
                self.module.RecipesWithDotInName.remove(self)
        
        return


    def DoSource(self, data : str) -> None:
        source = Source()
        if '=' in data:
            data, count = data.split('=')
            data, count = data.strip(), float(count.strip())
            source.count = count
        
        if data.startswith("keep"):
            data = data[5:]
            source.keep = True

        if ";" in data:
            data, count = data.split(';')
            source.use = float(count)

        if data.startswith("destroy"):
            data = data[8:]
            source.destroy = True

        if data == 'null':
            source.items.clear()

        elif '/' in data:
            for i in data.split('/'):
                source.items.add(i)

        else:
            source.items.add(data)

        if data:
            self.Source.add(source)


    def DoResult(self, data : str) -> None:
        result = Result()
        if '=' in data:
            data, count = data.split('=')
            data, count = data.strip(), int(count.strip())
            result.count = count

        if ";" in data:
            data, count = data.split(';')
            data, count = data.strip(), int(count.strip())
            result.drainableCount = count

        if '.' in data:
            result.module, result.type = data.split('.')
        else:
            result.type = data
        
        self.Result = result


    def getResult(self) -> Result:
        return self.Result

    def getSound(self) -> str:
        return self.Sound

    def getOriginalName(self) -> str:
        return self.originalname

    def setOriginalName(self, value : str) -> None:
        self.originalname = value

    def needToBeLearn(self) -> bool:
        return self.NeedToBeLearn

    def setNeedToBeLearn(self, value : bool) -> None:
        self.NeedToBeLearn = value

    def getCategory(self) -> str:
        return self.category

    def setCategory(self, value : str) -> None:
        self.category = value

    def getRequiredSkills(self) -> None:
        skills = []
        if self.skillRequired:
            for sk in self.skillRequired:
                # TODO: we need to get the perk from string from PerkFactory
                #str2 = (PerkFactory.getPerk(PerkFactory.Perks.FromString(str1))).name + " " + + this.skillRequired.get(str1);
                skills.append("%s %s" % (sk, self.skillRequired[sk]))
        
        return ArrayList(*skills)


    def findSource(self, item : str) -> Source:
        for source in self.Source:
            if item in source.items:
                return source

        return None


    def isDestroy(self, item : str) -> Source:
        try:
            source = self.findSource(item)
            return source.destroy

        except AttributeError: # Todo: should raise a specific exception
            raise


    def isKeep(self, item : str) -> Source:
        try:
            source = self.findSource(item)
            return source.keep

        except AttributeError: # Todo: should raise a specific exception
            raise

    def getHeat(self) -> float:
        return self.heat

    def noBrokenItems(self) -> bool:
        return self.NoBrokenItems

    def getWaterAmountNeeded(self) -> int:
        source = self.findSource("Water")
        if not source:
            return 0

        return source.count

    def getNearItem(self) -> str:
        return self.nearItem

    def setNearItem(self, value : str) -> None:
        self.nearItem = value

    def isRemoveResultItem(self) -> bool:
        return self.removeResultItem

    def setRemoveResultItem(self, value : bool) -> None:
        self.removeResultItem = value

    def getAnimNode(self) -> str:
        return self.AnimNode

    def setAnimNode(self, value : str) -> None:
        self.AnimNode = value

    def getProp1(self) -> str:
        return self.Prop1

    def setProp1(self, value : str) -> None:
        self.Prop1 = value

    def getProp2(self) -> str:
        return self.Prop2

    def setProp2(self, value : str) -> None:
        self.Prop2 = value

