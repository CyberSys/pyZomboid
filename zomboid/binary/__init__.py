#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 19:19:50 2019

@author: wolf
"""
from struct import unpack
import zomboid.binary.helpers as helpers
import zomboid.binary.instructions as instructions

_format_instructions = ('conditional', 'callback', 'report', 'string')
_format_sizes = {'b':1, 'B':1,'?':1,'h':2,'H':2,'i':4,'I':4,'f':4,'l':4,'L':4,'q':8,'Q':8,'d':8}
def format_size(text):
    return sum([_format_sizes[x] for x in text])



def load(obj, template, data, pos=0):
    return run_instruction_set(obj, template, data, pos)



def run_instruction_set(obj, template, data, pos=0, write_mode=False, depth=0):
    """loops through all items in the instruction set performing each one and 
    setting attributes on the specifed object"""
    print("Reading binary data for %s" % str(obj))
    instruction_set = instructions.instruction_sets[template]
    for rule in instruction_set:
        value = None
        callback = rule.load
        if write_mode:
            callback = rule.save
        #print(rule)
        if rule.format == 'include':

            assert depth <= 1, "recursed mutliple times."
            pos = run_instruction_set(obj, rule.attrib, data, pos, write_mode, depth+1)
            continue
            
        elif rule.format == 'string':
            value, pos = helpers.unpack_string(data, pos)

        elif rule.format == 'conditional':            
            cond, = unpack('>?', data[pos:1+pos])
            result = None
            pos +=1
            if cond:
                assert callback, "no callback for %s" % rule.attrib
                value, pos = callback(data, pos)
            #value, pos = helpers.unpack_conditional(obj, key, data, pos, length) # length is callback function here

        elif rule.format.startswith('list:'):
            f = rule.format[-1]
            length = format_size(f)
            count, = unpack('>'+f, data[pos:pos+length])
            pos += length
            value = []
            for i in range(count):
                result, pos = callback(data, pos) # length is callback function here
                value.append(result)

        elif rule.format == 'callback':
            result, pos = callback(data, pos)

        elif rule.format == 'report': # cheap callback no update of position for debugging purposes. does nothing!
            callback(obj, template, data, pos)
            continue

        else:
            length = format_size(rule.format)
            value = unpack(">" + rule.format, data[pos:pos+length])
            if len(rule.format) == 1:
                value, = value
            pos += length
            
        setattr(obj, rule.attrib, value)

    return pos
