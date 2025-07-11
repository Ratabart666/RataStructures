import DataStructures.List.single_linked_list as lt
from DataStructures.List import array_list as al
import DataStructures.Tree.bst_node as bst

# List type constants
ARRAY = 'array'
SINGLE_LINKED = 'single_linked'


def inorder_tree(root, node_list, *, values=False, key_initial=None, key_final=None, list_type=SINGLE_LINKED):
    if root:
        current_key = bst.get_key(root)

        if not key_initial or current_key > key_initial:
            node_list = inorder_tree(
                root['left'], node_list, values=values, key_initial=key_initial, key_final=key_final, list_type=list_type)

        if (not key_initial or current_key >= key_initial) and (not key_final or current_key <= key_final):
            extractor = bst.get_value if values else bst.get_key
            item = extractor(root)
            list_adder = al.add_last if list_type == ARRAY else lt.add_last
            node_list = list_adder(node_list, item)

        if not key_final or current_key < key_final:
            node_list = inorder_tree(
                root['right'], node_list, values=values, key_initial=key_initial, key_final=key_final, list_type=list_type)

    return node_list


def preorder_tree(root, node_list, *, values=False, key_initial=None, key_final=None, list_type=SINGLE_LINKED):
    if root:
        current_key = bst.get_key(root)

        if (not key_initial or current_key >= key_initial) and (not key_final or current_key <= key_final):
            extractor = bst.get_value if values else bst.get_key
            item = extractor(root)
            list_adder = al.add_last if list_type == ARRAY else lt.add_last
            node_list = list_adder(node_list, item)

        if not key_initial or current_key > key_initial:
            node_list = preorder_tree(
                root['left'], node_list, values=values, key_initial=key_initial, key_final=key_final, list_type=list_type)

        if not key_final or current_key < key_final:
            node_list = preorder_tree(
                root['right'], node_list, values=values, key_initial=key_initial, key_final=key_final, list_type=list_type)

    return node_list


def postorder_tree(root, node_list, *, values=False, key_initial=None, key_final=None, list_type=SINGLE_LINKED):
    if root:
        current_key = bst.get_key(root)

        if not key_initial or current_key > key_initial:
            node_list = postorder_tree(
                root['left'], node_list, values=values, key_initial=key_initial, key_final=key_final, list_type=list_type)

        if not key_final or current_key < key_final:
            node_list = postorder_tree(
                root['right'], node_list, values=values, key_initial=key_initial, key_final=key_final, list_type=list_type)

        if (not key_initial or current_key >= key_initial) and (not key_final or current_key <= key_final):
            extractor = bst.get_value if values else bst.get_key
            item = extractor(root)
            list_adder = al.add_last if list_type == ARRAY else lt.add_last
            node_list = list_adder(node_list, item)

    return node_list
