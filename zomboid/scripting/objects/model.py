# -*- coding: utf-8 -*-
from zomboid.java import ArrayList
from .base import BaseScriptObject
from ..parser import ScriptParser

Model = None #TODO: replace with class 
Vector3f = None #TODO: replace with class 

class ModelAttachment:
    id : str = None
    offset : Vector3f = None
    rotate : Vector3f = None
    bone : str = None

    def __init__(self, id : str):
        self.id = id
        self.offset = None #TODO: replace with class initialization
        self.rorate = None #TODO: replace with class initialization

    def getId(self) -> str:
        return self.id

    def setId(self, value : str) -> None:
        if not value:
            return #TODO: raise exception

        self.id = value

    def getOffset(self) -> Vector3f:
        return self.offset

    def getRotate(self) -> Vector3f:
        return self.rotate

    def getBone(self) -> str:
        return self.bone

    def setBone(self, value : str) -> None:
        if not value:
            value = None # no empty strings
        self.bone = value


class ModelScript(BaseScriptObject):
    DEFAULT_SHADER_NAME : str = "basicEffect"
    fileName : str = None
    name : str = None
    scale : float = 1.0
    meshName : str = None
    textureName : str = None
    shaderName : str = None
    bStatic : bool = None
    m_attachments : ArrayList = None
    invertX : bool = False
    loadedModel : Model = None

    def __init__(self):
        self.m_attachments = ArrayList()


    def Load(self, name : str, data : str) -> None:
        from ..manager import instance
        self.fileName = instance.currentFileName
        self.name = name
        block = ScriptParser.parse(data)
        block = block.children[0]
        for sub in block.children:
            if sub.type == 'attachment':
                self.LoadAttachment(sub)

        for value in block.values:
            key, value = value.string.split(' = ')
            key = key.lower()
            if key == 'mesh':
                self.meshName = value
            elif key == 'scale':
                self.scale = float(value)
            elif key == 'shader':
                self.shaderName = value
            elif key == 'static':
                self.bStatic = value.lower() == 'true'
            elif key == 'texture':
                self.textureName = value
            elif key == 'invertX':
                self.invertX = value.lower() == 'true'


    def LoadAttachment(self, block) -> ModelAttachment:
        attach = self.getAttachmentById(block.id)
        if not attach:
            attach = ModelAttachment(block.id)
            self.m_attachments.add(attach)

        for value in block.values:
            key, value = value.string.split(' = ')
            if key == 'bone':
                attach.setBone(value)
            elif key == 'offset':
                self.LoadVector3f(value, attach.offset)
            elif key == 'rotate':
                self.LoadVector3f(value, attach.offset)

        return attach


    def LoadVector3f(cls, data : str, vector : Vector3f) -> None:
        data = [float(x) for x in data.split()]
        # TODO: set the vector here
        


    def getName(self) -> str:
        return self.name


    def getFullType(self) -> str:
        return f"{self.module.name}.{self.name}"


    def getMeshName(self) -> str:
        return self.meshName


    def getTextureName(self) -> str:
        if not self.textureName:
            return self.meshName

        return self.textureName


    def getShaderName(self) -> str:
        if not self.shaderName:
            return 'basicEffect'

        return self.textureName


    def getFileName(self) -> str:
        return self.fileName


    def getAttachmentCount(self) -> int:
        return len(self.m_attachments)


    def getAttachment(self, index : int) -> ModelAttachment:
        return self.m_attachments[index]


    def getAttachmentById(self, id : str) -> ModelAttachment:
        for attach in self.m_attachments:
            if attach.id == id:
                return attach

        return None


    def addAttachment(self, attach : ModelAttachment) -> ModelAttachment:
        self.m_attachments.add(attach)
        return attach


    def removeAttachment(self, attach : ModelAttachment) -> ModelAttachment:
        if isinstance(attach, int):
            attach = self.m_attachments[attach] #TODO: beware exceptions

        self.m_attachments.remove(attach)
        return attach

    def addAttachmentAt(self, index : int, attach : ModelAttachment) -> ModelAttachment:
        self.m_attachments.add(index, attach)
        return attach


    def reset(self) -> None:
        self.name = None
        self.meshName = None
        self.textureName = None
        self.shaderName = None
        self.bStatic = False
        self.scale = 1.0
