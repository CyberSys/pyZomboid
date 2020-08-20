# -*- coding: utf-8 -*-

from zomboid.java import ArrayList
s_activeMods = ArrayList() # shared
s_loaded = None # set at bottom.
class ActiveMods:
    #s_activeMods : ArrayList = ArrayList() # shared
    #s_loaded : ActiveMods = ActiveMods('loaded') # shared

    id : str = None
    mods : ArrayList = None

    def __init__(self, id : str):
        self.requireValidId(id)
        self.id = id
        self.mods = ArrayList()
        self.mapOrder = ArrayList()


    @classmethod
    def count(cls) -> int:
        return len(s_activeMods)

    @classmethod
    def getByIndex(cls, index : int): #->ActiveMods
        return s_activeMods[index]

    @classmethod
    def getById(cls, id : str): #->ActiveMods
        index = cls.indexOf(id)
        if index == -1:
            return cls.create(id)

        return s_activeMods[index]

    @classmethod
    def indexOf(cls, id : str) -> int:
        id = id.strip()
        cls.requireValidId(id)
        for index, mod in s_activeMods.as_list().enumerate():
            if mod.id.lower() == id.lower():
                return index

        return -1

    @classmethod
    def create(cls, id : str): #->ActiveMods
        cls.requireValidId(id)
        if cls.indexOf(id) > -1:
            assert False, "illegal state" #TODO: proper exception?

        mod = ActiveMods(id)
        s_activeMods.add(mod)
        return mod

    @classmethod
    def requireValidId(cls, id : str) -> None:
        if not id:
            raise ValueError('id must be a valid string')


    @classmethod
    def setLoadedMods(cls, mods) -> None: # mods : ActiveMods) -> None:
        raise NotImplementedError


    @classmethod
    def requiresResetLua(cls, mods) -> bool:
        raise NotImplementedError

    @classmethod
    def renderUI(cls) -> None:
        raise NotImplementedError

    @classmethod
    def Reset(cls) -> None:
        raise s_loaded.clear()

    def clear(self) -> None:
        self.mods.clear()
        self.mapOrder.clear()

    def getMods(self) -> ArrayList:
        return self.mods

    def getMapOrder(self) -> ArrayList:
        return self.mapOrder

    def copyFrom(self, mods) -> None: # mods : ActiveMods) -> None:
        self.clear()
        self.mods.addAll(mods.mods)
        self.mapOrder.addAll(mods.mapOrder)

    def setModActive(self, id : str, active : bool) -> None:
        id = id.strip()
        if not id:
            return

        if not active:
            self.mods.remove(id)

        elif id not in self.mods:
            self.mods.add(id)


    def isModActive(self, id : str) -> bool:
        return id.strip() in self.mods

    def removeMod(self, id : str) -> None:
        raise NotImplementedError

    def removeMapOrder(self, id : str) -> None:
        raise NotImplementedError

    def checkMissingMods(self) -> None:
        raise NotImplementedError

    def checkMissingMaps(self) -> None:
        raise NotImplementedError


######################################################################

s_loaded = ActiveMods('loaded')
