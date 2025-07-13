from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Tree import rbt_node as rbt_node
from DataStructures.Utils.utils import handle_not_implemented


def setup_tests():
    empty_tree = rbt.new_rbt()

    return empty_tree


def setup_three_nodes():
    three_nodes = rbt.new_rbt()
    node_1 = rbt_node.new_node(1, 1)
    node_3 = rbt_node.new_node(10, 10)
    node_2 = rbt_node.new_node(5, 5)

    node_1["parent"] = node_2
    node_2["left"] = node_1
    node_2["right"] = node_3
    node_2["size"] = 3
    node_3["parent"] = node_2

    three_nodes["root"] = node_2

    return three_nodes


@handle_not_implemented
def test_new_red_black_tree():
    empty_rbt = rbt.new_rbt()

    assert empty_rbt["root"] is None


@handle_not_implemented
def test_put():
    empty_tree = rbt.new_rbt()

    result = rbt.put(empty_tree, 5, "test")

    assert isinstance(result, dict)
    assert "root" in result


@handle_not_implemented
def test_get():
    empty_tree = rbt.new_rbt()

    result = rbt.get(empty_tree, 5)

    assert result is None


@handle_not_implemented
def test_remove():
    empty_tree = rbt.new_rbt()

    result = rbt.remove(empty_tree, 5)

    assert isinstance(result, dict)
    assert "root" in result


@handle_not_implemented
def test_contains():
    empty_tree = rbt.new_rbt()

    result = rbt.contains(empty_tree, 10)

    assert isinstance(result, bool)


@handle_not_implemented
def test_size():
    empty_tree = rbt.new_rbt()

    result = rbt.size(empty_tree)

    assert isinstance(result, int)


@handle_not_implemented
def test_is_empty():
    empty_rbt = setup_tests()
    three_rbt = setup_three_nodes()

    assert rbt.is_empty(empty_rbt)

    assert not rbt.is_empty(three_rbt)


@handle_not_implemented
def test_key_set():
    empty_tree = rbt.new_rbt()

    result = rbt.key_set(empty_tree)

    count = 0
    current = result["first"]
    while current is not None:
        count += 1
        current = current["next"]

    assert count == 0


@handle_not_implemented
def test_value_set():
    empty_tree = rbt.new_rbt()

    result = rbt.value_set(empty_tree)

    count = 0
    current = result["first"]
    while current is not None:
        count += 1
        current = current["next"]

    assert count == 0


@handle_not_implemented
def test_get_min():
    empty_tree = rbt.new_rbt()
    assert rbt.get_min(empty_tree) is None

    # Insertar nodos
    tree = rbt.new_rbt()
    rbt.put(tree, 30, "A")
    rbt.put(tree, 10, "B")
    rbt.put(tree, 20, "C")
    rbt.put(tree, 5, "D")
    rbt.put(tree, 40, "E")

    assert rbt.get_min(tree) == 5


@handle_not_implemented
def test_get_max():
    empty_tree = rbt.new_rbt()
    assert rbt.get_max(empty_tree) is None

    tree = rbt.new_rbt()
    rbt.put(tree, 15, "A")
    rbt.put(tree, 10, "B")
    rbt.put(tree, 5, "C")
    rbt.put(tree, 20, "D")

    assert rbt.get_max(tree) == 20


@handle_not_implemented
def test_delete_min():
    tree = rbt.new_rbt()

    rbt.put(tree, 50, "a")
    rbt.put(tree, 30, "b")
    rbt.put(tree, 70, "c")
    rbt.put(tree, 10, "d")
    rbt.put(tree, 40, "e")

    assert rbt.get_min(tree) == 10

    rbt.delete_min(tree)

    assert rbt.get_min(tree) == 30


@handle_not_implemented
def test_delete_max():

    empty_tree = rbt.new_rbt()
    rbt.delete_max(empty_tree)
    assert empty_tree["root"] is None

    tree = rbt.new_rbt()
    rbt.put(tree, 30, "A")
    rbt.put(tree, 10, "B")
    rbt.put(tree, 40, "C")
    rbt.put(tree, 35, "D")

    tree = rbt.delete_max(tree)
    assert rbt.get_max(tree) == 35

    tree = rbt.delete_max(tree)
    assert rbt.get_max(tree) == 30


@handle_not_implemented
def test_floor():
    tree = rbt.new_rbt()

    rbt.put(tree, 10, "a")
    rbt.put(tree, 20, "b")
    rbt.put(tree, 30, "c")
    rbt.put(tree, 40, "d")
    rbt.put(tree, 50, "e")

    assert rbt.floor(tree, 10) == 10
    assert rbt.floor(tree, 20) == 20

    assert rbt.floor(tree, 25) == 20
    assert rbt.floor(tree, 45) == 40

    assert rbt.floor(tree, 5) is None
    assert rbt.floor(tree, 60) == 50


@handle_not_implemented
def test_ceiling():
    tree = rbt.new_rbt()

    rbt.put(tree, 10, "a")
    rbt.put(tree, 20, "b")
    rbt.put(tree, 30, "c")
    rbt.put(tree, 40, "d")
    rbt.put(tree, 50, "e")

    assert rbt.ceiling(tree, 10) == 10
    assert rbt.ceiling(tree, 20) == 20

    assert rbt.ceiling(tree, 25) == 30
    assert rbt.ceiling(tree, 45) == 50

    # Casos extremos
    assert rbt.ceiling(tree, 5) == 10
    assert rbt.ceiling(tree, 60) is None


@handle_not_implemented
def test_select():
    tree = rbt.new_rbt()
    rbt.put(tree, 10, "a")
    key = rbt.select(tree, 0)
    assert key is None or isinstance(key, (int, float, str))


@handle_not_implemented
def test_rank():
    tree = rbt.new_rbt()
    rbt.put(tree, 10, "a")
    r = rbt.rank(tree, 10)
    assert isinstance(r, int)


@handle_not_implemented
def test_heigh():
    tree = rbt.new_rbt()
    rbt.put(tree, 10, "a")
    h = rbt.height(tree)
    assert isinstance(h, int)


@handle_not_implemented
def test_keys():
    tree = rbt.new_rbt()
    rbt.put(tree, 10, "a")
    rbt.put(tree, 20, "b")
    keys = rbt.keys(tree, 5, 25)
    assert isinstance(keys, object)


@handle_not_implemented
def test_values():
    tree = rbt.new_rbt()
    rbt.put(tree, 10, "a")
    rbt.put(tree, 20, "b")
    values = rbt.values(tree, 5, 25)
    assert isinstance(values, object)
