from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
from DataStructures.List import array_list as lt
import random as rd
 
 
def new_map(num_elements, load_factor, prime=109345121):
     
     
     capacity = mf.next_prime(int(num_elements / load_factor))
     
     scale = rd.randint(1, prime - 1)
     shift = rd.randint(0, prime - 1)
     
     table = lt.new_list()
     
     for i in range(capacity):
         lt.add_last(table, me.new_map_entry(None, None))
     
     my_map = {
         'prime': prime,
         'capacity': capacity,
         'size': 0,
         'scale': scale,
         'shift': shift,
         'current_factor': 0,
         'limit_factor': load_factor,
         'table': table,
     }
     
     return my_map
 
def put(my_map, key, value):
     
     entry = me.new_map_entry(key, value)
     hash = mf.hash_value(my_map, key)
     position = find_slot(my_map, key, hash)
     
     
     my_map['table']['elements'][position[1]] = entry
     
     my_map['size'] += 1
     my_map['current_factor'] = my_map['size'] / my_map['capacity']
     if my_map['current_factor'] > my_map['limit_factor']:
         rehash(my_map)
     
     return my_map
 
def contains(my_map, key):
     hash = mf.hash_value(my_map, key)
     position = find_slot(my_map, key, hash)
     
     if position[0]:
         return True
     return False
 
def remove(my_map, key):
     
     hash = mf.hash_value(my_map, key)
     position = find_slot(my_map, key, hash)
     
     if position[0]:
         entry = lt.get_element(my_map["table"], position[1])
         entry['key'] = "__EMPTY__"
         entry['value'] = "__EMPTY__"
         my_map['size'] -= 1
         my_map['current_factor'] = my_map['size'] / my_map['capacity']
         return True
     return False
 
def get(my_map, key):
     hash = mf.hash_value(my_map, key)
     position = find_slot(my_map, key, hash)
     
     if position[0]:
         entry = lt.get_element(my_map["table"], position[1])
         return me.get_value(entry)
     return None
 
def size(my_map):
     return my_map['size']
 
def is_empty(my_map):
     
     if my_map['size'] == 0:
         return True
     return False
 
def key_set(my_map):
     keys = lt.new_list()
     
     capacity = my_map['capacity']
     for i in range(capacity):
         entry = lt.get_element(my_map["table"], i)
         if me.get_key(entry) is not None and me.get_key(entry) != "__EMPTY__":
             lt.add_last(keys, me.get_key(entry))
     
     return keys
 
def value_set(my_map):
     
     values = lt.new_list()
     
     capacity = my_map['capacity']
     for i in range(capacity):
         entry = lt.get_element(my_map["table"], i)
         if me.get_key(entry) is not None and me.get_key(entry) != "__EMPTY__":
             lt.add_last(values, me.get_value(entry))
     
     return values
 
def rehash(my_map):
     
     old_table = my_map['table']
     old_capacity = my_map['capacity']
     
     new_capacity = mf.next_prime(old_capacity * 2)
     my_map['capacity'] = new_capacity
     
     my_map['table'] = lt.new_list()
     for i in range(new_capacity):
         lt.add_last(my_map["table"], me.new_map_entry(None, None))
     my_map['size'] = 0
     my_map['current_factor'] = 0
     
     for entry in old_table['elements']:
         if me.get_key(entry) is not None and me.get_key(entry) != "__EMPTY__":
             key = me.get_key(entry)
             value = me.get_value(entry)
             put(my_map, key, value)
             
     return my_map
     
 
def find_slot(my_map, key, hash_value):
     first_avail = None
     found = False
     ocupied = False
     while not found:
         entry = lt.get_element(my_map["table"], hash_value)
         if is_available(my_map["table"], hash_value):
             if first_avail is None:
                 first_avail = hash_value
             if me.get_key(entry) is None:
                 found = True
             # Check if this is a removed slot (marked as __EMPTY__)
             elif me.get_key(entry) == "__EMPTY__" and first_avail is None:
                 first_avail = hash_value
         elif default_compare(key, entry) == 0:
             first_avail = hash_value
             found = True
             ocupied = True
         hash_value = (hash_value + 1) % my_map["capacity"]
     return ocupied, first_avail
 
def default_compare(key, entry):
 
     if key == me.get_key(entry):
         return 0
     elif key > me.get_key(entry):
         return 1
     return -1
 
def is_available(table, pos):
 
     entry = lt.get_element(table, pos)
     if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
         return True
     return False
