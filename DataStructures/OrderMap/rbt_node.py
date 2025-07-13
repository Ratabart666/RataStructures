from DataStructures.OrderMap import tree_traversal as tt

ARRAY = 'array'
SINGLE_LINKED = 'single_linked'
BLACK = 'black'
RED = 'red'


def new_node(key, value):
    node = {'key': key, 'value': value, 'size': 1,
            'left': None, 'right': None, 'color': RED}
    return node


def get_value(node):
    value = node['value'] if node else None
    return value


def get_key(node):
    key = node['key'] if node else None
    return key


def get_left(node):
    return node['left'] if node else None


def get_right(node):
    return node['right'] if node else None


def update_left(node, new_left):
    if node:
        node['left'] = new_left
        node = update_size(node)
    return node


def update_right(node, new_right):
    if node:
        node['right'] = new_right
        node = update_size(node)
    return node


def update_key(node, new_key):
    if node:
        node['key'] = new_key
    return node


def update_value(node, new_value):
    if node:
        node['value'] = new_value
    return node


def update_color(node, new_color):
    if node:
        node['color'] = new_color
    return node


def get_color(node):
    return node['color'] if node else BLACK


def size_tree(root):
    return root['size'] if root else 0


def update_size(node):
    if node:
        node['size'] = 1 + size_tree(get_left(node)) + \
            size_tree(get_right(node))
    return node


def insert_node(root, key, value, compare):
    if not root:
        root = new_node(key, value)
    elif compare(key, get_key(root)) == 0:
        root = update_value(root, value)
    elif compare(key, get_key(root)) < 0:
        new_left = insert_node(get_left(root), key, value, compare)
        root = update_left(root, new_left)
        root = balance(root)
    elif compare(key, get_key(root)) > 0:
        new_right = insert_node(get_right(root), key, value, compare)
        root = update_right(root, new_right)
        root = balance(root)
    return root


def get_node(root, key, compare):
    if not root:
        value = None
    elif compare(key, get_key(root)) == 0:
        value = get_value(root)
    elif compare(key, get_key(root)) < 0:
        value = get_node(get_left(root), key, compare)
    elif compare(key, get_key(root)) > 0:
        value = get_node(get_right(root), key, compare)
    return value


def remove_node(root, key, compare):
    if root:
        if compare(key, get_key(root)) < 0:
            if not is_red(get_left(root)) and not is_red(get_left(get_left(root))):
                root = move_red_left(root)
            new_left = remove_node(get_left(root), key, compare)
            root = update_left(root, new_left)
            root = balance(root)
        elif compare(key, get_key(root)) > 0:
            if is_red(get_left(root)):
                root = rotate_right(root)
            elif not is_red(get_right(root)) and not is_red(get_left(get_right(root))):
                root = move_red_right(root)
            new_right = remove_node(get_right(root), key, compare)
            root = update_right(root, new_right)
            root = balance(root)
        elif compare(key, get_key(root)) == 0:
            if not get_left(root) and not get_right(root):
                root = None
            elif not get_left(root):
                root = get_right(root)
            elif not get_right(root):
                root = get_left(root)
            elif get_left(root) and get_right(root):
                successor_key = get_min_node(get_right(root))
                successor_value = get_node(
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


def get_min_node(root):
    if not root:
        key = None
    elif not get_left(root):
        key = get_key(root)
    elif get_left(root):
        key = get_min_node(get_left(root))
    return key


def get_max_node(root):
    if not root:
        key = None
    elif not get_right(root):
        key = get_key(root)
    elif get_right(root):
        key = get_max_node(get_right(root))
    return key


def delete_min_tree(root):
    if root:
        if not get_left(root):
            root = get_right(root)
        elif get_left(root):
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


def rotate_left(node):
    right = get_right(node)
    node = update_right(node, get_left(right))
    right = update_left(right, node)
    right = update_color(right, get_color(node))
    node = update_color(node, RED)
    return right


def rotate_right(node):
    left = get_left(node)
    node = update_left(node, get_right(left))
    left = update_right(left, node)
    left = update_color(left, get_color(node))
    node = update_color(node, RED)
    return left


def flip_node_color(node):
    if node:
        new_color = RED if get_color(node) == BLACK else BLACK
        node = update_color(node, new_color)
    return node


def flip_colors(node):
    node = flip_node_color(node)
    node = update_left(node, flip_node_color(get_left(node)))
    node = update_right(node, flip_node_color(get_right(node)))
    return node


def is_red(node):
    return get_color(node) == RED if node else False


def move_red_left(node):
    node = flip_colors(node)
    if is_red(get_right(get_left(node))):
        node = update_right(node, rotate_right(get_right(node)))
        node = rotate_left(node)
        node = flip_colors(node)
    return node


def move_red_right(node):
    node = flip_colors(node)
    if is_red(get_left(get_left(node))):
        node = rotate_right(node)
        node = flip_colors(node)
    return node


def balance(node):
    if not is_red(get_left(node)) and is_red(get_right(node)):
        node = rotate_left(node)
        node = balance(node)
    elif is_red(get_left(node)) and is_red(get_left(get_left(node))):
        node = rotate_right(node)
        node = balance(node)
    elif is_red(get_left(node)) and is_red(get_right(node)):
        node = flip_colors(node)
        node = balance(node)
    return node
