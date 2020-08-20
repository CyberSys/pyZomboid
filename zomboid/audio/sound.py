# -*- coding: utf-8 -*-
from zomboid.java import ArrayList, Enum

class MasterVolume(Enum):
    Primary = 0
    Ambient = 1
    Music = 2
    VehicleEngine = 3


class GameSound:
    name : str = None
    category : str = "General"
    loop : bool = False
    is3D : bool = True
    clips : ArrayList = None
    userVolume : float = 1.0
    master : int = MasterVolume.Primary
    reloadEpoch : int = None

    def __init__(self):
        self.clips = ArrayList()


class GameSoundClip:
    gameSound : GameSound = None
    event : str = None
    file : str = None
    volume : float = 1.0
    pitch : float = 1.0
    distanceMin : float = 10.0
    distanceMax : float = 10.0
    reverbMaxRange : float = 10.0
    reverbFactor : float = 0.0
    priority : int = 5
    initFlags : int = 0
    reloadEpoch : int
    
    def __init__(self, gamesound : str):
        self.gameSound = gamesound
