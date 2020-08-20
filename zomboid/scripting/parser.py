#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 19:00:19 2020

@author: wolf
"""

from zomboid.java import ArrayList

class Value:
    string : str = None
    
    def asBlock(self):
        return None

    def asValue(self):
        return self

    def getKey(self) -> str:
        if '=' not in self.string:
            return self.string

        return self.string.split('=')[0]


    def getValue(self) -> str:
        if '=' not in self.string:
            return ''

        return self.string.split('=')[1]
        

class Block:
    type : str = None
    id : str = None
    elements : ArrayList = None
    values : ArrayList = None
    children : ArrayList = None

    def __init__(self):
        self.elements = ArrayList()
        self.values = ArrayList()
        self.children = ArrayList()

    def asBlock(self):
        return self

    def asValue(self):
        return None

    def isEmpty(self) -> bool:
        return self.elements.isEmpty()

    def addBlock(self, type : str, id : str): #-> Block:
        block = Block()
        block.type = type
        block.id = id
        self.elements.add(block)
        self.children.add(block)
        return block

    def getBlock(self, type : str, id : str): #-> Block:
        for block in self.children:
            if block.type == type and block.id == id:
                return block

        return None


    def getValue(self, key : str) -> Value:
        for value in self.values:
            if value.string[0] != '=' and value.getKey().strip() == key:
                return value

        return None


    def setValue(self, key : str, new_value : str) -> None:
        value = self.getValue(key)
        if not value:
            self.addValue(key, value)
        else:
            value.string = f"{key} = {new_value}"


    def addValue(self, key : str, new_value : str) -> Value:
        value = Value()
        value.string = f"{key} = {new_value}"
        self.elements.add(value)
        self.values.add(value)
        return value


class ScriptParser:
    @classmethod
    def stripComments(cls, data : str) -> str:
        end = data.rfind("*/")
        while end != -1:
            start = data[:end].rfind("/*")
            if start == -1:
                break

            k = data[:end].rfind("*/")
            while k > start:
                prev_start = start
                start = data[:start].rfind("/*")
                if start == -1:
                    break
                k = data[:prev_start-1].rfind("*/")

            if start == -1:
                break
            
            data = data[0:start] + data[end+2:]
            end = data[:start].rfind("*/")

        return data


    @classmethod
    def parseTokens(cls, data : str) -> list:
        tokens = []
        while True:
            depth, nextOpen, nextClosed = 0,0,0
            if data.find("}", nextOpen + 1) == -1:
                break

            while True:
                nextOpen = data.find("{", nextOpen + 1) # find next block open
                nextClosed = data.find("}", nextClosed + 1) # find next block closed
                if (((nextClosed < nextOpen) # closed comes before open 
                    and (nextClosed != -1)) # didnt find a close
                    or (nextOpen == -1)): # no more open
                    nextOpen = nextClosed
                    depth -= 1

                else:
                #elif (nextOpen != -1):
                    nextClosed = nextOpen
                    depth += 1

                if depth <= 0:
                    break

            tokens.append(data[0:nextOpen+1].strip())
            data = data[nextOpen+1:]
        
        if data.strip():
            tokens.append(data.strip())

        return tokens


    @classmethod
    def parse(cls, data : str) -> Block:
        block = Block()
        cls.readBlock(data, 0, block)
        return block
    
    @classmethod
    def readBlock(cls, data : str, start : int, block : Block) -> int:
        pos = start -1
        while pos < len(data):
            pos += 1
            if data[pos] == '{':
                new_block = Block()
                block.children.add(new_block)
                block.elements.add(new_block)
                text = data[start:pos].strip()
                try:
                    new_block.type, new_block.id = text.split()

                except ValueError:
                    new_block.type = text
                
                pos = cls.readBlock(data, pos+1, new_block)
                start = pos
                
            else:
                if data[pos] == '}':
                    return pos+1

                if data[pos] == ',':
                    value = Value()
                    value.string = data[start:pos]
                    block.values.add(value)
                    block.elements.add(value)
                    start = pos + 1
            
        return pos

