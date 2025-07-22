from DataStructures.List import single_linked_list as lt
from DataStructures.List import array_list as al
from DataStructures.OrderedMap import rbt_node

ARRAY = 'array'
SINGLE_LINKED = 'single_linked'


def default_compare(a, b):
    if a < b:
        return -1
    elif a == b:
        return 0
    elif a > b:
        return 1


def new_map(*, compare=None):
    rbt = {
        'root': None,
        'compare': compare or default_compare
    }
    return rbt


def get_root(rbt):
    return rbt['root']


def update_root(rbt, new_root):
    rbt['root'] = new_root
    return rbt


def get_compare(rbt):
    return rbt['compare']


def put(rbt, key, value):
    root = get_root(rbt)
    compare = get_compare(rbt)
    new_root = rbt_node.insert_node(root, key, value, compare)
    new_root = rbt_node.update_color(new_root, rbt_node.BLACK)
    rbt = update_root(rbt, new_root)
    return rbt


def get(rbt, key):
    root = get_root(rbt)
    compare = get_compare(rbt)
    return rbt_node.get_node(root, key, compare)


def remove(rbt, key):
    root = get_root(rbt)
    compare = get_compare(rbt)
    new_root = rbt_node.remove_node(root, key, compare)
    new_root = rbt_node.update_color(new_root, rbt_node.BLACK)
    rbt = update_root(rbt, new_root)
    return rbt


def contains(rbt, key):
    return bool(get(rbt, key))


def size(rbt):
    return rbt_node.size_tree(get_root(rbt))


def is_empty(rbt):
    return rbt_node.size_tree(get_root(rbt)) == 0


def key_set(rbt, *, list_type=SINGLE_LINKED):
    root = get_root(rbt)
    compare = get_compare(rbt)
    key_list = al.new_list() if list_type == ARRAY else lt.new_list()
    return rbt_node.key_set_tree(root, key_list, compare, list_type=list_type)


def value_set(rbt, *, list_type=SINGLE_LINKED):
    root = get_root(rbt)
    compare = get_compare(rbt)
    value_list = al.new_list() if list_type == ARRAY else lt.new_list()
    return rbt_node.value_set_tree(root, value_list, compare, list_type=list_type)


def get_min(rbt):
    root = get_root(rbt)
    return rbt_node.get_min_node(root)


def get_max(rbt):
    root = get_root(rbt)
    return rbt_node.get_max_node(root)


def delete_min(rbt):
    root = get_root(rbt)
    new_root = rbt_node.delete_min_tree(root)
    new_root = rbt_node.update_color(new_root, rbt_node.BLACK)
    rbt = update_root(rbt, new_root)
    return rbt


def delete_max(rbt):
    root = get_root(rbt)
    new_root = rbt_node.delete_max_tree(root)
    new_root = rbt_node.update_color(new_root, rbt_node.BLACK)
    rbt = update_root(rbt, new_root)
    return rbt


def floor(rbt, key):
    root = get_root(rbt)
    compare = get_compare(rbt)
    return rbt_node.floor_key(root, key, compare)


def ceiling(rbt, key):
    root = get_root(rbt)
    compare = get_compare(rbt)
    return rbt_node.ceiling_key(root, key, compare)


def select(rbt, pos):
    root = get_root(rbt)
    return rbt_node.select_key(root, pos)


def rank(rbt, key):
    root = get_root(rbt)
    compare = get_compare(rbt)
    return rbt_node.rank_key(root, key, compare)


def height(rbt):
    root = get_root(rbt)
    return rbt_node.height_tree(root)


def keys(rbt, key_initial, key_final, *, list_type=SINGLE_LINKED):
    root = get_root(rbt)
    compare = get_compare(rbt)
    key_list = al.new_list() if list_type == ARRAY else lt.new_list()
    return rbt_node.keys_range(root, key_initial, key_final, key_list, compare, list_type=list_type)


def values(rbt, key_initial, key_final, *, list_type=SINGLE_LINKED):
    root = get_root(rbt)
    compare = get_compare(rbt)
    value_list = al.new_list() if list_type == ARRAY else lt.new_list()
    return rbt_node.values_range(root, key_initial, key_final, value_list, compare, list_type=list_type)
