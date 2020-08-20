#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 23:04:32 2019

@author: wolf
"""
import enum



class Enum(enum.Enum):

    @classmethod
    def valueOf(cls, key):
        for attrib in dir(cls):
            if attrib.lower() == key.lower():
                return cls[attrib]

        raise KeyError("invalid enum key")



class ArrayList:
    def __init__(self, data=None):
        if data is None:
            data = []

        self.data = data

    def add(self, value):
        self.data.append(value)

    def remove(self, value):
        self.data.remove(value)

    def get(self, index):
        return self.data[index]

    def size(self):
        return len(self.data)

    def contains(self, value):
        return (value in self.data)

    def isEmpty(self):
        return len(self.data) > 0

    def clear(self):
        self.data = []

    def __add__(self, other):
        if isinstance(other, ArrayList):
            other = other.data

        return ArrayList(self.data + other)
    
    def __len__(self):
        return self.size()

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __contains__(self, value):
        return value in self.data

    def __iter__(self):
        return iter(self.data)

class HashMap:
    def __init__(self, data=None):
        if data is None:
            data = {}

        self.data = data

    def remove(self, key):
        if key in self.data:
            del self.data[key]

    def __delitem__(self, key):
        del self.data[key]

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __contains__(self, value):
        return value in self.data

    def __iter__(self):
        return iter(self.data)


class LinkedList:
    pass


class BufferedReader:
    def __init__(self, path):
        self.io = open(path)

    def readLine(self):
        self.io.readline()

    def close(self):
        self.io.close()
