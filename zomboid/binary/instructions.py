#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file is a instruction set for reading/writing the binary structures of pz's class objects.
Useful for reading and manuplating savegame data.

Each 'instruction set' is a tuple, and each instruction (rule) in the set is a namedtuple.

Each namedtuple rule has 4 values:

attrib is the object attribute name of the value

format is a string struct format, or special keyword:
    'include' includes another instruction set identified by the attrib value
    
    'callback' run either the function passed via load attribute, or save, 
        depending on current mode.
    
    'conditional' reads the next byte as a boolean. if true, runs the load/save callback.
        true or false, the byte is consumed.
    
    'list:' next byte(s) is(are) read as a data type in the format specified after the : 
        (ie 'list:i' for a int value). the callback is then run this many times.
    
    'report' executes the callback specified with no advancement in the data stream.
        ideal for debugging or running additional code without effecting the read/write
        process.

load is a callback to run on loading data, for use with the special format keywords

save is a callback to run on saving data, for use with the special format keywords




Notes on various data patterns:
Conditionals are in heavy use. A 0 or 1 byte used to determine what the following bytes 
will contain. (ie: a 1 might be used to signal the next chunk of data is a kahlua table)


Kahlua tables (aka: ModData) are recorded as:
    Read int (total number of key/value pairs) 
    loop number:
        read byte: (0 = string, 1 = double)
        read key (string or double)
        read byte: (0 = string, 1 double, 2 table, 3 bool)
        read value. note tables (byte 2) will need to recurse




Created on Sat Dec 14 19:22:06 2019

