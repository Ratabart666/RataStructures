from DataStructures.Tree import tree_trasversal as tt


def new_node(key, value):
    node = {'key': key, 'value': value, 'size': 1, 'left': None, 'right': None}
    return node


def get_value(my_node):
    value = my_node['value'] if my_node else None
    return value


def get_key(my_node):
    key = my_node['key'] if my_node else None
    return key


def insert_node(root, key, value):
    if not root:
        root = new_node(key, value)
    elif key == get_key(root):
        root['value'] = value
    elif key < get_key(root):
        old_size = size_tree(root['left'])
        root['left'] = insert_node(root['left'], key, value)
        new_size = size_tree(root['left'])
        root['size'] += new_size - old_size
    elif key > get_key(root):
        old_size = size_tree(root['right'])
        root['right'] = insert_node(root['right'], key, value)
        new_size = size_tree(root['right'])
        root['size'] += new_size - old_size
    return root


def get_node(root, key):
    if not root:
        value = None
    elif key == get_key(root):
        value = get_value(root)
    elif key < get_key(root):
        value = get_node(root['left'], key)
    elif key > get_key(root):
        value = get_node(root['right'], key)
    return value


def remove_node(root, key):
    if root:
        if key < get_key(root):
            old_size = size_tree(root['left'])
            root['left'] = remove_node(root['left'], key)
            new_size = size_tree(root['left'])
            root['size'] -= old_size - new_size
        elif key > get_key(root):
            old_size = size_tree(root['right'])
            root['right'] = remove_node(root['right'], key)
            new_size = size_tree(root['right'])
            root['size'] -= old_size - new_size
        elif key == get_key(root):
            if not root['left'] and not root['right']:
                root = None
            elif not root['left']:
                root = root['right']
            elif not root['right']:
                root = root['left']
            elif root['left'] and root['right']:
                successor_key = get_min_node(root['right'])
                successor_value = get_node(root['right'], successor_key)
                root['right'] = delete_min_tree(root['right'])
                root['key'] = successor_key
                root['value'] = successor_value
                root['size'] -= 1
    return root


def size_tree(root):
    size = root['size'] if root else 0
    return size


def key_set_tree(root, key_list, *, list_type="single_linked"):
    return tt.inorder_tree(root, key_list, list_type=list_type)


def value_set_tree(root, value_list, *, list_type="single_linked"):
    return tt.inorder_tree(root, value_list, values=True, list_type=list_type)


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


def floor_key(root, key):
    if not root:
        floor = None
    elif key == get_key(root):
        floor = get_key(root)
    elif key < get_key(root):
        floor = floor_key(root['left'], key)
    elif key > get_key(root):
        right_floor = floor_key(root['right'], key)
        floor = right_floor if right_floor else get_key(root)
    return floor


def ceiling_key(root, key):
    if not root:
        ceiling = None
    elif key == get_key(root):
        ceiling = get_key(root)
    elif key > get_key(root):
        ceiling = ceiling_key(root['right'], key)
    elif key < get_key(root):
        left_ceiling = ceiling_key(root['left'], key)
        ceiling = left_ceiling if left_ceiling else get_key(root)
    return ceiling


def rank_key(root, key):
    if not root:
        rank = 0
    elif root:
        if key < get_key(root):
            rank = rank_key(root['left'], key)
        elif key > get_key(root):
            rank_left = size_tree(root['left'])
            rank_right = rank_key(root['right'], key)
            rank = rank_left + 1 + rank_right
        elif key == get_key(root):
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


def keys_range(root, key_initial, key_final, key_list, *, list_type="single_linked"):
    return tt.inorder_tree(root, key_list, key_initial=key_initial, key_final=key_final, list_type=list_type)


def values_range(root, key_initial, key_final, value_list, *, list_type="single_linked"):
    return tt.inorder_tree(root, value_list, values=True, key_initial=key_initial, key_final=key_final, list_type=list_type)
