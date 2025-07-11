from DataStructures.Tree import bst_node
from DataStructures.List import single_linked_list as lt


def new_map():
    o_map = {'root': None}
    return o_map


def put(my_bst, key, value):
    my_bst['root'] = bst_node.insert_node(my_bst['root'], key, value)
    return my_bst


def get(my_bst, key):
    return bst_node.get_node(my_bst['root'], key)


def remove(my_bst, key):
    my_bst['root'] = bst_node.remove_node(my_bst['root'], key)
    return my_bst


def contains(my_bst, key):
    return bool(get(my_bst, key))


def size(my_bst):
    return bst_node.size_tree(my_bst['root'])


def is_empty(my_bst):
    return bst_node.size_tree(my_bst['root']) == 0


def key_set(my_bst):
    key_list = lt.new_list()
    return bst_node.key_set_tree(my_bst['root'], key_list)


def value_set(my_bst):
    value_list = lt.new_list()
    return bst_node.value_set_tree(my_bst['root'], value_list)


def get_min(my_bst):
    return bst_node.get_min_node(my_bst['root'])


def get_max(my_bst):
    return bst_node.get_max_node(my_bst['root'])


def delete_min(my_bst):
    my_bst['root'] = bst_node.delete_min_tree(my_bst['root'])
    return my_bst


def delete_max(my_bst):
    my_bst['root'] = bst_node.delete_max_tree(my_bst['root'])
    return my_bst


def floor(my_bst, key):
    return bst_node.floor_key(my_bst['root'], key)


def ceiling(my_bst, key):
    return bst_node.ceiling_key(my_bst['root'], key)


def select(my_bst, pos):
    return bst_node.select_key(my_bst['root'], pos)


def rank(my_bst, key):
    return bst_node.rank_key(my_bst['root'], key)


def height(my_bst):
    return bst_node.height_tree(my_bst['root'])


def keys(my_bst, key_initial, key_final):
    key_list = lt.new_list()
    return bst_node.keys_range(my_bst['root'], key_initial, key_final, key_list)


def values(my_bst, key_initial, key_final):
    value_list = lt.new_list()
    return bst_node.values_range(my_bst['root'], key_initial, key_final, value_list)
