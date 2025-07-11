from DataStructures.List import single_linked_list as lt
from DataStructures.List import array_list as al
from DataStructures.Tree import bst_node

ARRAY = 'array'
SINGLE_LINKED = 'single_linked'


def new_map():
    bst = {'root': None}
    return bst


def put(bst, key, value):
    bst['root'] = bst_node.insert_node(bst['root'], key, value)
    return bst


def get(bst, key):
    return bst_node.get_node(bst['root'], key)


def remove(bst, key):
    bst['root'] = bst_node.remove_node(bst['root'], key)
    return bst


def contains(bst, key):
    return bool(get(bst, key))


def size(bst):
    return bst_node.size_tree(bst['root'])


def is_empty(bst):
    return bst_node.size_tree(bst['root']) == 0


def key_set(bst, *, list_type=SINGLE_LINKED):
    key_list = al.new_list() if list_type == ARRAY else lt.new_list()
    return bst_node.key_set_tree(bst['root'], key_list, list_type=list_type)


def value_set(bst, *, list_type=SINGLE_LINKED):
    value_list = al.new_list() if list_type == ARRAY else lt.new_list()
    return bst_node.value_set_tree(bst['root'], value_list, list_type=list_type)


def get_min(bst):
    return bst_node.get_min_node(bst['root'])


def get_max(bst):
    return bst_node.get_max_node(bst['root'])


def delete_min(bst):
    bst['root'] = bst_node.delete_min_tree(bst['root'])
    return bst


def delete_max(bst):
    bst['root'] = bst_node.delete_max_tree(bst['root'])
    return bst


def floor(bst, key):
    return bst_node.floor_key(bst['root'], key)


def ceiling(bst, key):
    return bst_node.ceiling_key(bst['root'], key)


def select(bst, pos):
    return bst_node.select_key(bst['root'], pos)


def rank(bst, key):
    return bst_node.rank_key(bst['root'], key)


def height(bst):
    return bst_node.height_tree(bst['root'])


def keys(bst, key_initial, key_final, *, list_type=SINGLE_LINKED):
    key_list = al.new_list() if list_type == ARRAY else lt.new_list()
    return bst_node.keys_range(bst['root'], key_initial, key_final, key_list, list_type=list_type)


def values(bst, key_initial, key_final, *, list_type=SINGLE_LINKED):
    value_list = al.new_list() if list_type == ARRAY else lt.new_list()
    return bst_node.values_range(bst['root'], key_initial, key_final, value_list, list_type=list_type)
