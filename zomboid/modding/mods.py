# -*- coding: utf-8 -*-

from zomboid.java import ArrayList

class ActiveMods:
    s_activeMods : ArrayList = None
    s_loaded : ArrayList = None
    
    def __init__(self, id : str):
        self.requireValidId(id)
        self.s_loaded = ArrayList(['loaded'])
        self.id = id
        
    @classmethod
    def requireValidId(cls, id : str) -> None:
        if not id:
            raise ValueError('id must be a valid string')
