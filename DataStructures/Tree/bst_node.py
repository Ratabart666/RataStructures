from DataStructures.List import single_linked_list as lt


def new_node(key, value):
    node = {'key': key, 'value': value, 'size': 1, 'left': None, 'right': None}
    return node


def get_value(my_node):
    value = my_node['value'] if my_node is not None else None
    return value


def get_key(my_node):
    key = my_node['key'] if my_node is not None else None
    return key


def insert_node(root, key, value):
    if root is None:
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
    if root is None:
        value = None
    elif key == get_key(root):
        value = get_value(root)
    elif key < get_key(root):
        value = get_node(root['left'], key)
    elif key > get_key(root):
        value = get_node(root['right'], key)
    return value


def remove_node(root, key):
    if root is not None:
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
            if root['left'] is None and root['right'] is None:
                root = None
            elif root['left'] is None:
                root = root['right']
            elif root['right'] is None:
                root = root['left']
            else:
                succesor_key = get_min_node(root['right'])
                succesor_value = get_node(root['right'], succesor_key)
                root['right'] = delete_min_tree(root['right'])
                root['key'] = succesor_key
                root['value'] = succesor_value
                root['size'] -= 1
    return root


def size_tree(root):
    size = root['size'] if root is not None else 0
    return size


def key_set_tree(root, key_list):
    if root is not None:
        key_list = key_set_tree(root['left'], key_list)
        key_list = lt.add_last(key_list, get_key(root))
        key_list = key_set_tree(root['right'], key_list)
    return key_list


def value_set_tree(root, value_list):
    if root is not None:
        value_list = value_set_tree(root['left'], value_list)
        value_list = lt.add_last(value_list, get_value(root))
        value_list = value_set_tree(root['right'], value_list)
    return value_list


def get_min_node(root):
    if root is None:
        key = None
    elif root['left'] is None:
        key = get_key(root)
    elif root['left'] is not None:
        key = get_min_node(root['left'])
    return key


def get_max_node(root):
    if root is None:
        key = None
    elif root['right'] is None:
        key = get_key(root)
    elif root['right'] is not None:
        key = get_max_node(root['right'])
    return key


def delete_min_tree(root):
    if root is not None:
        if root['left'] is None:
            root = root['right']
        else:
            root['left'] = delete_min_tree(root['left'])
            root['size'] -= 1
    return root


def delete_max_tree(root):
    if root is not None:
        if root['right'] is None:
            root = root['left']
        elif root['right'] is not None:
            root['right'] = delete_max_tree(root['right'])
            root['size'] -= 1
    return root


def floor_key(root, key):
    if root is None:
        floor = None
    elif root is not None:
        if key == get_key(root):
            floor = get_key(root)
        elif key < get_key(root):
            floor = floor_key(root['left'], key)
        elif key > get_key(root):
            if root['right'] is None or get_key(root['right']) > key:
                floor = get_key(root)
            if root['right'] is not None and get_key(root['right']) < key:
                floor = floor_key(root['right'], key)
    return floor


def ceiling_key(root, key):
    if root is None:
        ceiling = None
    else:
        if key == get_key(root):
            ceiling = get_key(root)
        elif key > get_key(root):
            ceiling = ceiling_key(root['right'], key)
        elif key < get_key(root):
            if root['left'] is None or get_key(root['left']) < key:
                ceiling = get_key(root)
            else:
                ceiling = ceiling_key(root['left'], key)
    return ceiling


def rank_keys(root, key):
    if root is None:
        rank = 0
    else:
        if key < get_key(root):
            rank = rank_keys(root['left'], key)
        elif key > get_key(root):
            rank_left = size_tree(root['left'])
            rank_right = rank_keys(root['right'], key)
            rank = rank_left + 1 + rank_right
        else:
            rank = size_tree(root['left'])
    return rank


def select_key(root, pos):
    if root is None:
        key = None
    elif root is not None:
        left_size = size_tree(root['left'])
        if pos == left_size:
            key = get_key(root)
        elif pos < left_size:
            key = select_key(root['left'], pos)
        elif pos > left_size:
            key = select_key(root['right'], pos - left_size - 1)
    return key


def height_tree(root):
    if root is None:
        return 0
    else:
        left_height = height_tree(root['left'])
        right_height = height_tree(root['right'])
        return 1 + max(left_height, right_height)


def keys_range(root, key_initial, key_final, key_list):
    if root is not None:
        current_key = get_key(root)
        if key_initial < current_key:
            key_list = keys_range(
                root['left'], key_initial, key_final, key_list)
        if key_initial <= current_key <= key_final:
            key_list = lt.add_last(key_list, current_key)
        if current_key < key_final:
            key_list = keys_range(
                root['right'], key_initial, key_final, key_list)
    return key_list


def values_range(root, key_initial, key_final, value_list):
    if root is not None:
        current_key = get_key(root)
        if key_initial < current_key:
            value_list = values_range(
                root['left'], key_initial, key_final, value_list)
        if key_initial <= current_key <= key_final:
            value_list = lt.add_last(value_list, get_value(root))
        if current_key < key_final:
            value_list = values_range(
                root['right'], key_initial, key_final, value_list)
    return value_list


def inorder_tree(root, node_list):
    if root is not None:
        node_list = inorder_tree(root['left'], node_list)
        node_list = lt.add_last(node_list, root)
        node_list = inorder_tree(root['right'], node_list)
    return node_list


def preorder_tree(root, node_list):
    if root is not None:
        node_list = lt.add_last(node_list, root)
        node_list = preorder_tree(root['left'], node_list)
        node_list = preorder_tree(root['right'], node_list)
    return node_list


def postorder_tree(root, node_list):
    if root is not None:
        node_list = postorder_tree(root['left'], node_list)
        node_list = postorder_tree(root['right'], node_list)
        node_list = lt.add_last(node_list, root)
    return node_list
