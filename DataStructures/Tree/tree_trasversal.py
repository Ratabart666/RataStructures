import DataStructures.List.single_linked_list as lt
import DataStructures.Tree.bst_node as bst


def inorder(my_order_map):
    node_list = lt.new_list()
    if my_order_map is not None and my_order_map['root'] is not None:
        node_list = bst.inorder_tree(my_order_map['root'], node_list)
    return node_list


def preorder(my_order_map):
    node_list = lt.new_list()
    if my_order_map is not None and my_order_map['root'] is not None:
        node_list = bst.preorder_tree(my_order_map['root'], node_list)
    return node_list


def postorder(my_order_map):
    node_list = lt.new_list()
    if my_order_map is not None and my_order_map['root'] is not None:
        node_list = bst.postorder_tree(my_order_map['root'], node_list)
    return node_list