@author: wolf
"""
from struct import unpack
import zomboid.binary.helpers as helpers
from collections import namedtuple

Rule = namedtuple('Rule', ('attrib', 'format', 'load', 'save'))

# 41.23 Binary format.
instruction_sets = {
    'IsoMovingObject' : (
        Rule('id', 'b', None, None),
        Rule('hash', 'i', None, None),
        Rule('offset_x', 'f', None, None),        
        Rule('offset_y', 'f', None, None),        
        Rule('pos', 'fff', None, None),
        Rule('index', 'i', None, None),
        Rule('table', 'conditional', helpers.unpack_table, None), # moddata kahlua table
    ),
    "BaseVehicle" :( 
        Rule('IsoMovingObject', 'include', None, None), # BaseVehicle starts with IsoMovingObject data
        Rule('quad', 'ffff', None, None),
        Rule('script', 'string', None, None),  
        Rule(None, 'report', (lambda o,t,d,p: print("BaseVehicle is %s" % o.script )), None),
        Rule('skin_index', 'i', None, None),
        Rule('engine_running', '?', None, None),
        Rule('front_durability', 'i', None, None),
        Rule('rear_durability', 'i', None, None),
        Rule('current_front_durability', 'i', None, None),
        Rule('current_rear_durability', 'i', None, None),
        Rule('engine_loudness', 'i', None, None),
        Rule('engine_quality', 'i', None, None),
        Rule('key_id', 'i', None, None),
        Rule('key_spawned', '?', None, None),
        Rule('headlight_on', '?', None, None),
        Rule('created', '?', None, None),
        Rule('horn_on', '?', None, None),
        Rule('rear_horn_on', '?', None, None),
        Rule('lightbar_mode', 'b', None, None),
        Rule('siren_mode', 'b', None, None),
        Rule('parts', 'list:h', helpers.unpack_part, None), # list of VehiclePart class objects.
        Rule('key_on_door', '?', None, None),
        Rule('hotwired', '?', None, None),
        Rule('hotwired_broken', '?', None, None),
        Rule('keys_in_ignition', '?', None, None),
        Rule('rust', 'f', None, None),
        Rule('hsv', 'fff', None, None),
        Rule('engine_power', 'i', None, None),
        Rule('vehicle_id', 'h', None, None),
        ## null string?
        Rule('null', 'string', None, None), # TODO: placeholder
        Rule('mechanical_id', 'i', None, None),
        Rule('alarmed', '?', None, None),
        Rule('siren_timestamp', 'd', None, None),
        Rule('key_data', 'conditional', None, None), #TODO: callback
        Rule(None, 'report', (lambda o,t,d,p: print("Finished parsing BaseVehicle: %s\n" % o.script)), None),
    ),
    'VehiclePart' : (
        Rule('scriptpart_id', 'string', None, None),
        Rule(None, 'report', (lambda o,t,d,p: print("VehiclePart is %s" % o.scriptpart_id)), None),
        Rule('created', '?', None, None),
        Rule('updated', 'f', None, None),
        Rule('inventory_item', 'conditional', helpers.unpack_withsize, None),
        Rule('container', 'conditional', helpers.unpack_itemcontainer, None), # conditional ItemContainer class.
        Rule('moddata', 'conditional', helpers.unpack_table, None), # moddata kahlua table
        Rule('devicedata', 'conditional', helpers.unpack_devicedata, None), # conditional DeviceData class
        Rule('light', 'conditional', helpers.unpack_light, None), # conditional Light class
        Rule('door', 'conditional', helpers.unpack_door, None), # conditional Door class
        Rule('window', 'conditional', helpers.unpack_window, None), # conditional Window class
        Rule('condition', 'i', None, None),
        Rule('wheel_friction', 'f', None, None),
        Rule('mechanics_skill_installer', 'i', None, None),
        Rule('suspension_compression', 'f', None, None),
        Rule('suspension_dampening', 'f', None, None),
        Rule(None, 'report', (lambda o,t,d,p: print("Finished parsing VehiclePart: %s\n" % o.scriptpart_id)), None),
    ),
    "VehicleDoor" : (
        Rule('open', '?', None, None),
        Rule('locked', '?', None, None),
        Rule('broken', '?', None, None)
    ),
    "VehicleLight" : (
        Rule('active', '?', None, None),
        Rule('offset_x', 'f', None, None),
        Rule('offset_y', 'f', None, None),
        Rule('intensity', 'f', None, None),
        Rule('dist', 'f', None, None),
        Rule('focus', 'i', None, None),
    ),
    "VehicleWindow" : (
        Rule('health', 'b', None, None),
        Rule('open', '?', None, None),
    ),
    "DeviceData" : (
        Rule('device_name', 'string', None, None),
        Rule('two_way', '?', None, None),
        Rule('transmit_range', 'i', None, None),
        Rule('mic_range', 'i', None, None),
        Rule('mic_muted', '?', None, None),
        Rule('base_volume_range', 'f', None, None),
        Rule('device_volume', 'f', None, None),
        Rule('is_portable', '?', None, None),
        Rule('is_television', '?', None, None),
        Rule('is_hightier', '?', None, None),
        Rule('is_turned_on', '?', None, None),
        Rule('channel', 'i', None, None),
        Rule('min_channel', 'i', None, None),
        Rule('max_channel', 'i', None, None),
        Rule('is_battery', '?', None, None),
        Rule('has_battery', '?', None, None),
        Rule('power_delta', 'f', None, None),
        Rule('use_delta', 'f', None, None),
        Rule('headphone_type', 'i', None, None),
        Rule('presets', 'conditional', helpers.unpack_devicepresets, None), # a map of strings followed by int values
    ),
    "DevicePresets":(
        Rule('max_presets', 'i', None, None),
        Rule('presets', 'list:i', helpers.unpack_devicepresetslist, None)
    ),
    "ItemContainer" :(
        Rule('type', 'string', None, None),
        Rule(None, 'report', (lambda o,t,d,p: print("ItemContainer is %s" % o.type)), None),
        Rule('explored', '?', None, None),
        #('items', 'list:h:2', helpers.unpack_compresseditems),
        Rule('items', 'callback', helpers.unpack_compresseditems, None),
        Rule('been_looted','?', None, None),
        Rule('capacity', 'i', None, None),
        Rule(None, 'report', (lambda o,t,d,p: print("Finished parsing ItemContainer %s\n" % o.type)), None),
    ),
    "InventoryItem" :(
        Rule(None, 'report', (lambda o,t,d,p: print("InventoryItem is %s" % o.full_type)), None),
        Rule('uses', 'i', None, None),
        Rule('id', 'q', None, None),
        Rule('table', 'conditional', helpers.unpack_table, None),
        Rule('use_delta', 'conditional', (lambda data,pos: (unpack(">f", data[pos:4+pos])[0], 4+pos)), None), # need to unpack a single float, on a conditional PITA!!!!
        Rule('condition', 'b', None, None),
        Rule('activated', '?', None, None),
        Rule('times_repaired', 'h', None, None),
        Rule('name', 'conditional', helpers.unpack_string, None),
        Rule('bytedata', 'conditional', None, None), #TODO: callback
        Rule('extra_items', 'list:i', helpers.unpack_string, None),
        Rule('custom_name', '?', None, None),
        Rule('weight', 'f', None, None),
        Rule('key_id', 'i', None, None),
        Rule('tainted', '?', None, None),
        Rule('remote_controller_id', 'i', None, None),
        Rule('remote_range', 'i', None, None),
        Rule('color', 'fff', None, None),
        Rule('worker', 'string', None, None),
        Rule('wetcooldown', 'f', None, None),
        Rule('favorite', '?', None, None),
        Rule('custom_color', 'conditional', None, None), # TODO: callbacks
        Rule('stash_map', 'string', None, None),
        Rule('capacity', 'f', None, None),
        Rule('infected', '?', None, None),
        Rule('visual', 'conditional', None, None),
        Rule('ammo_count', 'i', None, None),
        Rule('slot', 'i', None, None),
        Rule('slot_type', 'string', None, None),
        Rule('attached_model', 'string', None, None),
        Rule(None, 'report', (lambda o,t,d,p: print("Finished parsing InventoryItem %s\n" % o.full_type)), None),
    ),
    "AlarmClock":(
        Rule('InventoryItem', 'include', None, None), # Starts with InventoryItem data
        Rule('alarm_hour', 'i', None, None),
        Rule('alarm_minute', 'i', None, None),
        Rule('alarm_set', '?', None, None),
        Rule('ring_since', 'f', None, None),
    ),
    "Clothing":(
        Rule('InventoryItem', 'include', None, None), # Starts with InventoryItem data
        Rule('col', 'fff', None, None), # hsv color
        Rule('dirt', 'f', None, None),
        Rule('blood', 'f', None, None),
        Rule('wetness', 'f', None, None),
        Rule('wetness_update', 'f', None, None),
        Rule('patches', 'list:i', None, None) # TODO: callback, ClothingPatch objects. This is actually a java map, with a preceeding int value key, value being ClothingPatch data.
    ),
    "ClothingPatch":(
        Rule('tailor_level', 'i', None, None),
        Rule('fabric_type', 'i', None, None),
        Rule('scratch_defense', 'i', None, None),
        Rule('bite_defense', 'i', None, None),
        Rule('has_hole', '?', None, None),
        Rule('condition_gain', 'i', None, None),
    ),
    "Food":(
        Rule('heat', 'f', None, None),
        Rule('age', 'f', None, None),
        Rule('last_aged', 'f', None, None),
        Rule('last_cook_minute', 'i', None, None),
        Rule('cooking_time', 'f', None, None),
        Rule('cooked', '?', None, None),
        Rule('burnt', '?', None, None),
        Rule('hunger_change', 'f', None, None),
        Rule('base_hunger', 'f', None, None),
        Rule('unhappy_change', 'f', None, None),
        Rule('bordom_change', 'f', None, None),
        Rule('is_cookable', '?', None, None),
        Rule('dangerous_uncooked', '?', None, None),
        Rule('poison_detection_level', 'i', None, None),
        Rule('spices', 'conditional', None, None), # TODO: callback. conditional list, int size, string names
        Rule('poison_power', 'i', None, None),
        Rule('thirst_change', 'f', None, None),
        Rule('chef', 'string', None, None),
        Rule('off_age', 'f', None, None),
        Rule('off_age_max', 'f', None, None),
        Rule('pain_reduction', 'f', None, None),
        Rule('flu_reduction', 'f', None, None),
        Rule('reduce_food_sickness', 'i', None, None),
        Rule('poison', '?', None, None),
        Rule('use_for_poison', 'i', None, None),
        Rule('calories', 'f', None, None),
        Rule('proteins', 'f', None, None),
        Rule('lipids', 'f', None, None),
        Rule('carbohydrates', 'f', None, None),
        Rule('freezing_time', 'f', None, None),
        Rule('last_frozen_update', 'f', None, None),
        Rule('rotten_time', 'f', None, None),
        Rule('compost_time', 'f', None, None),
        Rule('cooked_in_microwave', '?', None, None),
    ),
    "HandWeapon":(
        Rule('InventoryItem', 'include', None, None), # Starts with InventoryItem data
        Rule('max_range', 'f', None, None),
        Rule('min_range_ranged', 'f', None, None),
        Rule('clip_size', 'i', None, None),
        Rule('min_damage', 'f', None, None),
        Rule('max_damage', 'f', None, None),
        Rule('recoil_delay', 'i', None, None),
        Rule('aiming_time', 'i', None, None),
        Rule('reload_time', 'i', None, None),
        Rule('hit_chance', 'i', None, None),
        Rule('min_angle', 'f', None, None),
        # max of 6 attachments, InventoryItem for those are not saved, data is stored as string names
        Rule('part1', 'conditional', helpers.unpack_string, None),
        Rule('part2', 'conditional', helpers.unpack_string, None),
        Rule('part3', 'conditional', helpers.unpack_string, None),
        Rule('part4', 'conditional', helpers.unpack_string, None),
        Rule('part5', 'conditional', helpers.unpack_string, None),
        Rule('part6', 'conditional', helpers.unpack_string, None),
        Rule('explosion_timer', 'i', None, None),
        Rule('max_angle', 'f', None, None),
        Rule('blood_level', 'f', None, None),
        Rule('contains_clip', '?', None, None),
        Rule('round_chambered', '?', None, None),
        Rule('jammed', '?', None, None),
        Rule(None, 'report', (lambda o,t,d,p: print("Finished parsing HandWeapon %s\n" % o.full_type)), None),
    ),
    "InventoryContainer":(
        Rule('InventoryItem', 'include', None, None), # Starts with InventoryItem data
        Rule('container_id', 'i', None, None),
        Rule('weight_reduction', 'i', None, None),
        Rule('container', 'callback', helpers.unpack_itemcontainer, None), 
        Rule(None, 'report', (lambda o,t,d,p: print("Finished parsing InventoryContainer %s\n" % o.full_type)), None),
    ),
    "Key":(
        Rule('InventoryItem', 'include', None, None), # Starts with InventoryItem data
        Rule('key_id', 'i', None, None),
        Rule('number_of_key', 'b', None, None),
    ),
    "Literature" :(
        Rule('InventoryItem', 'include', None, None), # Starts with InventoryItem data
        Rule('num_of_pages', 'i', None, None),
        Rule('read_pages', 'i', None, None),
        Rule('can_write', '?', None, None),
        Rule('custom_pages', 'list:i', helpers.unpack_string, None),
        Rule('locked_by', 'conditional', helpers.unpack_string, None),
    ),
    "Moveable" :(
        Rule('InventoryItem', 'include', None, None), # Starts with InventoryItem data
        Rule('world_sprite', 'string', None, None),
        Rule('is_light', '?', None, None), # if is_light is true, then addition bytes are read. note this is not the same as other conditionals and needs special handling
        #Rule('light_uses_battery', '?', None, None),
        #Rule('light_has_battery', '?', None, None),
        #Rule('lightbulb_item', 'conditional', helpers.unpack_string, None), # note this conditional byte is seperate from the previous bool byte.
        #Rule('light_power', 'f', None, None),
        #Rule('light_delta', 'f', None, None),
        #Rule('light_r', 'f', None, None),
        #Rule('light_g', 'f', None, None),
        #Rule('light_b', 'f', None, None),
    ),
    "Radio" :(
        Rule('InventoryItem', 'include', None, None), # Starts with InventoryItem data
        Rule('devicedata', 'conditional', helpers.unpack_devicedata, None), # conditional DeviceData class
    ),

    "IsoGameCharacter" :(
        Rule('IsoMovingObject', 'include', None, None), # IsoMovingObject data
        Rule('descriptor', 'conditional', None, None), #TODO: callback. Need to load a SurvivorDesc, and set bool female
        Rule('inventory', 'callback', helpers.unpack_itemcontainer, None),
        Rule('asleep', '?', None, None),
        Rule('force_wakeup_time', 'f', None, None),
        # custom block here, loaded if object is not a zombie
        Rule('stats', 'callback', None, None), #TODO: callback. Stats class
        Rule('bodydamage', 'callback', None, None), #TODO: callback. BodyDdamage class
        Rule('xp', 'callback', None, None), #TODO: callback. XP class
        # read a int. inventory index of primary hand item
        # read a int. inventory index of secondary hand item
        # end block
        Rule('on_fire', '?', None, None),
        Rule('depress_effect', 'f', None, None),
        Rule('depress_first_take_time', 'f', None, None),
        Rule('beta_effect', 'f', None, None),
        Rule('beta_delta', 'f', None, None),
        Rule('pain_effect', 'f', None, None),
        Rule('pain_delta', 'f', None, None),
        Rule('sleepingtablet_effect', 'f', None, None),
        Rule('sleepingtablet_delta', 'f', None, None),
        Rule('readbooks', 'list:i', None, None), #TODO: callback. each list item is a string, followed by int (pages read)
        Rule('reduce_infenction', 'f', None, None),
        Rule('known_recipes', 'list:i', helpers.unpack_string, None),
        Rule('last_hour_slept', 'i', None, None),
        Rule('time_since_smoke', 'f', None, None),
        Rule('beard_grow_time', 'f', None, None),
        Rule('hair_grow_time', 'f', None, None),
        # cheat flags
        Rule('unlimited_weight', '?', None, None),
        Rule('build_cheat', '?', None, None),
        Rule('health_cheat', '?', None, None),
        Rule('mechancis_cheat', '?', None, None),
    ),
    "IsoPlayer" :(
        # huh? reads these 2 on load, but doesnt seem to save?
        Rule(None, 'b', None, None),
        Rule(None, 'i', None, None),
        Rule('IsoGameCharacter', 'include', None, None), # IsoGameCharacter data
        Rule("hours_survived", 'd', None, None),
        Rule("zombies_killed", 'i', None, None),
        Rule("worn_items", 'list:b', None, None), #TODO: callback. read a string (location), read a short (inventory item index). 

    ),
    "Stats":(
        Rule('anger', 'f', None, None),
        Rule('boredom', 'f', None, None),
        Rule('endurance', 'f', None, None),
        Rule('fatigue', 'f', None, None),
        Rule('fitness', 'f', None, None),
        Rule('hunger', 'f', None, None),
        Rule('morale', 'f', None, None),
        Rule('stress', 'f', None, None),
        Rule('fear', 'f', None, None),
        Rule('panic', 'f', None, None),
        Rule('sanity', 'f', None, None),
        Rule('sickness', 'f', None, None),
        Rule('Boredom', 'f', None, None), # yes, entries for boredom? this one seems unused.
        Rule('Pain', 'f', None, None),
        Rule('drunkenness', 'f', None, None),
        Rule('thirst', 'f', None, None),
        Rule('cigarette_stress', 'f', None, None),
    ),
            
    "GameTime":( # map_t.bin
        Rule(None, 'bbbb', None, None), # 4 bytes 71,77,84,77 (GMTM)
        Rule('version', 'i', None, None),
        Rule('multiplier', 'f', None, None),
        Rule('nights_survived', 'i', None, None),
        Rule('target_zombies', 'i', None, None),
        Rule('last_time_of_day', 'f', None, None),
        Rule('time_of_day', 'f', None, None),
        Rule('day', 'i', None, None),
        Rule('month', 'i', None, None),
        Rule('year', 'i', None, None),
        Rule(None, 'f', None, None), # 2 floats, both 0.0
        Rule(None, 'i', None, None), # value 0
        Rule('table', 'conditional', helpers.unpack_table, None), # moddata kahlua table
        Rule('core_poisonous_berry', 'string', None, None), # attribute of Core.class
        Rule('core_poisonous_mushroom', 'string', None, None), # attribute of Core.class
        Rule('helicoptor_day1', 'i', None, None),
        Rule('helicoptor_time1start', 'i', None, None),
        Rule('helicoptor_time1end', 'i', None, None),
        # need to load the ClimateManager data in a seperate object
    ),
    "ClimateManager":(
        ## this whole section is !client || server (sp or server-side only)
        Rule(None, 'b', None, None), # true conditional for the following
        Rule('simplex_offset_a', 'd', None, None),
        Rule('simplex_offset_b', 'd', None, None),
        Rule('simplex_offset_c', 'd', None, None),
        Rule('simplex_offset_d', 'd', None, None),
        # AirFront data        
        Rule('snow_frac_now', 'f', None, None),
        Rule('snow_strength', 'f', None, None),
        Rule('can_do_winter_sprites', '?', None, None),
        Rule('day_do_fog', '?', None, None),
        Rule('day_fog_strength', 'f', None, None),
        ## end 
        
        #Rule(None, 'b', None, None), # false conditional for the above
        
    ),
}
