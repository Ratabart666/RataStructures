from DataStructures.OrderMap import tree_traversal as tt

ARRAY = 'array'
SINGLE_LINKED = 'single_linked'


def new_bst_node(key, value):
    bst_node = {'key': key, 'value': value,
                'size': 1, 'left': None, 'right': None}
    return bst_node


def get_value(bst_node):
    value = bst_node['value'] if bst_node else None
    return value


def get_key(bst_node):
    key = bst_node['key'] if bst_node else None
    return key


def get_left(bst_node):
    return bst_node['left'] if bst_node else None


def get_right(bst_node):
    return bst_node['right'] if bst_node else None


def update_left(bst_node, new_left):
    if bst_node:
        bst_node['left'] = new_left
        bst_node = update_size(bst_node)
    return bst_node


def update_right(bst_node, new_right):
    if bst_node:
        bst_node['right'] = new_right
        bst_node = update_size(bst_node)
    return bst_node


def update_key(bst_node, new_key):
    if bst_node:
        bst_node['key'] = new_key
    return bst_node


def update_value(bst_node, new_value):
    if bst_node:
        bst_node['value'] = new_value
    return bst_node


def update_size(bst_node):
    if bst_node:
        bst_node['size'] = 1 + size_tree(get_left(bst_node)) + \
            size_tree(get_right(bst_node))
    return bst_node


def size_tree(root):
    return root['size'] if root else 0


def insert_bst_node(root, key, value, compare):
    if not root:
        root = new_bst_node(key, value)
    elif compare(key, get_key(root)) == 0:
        root = update_value(root, value)
    elif compare(key, get_key(root)) < 0:
        new_left = insert_bst_node(get_left(root), key, value, compare)
        root = update_left(root, new_left)
    elif compare(key, get_key(root)) > 0:
        new_right = insert_bst_node(get_right(root), key, value, compare)
        root = update_right(root, new_right)
    return root


def get_bst_node(root, key, compare):
    if not root:
        value = None
    elif compare(key, get_key(root)) == 0:
        value = get_value(root)
    elif compare(key, get_key(root)) < 0:
        value = get_bst_node(get_left(root), key, compare)
    elif compare(key, get_key(root)) > 0:
        value = get_bst_node(get_right(root), key, compare)
    return value


def remove_bst_node(root, key, compare):
    if root:
        if compare(key, get_key(root)) < 0:
            new_left = remove_bst_node(get_left(root), key, compare)
            root = update_left(root, new_left)
        elif compare(key, get_key(root)) > 0:
            new_right = remove_bst_node(get_right(root), key, compare)
            root = update_right(root, new_right)
        elif compare(key, get_key(root)) == 0:
            if not get_left(root) and not get_right(root):
                root = None
            elif not get_left(root):
                root = get_right(root)
            elif not get_right(root):
                root = get_left(root)
            elif get_left(root) and get_right(root):
                successor_key = get_min_bst_node(get_right(root))
                successor_value = get_bst_node(
                    get_right(root), successor_key, compare)
                new_right = delete_min_tree(get_right(root))
                root = update_right(root, new_right)
                root = update_key(root, successor_key)
                root = update_value(root, successor_value)
    return root


def key_set_tree(root, key_list, compare, *, list_type=SINGLE_LINKED):
    return tt.inorder_tree(root, key_list, compare, list_type=list_type)


def value_set_tree(root, value_list, compare, *, list_type=SINGLE_LINKED):
    return tt.inorder_tree(root, value_list, compare, values=True, list_type=list_type)


def get_min_bst_node(root):
    if not root:
        key = None
    elif not get_left(root):
        key = get_key(root)
    elif get_left(root):
        key = get_min_bst_node(get_left(root))
    return key


def get_max_bst_node(root):
    if not root:
        key = None
    elif not get_right(root):
        key = get_key(root)
    elif get_right(root):
        key = get_max_bst_node(get_right(root))
    return key


def delete_min_tree(root):
    if root:
        if not get_left(root):
            root = get_right(root)
        if get_left(root):
            new_left = delete_min_tree(get_left(root))
            root = update_left(root, new_left)
    return root


def delete_max_tree(root):
    if root:
        if not get_right(root):
            root = get_left(root)
        elif get_right(root):
            new_right = delete_max_tree(get_right(root))
            root = update_right(root, new_right)
    return root


def floor_key(root, key, compare):
    if not root:
        floor = None
    elif compare(key, get_key(root)) == 0:
        floor = get_key(root)
    elif compare(key, get_key(root)) < 0:
        floor = floor_key(get_left(root), key, compare)
    elif compare(key, get_key(root)) > 0:
        right_floor = floor_key(get_right(root), key, compare)
        floor = right_floor if right_floor else get_key(root)
    return floor


def ceiling_key(root, key, compare):
    if not root:
        ceiling = None
    if root:
        if compare(key, get_key(root)) == 0:
            ceiling = get_key(root)
        elif compare(key, get_key(root)) > 0:
            ceiling = ceiling_key(get_right(root), key, compare)
        elif compare(key, get_key(root)) < 0:
            left_ceiling = ceiling_key(get_left(root), key, compare)
            ceiling = left_ceiling if left_ceiling else get_key(root)
    return ceiling


def rank_key(root, key, compare):
    if not root:
        rank = 0
    elif root:
        if compare(key, get_key(root)) < 0:
            rank = rank_key(get_left(root), key, compare)
        elif compare(key, get_key(root)) > 0:
            rank_left = size_tree(get_left(root))
            rank_right = rank_key(get_right(root), key, compare)
            rank = rank_left + 1 + rank_right
        elif compare(key, get_key(root)) == 0:
            rank = size_tree(get_left(root))
    return rank


def select_key(root, pos):
    if not root:
        key = None
    elif root:
        left_size = size_tree(get_left(root))
        if pos == left_size:
            key = get_key(root)
        elif pos < left_size:
            key = select_key(get_left(root), pos)
        elif pos > left_size:
            key = select_key(get_right(root), pos - left_size - 1)
    return key


def height_tree(root):
    if not root:
        return -1
    elif root:
        left_height = height_tree(get_left(root))
        right_height = height_tree(get_right(root))
        return 1 + max(left_height, right_height)


def keys_range(root, key_initial, key_final, key_list, compare, *, list_type=SINGLE_LINKED):
    return tt.inorder_tree(root, key_list, compare, key_initial=key_initial, key_final=key_final, list_type=list_type)


def values_range(root, key_initial, key_final, value_list, compare, *, list_type=SINGLE_LINKED):
    return tt.inorder_tree(root, value_list, compare, values=True, key_initial=key_initial, key_final=key_final, list_type=list_type)
