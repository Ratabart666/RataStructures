import DataStructures.List.single_linked_list as lt
import DataStructures.Tree.bst_node as bst


def _is_in_range(key, key_initial, key_final):
    return (not key_initial or key >= key_initial) and (not key_final or key <= key_final)


def _should_visit_left(current_key, key_initial):
    return not key_initial or current_key > key_initial


def _should_visit_right(current_key, key_final):
    return not key_final or current_key < key_final


def inorder_tree(root, node_list, values=False, key_initial=None, key_final=None):
    if root:
        current_key = bst.get_key(root)

        if _should_visit_left(current_key, key_initial):
            node_list = inorder_tree(
                root['left'], node_list, values, key_initial, key_final)

        if _is_in_range(current_key, key_initial, key_final):
            extractor = bst.get_value if values else bst.get_key
            item = extractor(root)
            node_list = lt.add_last(node_list, item)

        if _should_visit_right(current_key, key_final):
            node_list = inorder_tree(
                root['right'], node_list, values, key_initial, key_final)

    return node_list


def preorder_tree(root, node_list, values=False, key_initial=None, key_final=None):
    if root:
        current_key = bst.get_key(root)

        if _is_in_range(current_key, key_initial, key_final):
            extractor = bst.get_value if values else bst.get_key
            item = extractor(root)
            node_list = lt.add_last(node_list, item)

        if _should_visit_left(current_key, key_initial):
            node_list = preorder_tree(
                root['left'], node_list, values, key_initial, key_final)

        if _should_visit_right(current_key, key_final):
            node_list = preorder_tree(
                root['right'], node_list, values, key_initial, key_final)

    return node_list


def postorder_tree(root, node_list, values=False, key_initial=None, key_final=None):
    if root:
        current_key = bst.get_key(root)

        if _should_visit_left(current_key, key_initial):
            node_list = postorder_tree(
                root['left'], node_list, values, key_initial, key_final)

        if _should_visit_right(current_key, key_final):
            node_list = postorder_tree(
                root['right'], node_list, values, key_initial, key_final)

        if _is_in_range(current_key, key_initial, key_final):
            extractor = bst.get_value if values else bst.get_key
            item = extractor(root)
            node_list = lt.add_last(node_list, item)

    return node_list
