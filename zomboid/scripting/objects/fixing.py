import re
from zomboid.java import ArrayList, LinkedList
from .base import BaseScriptObject 

InventoryItem, IsoGameCharacter = None, None # TODO: replace and finishs methods below.

class Fixer:
    fixerName : str = None
    skills : LinkedList = None
    numberOfUse : int = 1
    
    def __init__(self, name : str, skills : LinkedList, uses : int):
        self.fixerName = name
        self.skills = skills
        self.numberOfUse = uses

    def getFixerName(self) -> str:
        return self.fixerName

    def getNumberOfUse(self) -> int:
        return self.numberOfUse

    def getFixerSkills(self) -> LinkedList:
        return self.skills


class FixerSkill:
    skillName : str = None
    skillLvl : int = 0
    
    def __init__(self, name : str, level : int):
        self.skillName = name
        self.skillLvl = level

    def getSkillName(self) -> str:
        return self.skillName

    def getSkillLvl(self) -> int:
        return self.skillLvl


class Fixing(BaseScriptObject):
    Fixer = Fixer # just to match the java structure
    FixerSkill = FixerSkill # just to match the java structure
    name : str = None
    require : ArrayList = None
    fixers : LinkedList = None
    globalItem : Fixer = None
    conditionModifier : float = 1.0

    def Load(self, name : str, data : list):
        self.name = name
        for line in data:
            line = line.strip()

            match = re.match(r"^\s*(\S+)\s*:\s*(.+?)\s*$", line)
            if not match:
                continue

            key, value = match.groups()
            if key == "Require":
                for item in value.split(';'):
                    if not item:
                        continue

                    self.addRequiredItem(item.strip())

            elif key == "Fixer":
                if ';' in value:
                    linked = LinkedList()
                    for entry in value.split(';'):
                        if not item:
                            continue

                        item, count = entry.strip().split('=', 1)
                        linked.add(Fixer(item, None, int(count)))

                    if '=' in value.split(";")[0]:
                        item, count = value.split(";")[0].split('=', 1)
                        self.fixers.add(Fixer(item, linked, int(count)))

                    else:
                        self.fixers.add(Fixer(item, linked, 1))

                elif '=' in value:
                    item, count = value.split('=', 1)
                    self.fixers.add(Fixer(item, None, int(count)))

                else:
                    self.fixers.add(Fixer(value, None, 1))
                    

            elif key == "GlobalItem":
                if '=' in value:
                    item, count = value.split('=', 1)
                    self.globalItem = Fixer(item, None, int(count))

                else:
                    self.globalItem = Fixer(value, None, 1)

            elif key == "ConditionModifier":
                self.conditionModifier = float(value)


    def getName(self) -> str:
        return self.name


    def setName(self, name : str) -> None:
        self.name = name


    def addRequiredItem(self, item : str) -> None:
        if self.require is None:
            self.require = ArrayList()

        if item:
            self.require.add(item)


    def getFixers(self) -> LinkedList:
        return self.fixers


    def getGlobalItem(self) -> Fixer:
        return self.globalItem


    def setGlobalItem(self, item : Fixer) -> None:
        self.globalItem = item


    def getConditionModifier(self) -> float:
        return self.conditionModifier


    def setConditionModifier(self, value : float) -> None:
        self.conditionModifier = value

    def usedInFixer(self, item : InventoryItem, character : IsoGameCharacter) -> Fixer:
        raise NotImplementedError


    def haveGlobalItem(self, character : IsoGameCharacter) -> InventoryItem:
        raise NotImplementedError


    def haveThisFixer(self, character : IsoGameCharacter, fixer : Fixer, item : InventoryItem) -> InventoryItem:
        raise NotImplementedError


    def countUses(self, character : IsoGameCharacter, fixer : Fixer, item : InventoryItem) -> int:
        raise NotImplementedError


        