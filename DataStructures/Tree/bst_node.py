from DataStructures.Tree import tree_trasversal as tt

ARRAY = 'array'
SINGLE_LINKED = 'single_linked'


def new_node(key, value):
    node = {'key': key, 'value': value, 'size': 1, 'left': None, 'right': None}
    return node


def get_value(node):
    value = node['value'] if node else None
    return value


def get_key(node):
    key = node['key'] if node else None
    return key


def insert_node(root, key, value, compare):
    if not root:
        root = new_node(key, value)
    elif compare(key, get_key(root)) == 0:
        root['value'] = value
    elif compare(key, get_key(root)) < 0:
        old_size = size_tree(root['left'])
        root['left'] = insert_node(
            root['left'], key, value, compare)
        new_size = size_tree(root['left'])
        root['size'] += new_size - old_size
    else:
        old_size = size_tree(root['right'])
        root['right'] = insert_node(
            root['right'], key, value, compare)
        new_size = size_tree(root['right'])
        root['size'] += new_size - old_size
    return root


def get_node(root, key, compare):
    if not root:
        value = None
    elif compare(key, get_key(root)) == 0:
        value = get_value(root)
    elif compare(key, get_key(root)) < 0:
        value = get_node(root['left'], key, compare)
    else:
        value = get_node(root['right'], key, compare)
    return value


def remove_node(root, key, compare):
    if root:
        if compare(key, get_key(root)) < 0:
            old_size = size_tree(root['left'])
            root['left'] = remove_node(
                root['left'], key, compare)
            new_size = size_tree(root['left'])
            root['size'] -= old_size - new_size
        elif compare(key, get_key(root)) > 0:
            old_size = size_tree(root['right'])
            root['right'] = remove_node(
                root['right'], key, compare)
            new_size = size_tree(root['right'])
            root['size'] -= old_size - new_size
        else:
            if not root['left'] and not root['right']:
                root = None
            elif not root['left']:
                root = root['right']
            elif not root['right']:
                root = root['left']
            elif root['left'] and root['right']:
                successor_key = get_min_node(root['right'])
                successor_value = get_node(
                    root['right'], successor_key, compare)
                root['right'] = delete_min_tree(root['right'])
                root['key'] = successor_key
                root['value'] = successor_value
                root['size'] -= 1
    return root


def size_tree(root):
    return root['size'] if root else 0


def key_set_tree(root, key_list, compare, *, list_type=SINGLE_LINKED):
    return tt.inorder_tree(root, key_list, compare, list_type=list_type)


def value_set_tree(root, value_list, compare, *, list_type=SINGLE_LINKED):
    return tt.inorder_tree(root, value_list, compare, values=True, list_type=list_type)


def get_min_node(root):
    if not root:
        key = None
    elif not root['left']:
        key = get_key(root)
    elif root['left']:
        key = get_min_node(root['left'])
    return key


def get_max_node(root):
    if not root:
        key = None
    elif not root['right']:
        key = get_key(root)
    elif root['right']:
        key = get_max_node(root['right'])
    return key


def delete_min_tree(root):
    if root:
        if not root['left']:
            root = root['right']
        else:
            root['left'] = delete_min_tree(root['left'])
            root['size'] -= 1
    return root


def delete_max_tree(root):
    if root:
        if not root['right']:
            root = root['left']
        elif root['right']:
            root['right'] = delete_max_tree(root['right'])
            root['size'] -= 1
    return root


def floor_key(root, key, compare):
    if not root:
        floor = None
    elif compare(key, get_key(root)) == 0:
        floor = get_key(root)
    elif compare(key, get_key(root)) < 0:
        floor = floor_key(root['left'], key, compare)
    else:
        right_floor = floor_key(
            root['right'], key, compare)
        floor = right_floor if right_floor else get_key(root)
    return floor


def ceiling_key(root, key, compare):
    if not root:
        ceiling = None
    else:
        if compare(key, get_key(root)) == 0:
            ceiling = get_key(root)
        elif compare(key, get_key(root)) > 0:
            ceiling = ceiling_key(
                root['right'], key, compare)
        else:
            left_ceiling = ceiling_key(
                root['left'], key, compare)
            ceiling = left_ceiling if left_ceiling else get_key(root)
    return ceiling


def rank_key(root, key, compare):
    if not root:
        rank = 0
    else:
        if compare(key, get_key(root)) < 0:
            rank = rank_key(root['left'], key, compare)
        elif compare(key, get_key(root)) > 0:
            rank_left = size_tree(root['left'])
            rank_right = rank_key(
                root['right'], key, compare)
            rank = rank_left + 1 + rank_right
        else:
            rank = size_tree(root['left'])
    return rank


def select_key(root, pos):
    if not root:
        key = None
    elif root:
        left_size = size_tree(root['left'])
        if pos == left_size:
            key = get_key(root)
        elif pos < left_size:
            key = select_key(root['left'], pos)
        elif pos > left_size:
            key = select_key(root['right'], pos - left_size - 1)
    return key


def height_tree(root):
    if not root:
        return -1
    elif root:
        left_height = height_tree(root['left'])
        right_height = height_tree(root['right'])
        return 1 + max(left_height, right_height)


def keys_range(root, key_initial, key_final, key_list, compare, *, list_type=SINGLE_LINKED):
    return tt.inorder_tree(root, key_list, compare, key_initial=key_initial, key_final=key_final, list_type=list_type)


def values_range(root, key_initial, key_final, value_list, compare, *, list_type=SINGLE_LINKED):
    return tt.inorder_tree(root, value_list, compare, values=True, key_initial=key_initial, key_final=key_final, list_type=list_type)
