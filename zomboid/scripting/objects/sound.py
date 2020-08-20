# -*- coding: utf-8 -*-

from zomboid.audio.sound import GameSound, MasterVolume, GameSoundClip
from .base import BaseScriptObject 
from ..parser import ScriptParser, Block

class GameSoundScript(BaseScriptObject):
    gameSound : GameSound = None
    
    def __init__(self):
        self.gameSound = GameSound()

    def Load(self, name : str, data : str) -> None:
        self.gameSound.name = name
        block = ScriptParser.parse(data)
        block = block.children[0]
        for value in block.values:
            key, value = value.string.split(' = ')
            if key == 'category':
                self.gameSound.category = value

            elif key == 'is3D':
                self.gameSound.is3D = value.lower() == 'true'

            elif key == 'loop':
                self.gameSound.loop = value.lower() == 'true'

            elif key == 'master':
                self.gameSound.master = MasterVolume.valueOf(value)

        for subblock in block.children:
            if subblock.type == 'clip':
                clip = self.LoadClip(subblock)
                self.gameSound.clips.add(clip)


    def LoadClip(self, block : Block) -> GameSoundClip:
        clip = GameSoundClip(self.gameSound)
        for value in block.values:
            key, value = value.string.split(' = ')
            if key == 'distanceMax':
                clip.distanceMax = int(value) # NOTE: this should be a float.
        
            elif key == 'distanceMin':
                clip.distanceMin = int(value) # NOTE: this should be a float.

            elif key == 'event':
                clip.event = value

            elif key == 'file':
                clip.file = value

            elif key == 'pitch':
                clip.pitch = float(value)

            elif key == 'volume':
                clip.volume = float(value)

            elif key == 'reverbFactor':
                clip.reverbFactor = float(value)

            elif key == 'reverbMaxRange':
                clip.reverbMaxRange = float(value)

        return clip


    def reset(self) -> None:
        self.gameSound.reset()
