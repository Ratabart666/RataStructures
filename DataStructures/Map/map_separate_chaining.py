from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.List import single_linked_list as sl
from DataStructures.List import array_list as al
import random as rd
import sys


def new_map(num_elements, load_factor, prime=109345121):
    
    
    capacity = mf.next_prime(num_elements//load_factor)
    scale = rd.randint(1, prime-1)
    shift = rd.randint(0, prime-1)
    
    table = al.new_list()
    
    for i in range(capacity):
        bucket = sl.new_list()
        al.add_last(table, bucket)
        
    
    my_map = {
        'prime' : prime,
        'capacity': capacity, 
        'scale' : scale, 
        'shift': shift, 
        'table' : table,
        'size' : 0,
        'limit_factor' : load_factor,
        'current_factor' : 0,
    }
    
    return my_map

def put(my_map, key, value):
    
    hash = mf.hash_value(my_map, key)
    
    bucket = al.get_element(my_map['table'], hash)
    
    entry = me.new_map_entry(key, value)
    
    pos = sl.is_present(bucket, key, default_compare)
    
    if pos >= 0:
        sl.change_info(bucket, pos, entry)
    else:
        sl.add_last(bucket, entry)
        my_map['size'] += 1
        my_map['current_factor'] = my_map['size'] / my_map['capacity']

        if my_map['current_factor'] > my_map['limit_factor']:
            rehash(my_map)
        
    return my_map

def contains(my_map, key):
    bucket = get(my_map, key)
    if bucket is not None:
        return True 
    else:
        return False
    

def get(my_map, key):
    pos = mf.hash_value(my_map, key)
    bucket = al.get_element(my_map['table'], pos)
    
    temp = bucket["first"]
    
    while temp is not None:
        data = temp["info"]
        if me.get_key(data) == key:
            return me.get_value(data)
        temp = temp["next"]
    
    return None
    
def remove(my_map, key):
    pos = mf.hash_value(my_map, key)
    bucket = al.get_element(my_map['table'],pos)
    
    current_node = bucket['first']
    previous_node = None
    removed = False
    while not removed and current_node is not None:
        if current_node['info']['key'] == key and not removed:
            if previous_node is None:
                bucket['first'] = current_node['next']
            else:
                previous_node['next'] = current_node['next']
            if bucket['last'] == current_node:
                bucket['last'] = previous_node
            bucket['size'] -= 1
            my_map['size'] -= 1
            my_map['current_factor'] = my_map['size'] / my_map['capacity']
            removed = True
        else:
            previous_node = current_node
        current_node = current_node['next']
    return my_map


def size(my_map):
    return my_map['size']


def is_empty(my_map):
    return my_map['size'] == 0

def key_set(my_map):
    keys = {
        'elements': [],
        'size': 0
    }
    table = my_map['table']  
    for bucket in table['elements']:
        current_node = bucket['first']
        while current_node is not None:
            key = current_node['info']['key']
            keys['elements'].append(key)
            keys['size'] += 1 
            current_node = current_node['next']
    return keys

def value_set(my_map):
    values = {
        'elements': [],
        'size': 0
    }
    table = my_map['table']
    for bucket in table['elements']:
        current_node = bucket['first']
        while current_node is not None:
            value = current_node['info']['value']
            values['elements'].append(value)
            values['size'] += 1
            current_node = current_node['next']

    return values
     

def rehash(my_map):
    new_capacity = mf.next_prime(my_map['capacity'] * 2)
    new_map_obj = new_map(my_map['size'], my_map['limit_factor'])
    old_table = my_map['table']
    for bucket in old_table['elements']:
        current_node = bucket['first']
        while current_node is not None:
            key = current_node['info']['key']
            value = current_node['info']['value']
            put(new_map_obj, key, value)
            current_node = current_node['next']
    my_map['capacity'] = new_map_obj['capacity']
    my_map['table'] = new_map_obj['table']
    my_map['size'] = new_map_obj['size']
    my_map['current_factor'] = my_map['size'] / my_map['capacity']
    my_map['prime'] = new_map_obj['prime']
    my_map['scale'] = new_map_obj['scale']
    my_map['shift'] = new_map_obj['shift']

    return my_map
    

def default_compare(key, element):
    if (key == me.get_key(element)):
        return 0
    else:
        return -1

