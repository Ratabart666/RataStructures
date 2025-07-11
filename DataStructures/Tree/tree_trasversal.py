import DataStructures.List.single_linked_list as lt
import DataStructures.Tree.bst_node as bst


def inorder_tree(root, node_list, values=False, key_initial=None, key_final=None):
    if root:
        current_key = bst.get_key(root)

        if not key_initial or current_key > key_initial:
            node_list = inorder_tree(
                root['left'], node_list, values, key_initial, key_final)

        if (not key_initial or current_key >= key_initial) and (not key_final or current_key <= key_final):
            item = bst.get_value(root) if values else bst.get_key(root)
            node_list = lt.add_last(node_list, item)

        if not key_final or current_key < key_final:
            node_list = inorder_tree(
                root['right'], node_list, values, key_initial, key_final)

    return node_list


def preorder_tree(root, node_list, values=False, key_initial=None, key_final=None):
    if root:
        current_key = bst.get_key(root)

        if (not key_initial or current_key >= key_initial) and (not key_final or current_key <= key_final):
            item = bst.get_value(root) if values else bst.get_key(root)
            node_list = lt.add_last(node_list, item)

        if not key_initial or current_key > key_initial:
            node_list = preorder_tree(
                root['left'], node_list, values, key_initial, key_final)

        if not key_final or current_key < key_final:
            node_list = preorder_tree(
                root['right'], node_list, values, key_initial, key_final)

    return node_list


def postorder_tree(root, node_list, values=False, key_initial=None, key_final=None):
    if root:
        current_key = bst.get_key(root)

        if not key_initial or current_key > key_initial:
            node_list = postorder_tree(
                root['left'], node_list, values, key_initial, key_final)

        if not key_final or current_key < key_final:
            node_list = postorder_tree(
                root['right'], node_list, values, key_initial, key_final)

        if (not key_initial or current_key >= key_initial) and (not key_final or current_key <= key_final):
            item = bst.get_value(root) if values else bst.get_key(root)
            node_list = lt.add_last(node_list, item)

    return node_list
