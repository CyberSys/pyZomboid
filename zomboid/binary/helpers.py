#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 19:20:02 2019

@author: wolf
"""
from struct import pack, unpack


def unpack_string(data, start):
    """basic string unpacking."""
    length, = unpack('>H', data[start:2+start])
    result, = unpack('>%ss' % length, data[2+start:2+start+length])
    return result.decode(), 2+start+length 


def unpack_conditional(obj, key, data, pos, callback, default=None):
    """checks if a byte is a 0|1 and runs the callback to unpack if 1"""
    cond, = unpack('>?', data[pos:1+pos])
    result = None
    pos +=1
    if cond:
        assert callback, "no callback for %s" % key
        result, pos = callback(data, pos)
    return result, pos


def unpack_table(data, start):
    # read a int. total number of key/value pairs
    # loop:
    #   read byte: (0 = string, 1 = double)
    #   read key (string or double)
    #   read byte: (0 = string, 1 double, 2 table, 3 bool)
    #   read value. note tables (byte 2) will need to recurse
    length, = unpack('>i', data[start:4+start])
    pos = 4+start
    #print("Reading kahlua table, %s items" % length)
    table = {}
    for i in range(length):
        key_type, = unpack('>b', data[pos:1+pos])
        pos +=1
        if key_type == 0:
            key, pos = unpack_string(data, pos)
        elif key_type == 1:
            key, = unpack('>d', data[pos:8+pos])
            pos += 8
        else:
            assert False, "Bad kahlua table? key_type is %s" % key_type

        value_type, = unpack('>b', data[pos:1+pos])
        pos +=1
        
        if value_type == 0:
            value, pos = unpack_string(data, pos)
        elif value_type == 1:
            value, = unpack('>d', data[pos:8+pos])
            pos += 8
        elif value_type == 2:
            value, pos = unpack_table(data, pos)
        elif value_type == 3:
            value = unpack('>?', data[pos:1+pos])
            pos += 1
        else:
            assert False, "Bad kahlua table? value_type is %s" % value_type
        
        table[key] = value
    print("ModData Table: %s" % str(table))
    return table, pos


def unpack_withsize(data, start):
    # read a int, record position after.
    from zomboid.inventory import InventoryItem
    length, = unpack(">i", data[start:4+start])
    pos = 4+start
    item_type, pos = unpack_string(data, pos)
    save_type = unpack(">b", data[pos:1+pos])
    pos += 1
    #print("InventoryItem is: " + repr(item_type))
    ##print("item: %s, len: %s" % (repr(item_type), len(item_type)))
    if not item_type: # or item_type == "\x00":
        print("Skipping null InventoryItem")
        return None, pos
    else:
        #print(repr(item_type))
        item = InventoryItem()
        item.full_type = item_type
        pos = item.load(data, pos)    
    pos = 4 + start + length
    
    return item, pos



def unpack_window(data, start):
    from zomboid.vehicles import VehicleWindow
    d = VehicleWindow()
    return d, d.load(data, start)

def unpack_door(data, start):
    from zomboid.vehicles import VehicleDoor
    d = VehicleDoor()
    return d, d.load(data, start)

def unpack_light(data, start):
    from zomboid.vehicles import VehicleLight
    d = VehicleLight()
    return d, d.load(data, start)

def unpack_devicedata(data, start):
    from zomboid.radio import DeviceData
    p = DeviceData()
    return p, p.load(data, start)


def unpack_devicepresets(data, start):
    from zomboid.radio import DevicePresets
    p = DevicePresets()
    return p, p.load(data, start)

def unpack_devicepresetslist(data, start):
    chan, pos = unpack_string(data, start)
    val, = unpack('>i', data[pos:4+pos])
    return ((chan, val), 4+pos)


def unpack_part(data, start):
    from zomboid.vehicles import VehiclePart
    p = VehiclePart()
    return p, p.load(data, start)

def unpack_itemcontainer(data, start):
    from zomboid.iso import ItemContainer
    p = ItemContainer()
    return p, p.load(data, start)
    

def unpack_compresseditems(data, start):
    import zomboid.inventory.InventoryItemFactory as InventoryItemFactory
    print("Reading Compressed Items")
    result = []
    count, = unpack('>h', data[start:2+start])    
    pos = 2+start
    print("total count:" + str(count))
    for c in range(count):
        i,j = unpack('>ii', data[pos:8+pos])
        pos +=8
        k = pos
        #print("i, j:", i, j)
        full_type, pos = unpack_string(data, pos)
        
        save_type = unpack(">b", data[pos:1+pos])
        #print("save_type: %s" % save_type)
        pos += 1
        
        print("Reading Comressed Item: "+full_type)

        if False: # testing block to skip items
            print("skipping....")
            m = (i > 1) and ((i - 1) * 8) or 0       
            pos = (k + j + m)
            #print("Jumping to %s" % pos)
            continue
        
        # note: something chokes and we end with wrong position.
        mark = pos
        for n in range(i):
            #print("creating item")
            pos = mark
            item = InventoryItemFactory.CreateItem(full_type)
            assert item
            #item = InventoryItem()
            result.append(item)
            item.full_type = full_type
            pos = item.load(data, pos)
            #print("at: %s" % pos)
        
        for n in range(i-1):
            this_id, = unpack(">q", data[pos:8+pos])
            pos +=8
            result[len(result) - i + n].id 
        #this_id, = unpack(">q", data[pos:8+pos])
        #pos +=8
        #if result:
        #    result[-1].id = this_id
    # short number of items (s)
    # loop s:
    #   int (number of identicals?) (i) 
    #   int (j)
    #   mark pos (k)
    #   string
    #   byte (save type?) (b1)
    #   replace .. with . in string?
    #   mark pos (m)
    #   loop i
    #       jump m
    #       create item and load
    return result, pos

