from DataStructures.List import single_linked_list as lt
from DataStructures.List import array_list as al
from DataStructures.OrderMap import bst_node

ARRAY = 0
SINGLE_LINKED = 1


def default_compare(a, b):
    if a < b:
        return -1
    elif a == b:
        return 0
    elif a > b:
        return 1


def new_map(*, compare=None):
    bst = {
        'root': None,
        'compare': compare or default_compare
    }
    return bst


def get_root(tree):
    return tree['root']


def update_root(tree, new_root):
    tree['root'] = new_root
    return tree


def get_compare(tree):
    return tree['compare']


def put(bst, key, value):
    root = get_root(bst)
    compare = get_compare(bst)
    new_root = bst_node.insert_node(root, key, value, compare)
    bst = update_root(bst, new_root)
    return bst


def get(bst, key):
    root = get_root(bst)
    compare = get_compare(bst)
    return bst_node.get_node(root, key, compare)


def remove(bst, key):
    root = get_root(bst)
    compare = get_compare(bst)
    new_root = bst_node.remove_node(root, key, compare)
    bst = update_root(bst, new_root)
    return bst


def contains(bst, key):
    return bool(get(bst, key))


def size(bst):
    return bst_node.size_tree(get_root(bst))


def is_empty(bst):
    return bst_node.size_tree(get_root(bst)) == 0


def key_set(bst, *, list_type=SINGLE_LINKED):
    root = get_root(bst)
    compare = get_compare(bst)
    key_list = al.new_list() if list_type == ARRAY else lt.new_list()
    return bst_node.key_set_tree(root, key_list, compare, list_type=list_type)


def value_set(bst, *, list_type=SINGLE_LINKED):
    root = get_root(bst)
    compare = get_compare(bst)
    value_list = al.new_list() if list_type == ARRAY else lt.new_list()
    return bst_node.value_set_tree(root, value_list, compare, list_type=list_type)


def get_min(bst):
    root = get_root(bst)
    return bst_node.get_min_node(root)


def get_max(bst):
    root = get_root(bst)
    return bst_node.get_max_node(root)


def delete_min(bst):
    root = get_root(bst)
    new_root = bst_node.delete_min_tree(root)
    bst = update_root(bst, new_root)
    return bst


def delete_max(bst):
    root = get_root(bst)
    new_root = bst_node.delete_max_tree(root)
    bst = update_root(bst, new_root)
    return bst


def floor(bst, key):
    root = get_root(bst)
    compare = get_compare(bst)
    return bst_node.floor_key(root, key, compare)


def ceiling(bst, key):
    root = get_root(bst)
    compare = get_compare(bst)
    return bst_node.ceiling_key(root, key, compare)


def select(bst, pos):
    root = get_root(bst)
    return bst_node.select_key(root, pos)


def rank(bst, key):
    root = get_root(bst)
    compare = get_compare(bst)
    return bst_node.rank_key(root, key, compare)


def height(bst):
    root = get_root(bst)
    return bst_node.height_tree(root)


def keys(bst, key_initial, key_final, *, list_type=SINGLE_LINKED):
    root = get_root(bst)
    compare = get_compare(bst)
    key_list = al.new_list() if list_type == ARRAY else lt.new_list()
    return bst_node.keys_range(root, key_initial, key_final, key_list, compare, list_type=list_type)


def values(bst, key_initial, key_final, *, list_type=SINGLE_LINKED):
    root = get_root(bst)
    compare = get_compare(bst)
    value_list = al.new_list() if list_type == ARRAY else lt.new_list()
    return bst_node.values_range(root, key_initial, key_final, value_list, compare, list_type=list_type)
