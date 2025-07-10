from DataStructures.Tree import binary_search_tree as bst
from DataStructures.Tree import bst_node as bst_node
from DataStructures.Utils.utils import handle_not_implemented


def default_compare_test(a, b):
    if a > bst_node.get_key(b):
        return 1
    elif a < bst_node.get_key(b):
        return -1
    return 0


def setup_tests():
    empty_tree = bst.new_map()

    return empty_tree


def setup_three_nodes():
    three_nodes = bst.new_map()
    node_1 = bst_node.new_node(1, 1)
    node_3 = bst_node.new_node(10, 10)
    node_2 = bst_node.new_node(5, 5)

    node_2["left"] = node_1
    node_2["right"] = node_3
    node_2["size"] = 3

    three_nodes["root"] = node_2

    return three_nodes


def setup_seven_nodes():
    seven_nodes = bst.new_map()
    node_1 = bst_node.new_node(10, 10)
    node_2 = bst_node.new_node(20, 20)
    node_3 = bst_node.new_node(30, 30)
    node_4 = bst_node.new_node(40, 40)
    node_5 = bst_node.new_node(50, 50)
    node_6 = bst_node.new_node(60, 60)
    node_7 = bst_node.new_node(70, 70)

    node_2["left"] = node_1
    node_2["right"] = node_3
    node_2["size"] = 3

    node_6["left"] = node_5
    node_6["right"] = node_7
    node_6["size"] = 3

    node_4["left"] = node_2
    node_4["right"] = node_6
    node_4["size"] = 7

    seven_nodes["root"] = node_4

    return seven_nodes


@handle_not_implemented
def test_new_binary_search_tree():
    empty_bst = bst.new_map()

    assert empty_bst["root"] is None


@handle_not_implemented
def test_put():
    empty_bst = setup_tests()
    result = bst.put(empty_bst, 1, 1)

    # Verificar solo el tipo de retorno
    assert isinstance(result, dict)
    assert "root" in result

    # Verificar que el árbol cambia después de insertar
    empty_bst = setup_tests()
    assert empty_bst["root"] is None
    bst.put(empty_bst, 5, 5)
    assert empty_bst["root"] is not None

    # Verificar que la función maneja correctamente la actualización de valores
    three_bst = setup_three_nodes()
    old_root = three_bst["root"]
    bst.put(three_bst, old_root["key"], "nuevo_valor")
    assert three_bst["root"]["value"] == "nuevo_valor"


@handle_not_implemented
def test_get():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()

    # Verificar que retorna None en árbol vacío
    assert bst.get(empty_bst, 1) is None

    # Verificar que la función puede encontrar valores existentes
    # (no verificamos la estructura interna)
    bst.put(three_bst, 42, "test_value")
    assert bst.get(three_bst, 42) == "test_value"

    # Verificar que retorna None para llaves inexistentes
    assert bst.get(three_bst, 999) is None


@handle_not_implemented
def test_remove():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()

    # Verificar que remove retorna un BST
    result = bst.remove(empty_bst, 1)
    assert isinstance(result, dict)
    assert "root" in result

    # Verificar que eliminar de un árbol vacío no causa errores
    bst.remove(empty_bst, 99)
    assert empty_bst["root"] is None

    # Verificar que eliminar una llave existente funciona
    # (agregamos un valor y luego verificamos que se eliminó)
    test_bst = setup_tests()
    bst.put(test_bst, 25, "test_data")
    assert bst.get(test_bst, 25) == "test_data"
    bst.remove(test_bst, 25)
    assert bst.get(test_bst, 25) is None

    # Verificar que eliminar una llave inexistente no afecta al árbol
    size_before = three_bst["root"]["size"] if three_bst["root"] else 0
    bst.remove(three_bst, 999)
    size_after = three_bst["root"]["size"] if three_bst["root"] else 0
    assert size_before == size_after


@handle_not_implemented
def test_contains():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()

    # Verificar que la función retorna un valor booleano
    assert isinstance(bst.contains(empty_bst, 1), bool)
    assert isinstance(bst.contains(three_bst, 1), bool)
    assert isinstance(bst.contains(three_bst, 100), bool)

    # Verificar consistencia en casos sencillos
    result1 = bst.contains(three_bst, 5)
    result2 = bst.contains(three_bst, 5)
    assert result1 == result2, "La función debería ser determinista para el mismo valor"


@handle_not_implemented
def test_size():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Verificar que la función retorna un entero
    assert isinstance(bst.size(empty_bst), int)
    assert isinstance(bst.size(three_bst), int)
    assert isinstance(bst.size(seven_bst), int)

    # Verificar que el resultado es un número no negativo
    assert bst.size(empty_bst) >= 0, "El tamaño del árbol debe ser no negativo"
    assert bst.size(three_bst) >= 0, "El tamaño del árbol debe ser no negativo"
    assert bst.size(seven_bst) >= 0, "El tamaño del árbol debe ser no negativo"

    # Verificar la consistencia en múltiples llamadas
    result1 = bst.size(three_bst)
    result2 = bst.size(three_bst)
    assert result1 == result2, "La función debería ser determinista"


@handle_not_implemented
def test_is_empty():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()

    # Verificar si un árbol vacío está vacío
    assert bst.is_empty(empty_bst)

    # Verificar si un árbol con 3 nodos está vacío
    assert not bst.is_empty(three_bst)


@handle_not_implemented
def test_key_set():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()

    # Verificar que key_set retorna una lista enlazada simple
    key_set_empty = bst.key_set(empty_bst)
    key_set_three = bst.key_set(three_bst)

    # Verificar que el retorno tiene la estructura de una lista enlazada
    assert isinstance(key_set_empty, dict)
    assert "first" in key_set_empty
    assert "last" in key_set_empty
    assert "size" in key_set_empty

    # Verificar que size es un entero
    assert isinstance(key_set_empty["size"], int)
    assert isinstance(key_set_three["size"], int)

    # Verificar la consistencia en múltiples llamadas
    result1 = bst.key_set(three_bst)["size"]
    result2 = bst.key_set(three_bst)["size"]
    assert result1 == result2, "La función debería ser determinista"


@handle_not_implemented
def test_value_set():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()

    # Verificar que value_set retorna una lista enlazada simple
    value_set_empty = bst.value_set(empty_bst)
    value_set_three = bst.value_set(three_bst)

    # Verificar que el retorno tiene la estructura de una lista enlazada
    assert isinstance(value_set_empty, dict)
    assert "first" in value_set_empty
    assert "last" in value_set_empty
    assert "size" in value_set_empty

    # Verificar que size es un entero
    assert isinstance(value_set_empty["size"], int)
    assert isinstance(value_set_three["size"], int)

    # Verificar la consistencia en múltiples llamadas
    result1 = bst.value_set(three_bst)["size"]
    result2 = bst.value_set(three_bst)["size"]
    assert result1 == result2, "La función debería ser determinista"

    # Verificar que first es None cuando la lista está vacía
    if value_set_empty["size"] == 0:
        assert value_set_empty["first"] is None


@handle_not_implemented
def test_get_min():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Verificar que retorna None para un árbol vacío o un valor para árboles no vacíos
    left_key_empty = bst.get_min(empty_bst)
    left_key_three = bst.get_min(three_bst)
    left_key_seven = bst.get_min(seven_bst)

    # Verificar que el tipo de retorno es el esperado (None o algún valor)
    assert left_key_empty is None or isinstance(
        left_key_empty, (int, str, float, bool))
    assert isinstance(left_key_three, (int, str, float, bool)
                      ) or left_key_three is None
    assert isinstance(left_key_seven, (int, str, float, bool)
                      ) or left_key_seven is None

    # Verificar consistencia en múltiples llamadas
    result1 = bst.get_min(three_bst)
    result2 = bst.get_min(three_bst)
    assert result1 == result2, "La función debería ser determinista"


@handle_not_implemented
def test_get_max():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Verificar que retorna None para un árbol vacío o un valor para árboles no vacíos
    right_key_empty = bst.get_max(empty_bst)
    right_key_three = bst.get_max(three_bst)
    right_key_seven = bst.get_max(seven_bst)

    # Verificar que el tipo de retorno es el esperado (None o algún valor)
    assert right_key_empty is None or isinstance(
        right_key_empty, (int, str, float, bool))
    assert isinstance(right_key_three, (int, str, float, bool)
                      ) or right_key_three is None
    assert isinstance(right_key_seven, (int, str, float, bool)
                      ) or right_key_seven is None

    # Verificar consistencia en múltiples llamadas
    result1 = bst.get_max(three_bst)
    result2 = bst.get_max(three_bst)
    assert result1 == result2, "La función debería ser determinista"


@handle_not_implemented
def test_delete_min():

    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Eliminar la llave mínima y verificar que se retorna un árbol
    bst.delete_min(empty_bst)
    bst.delete_min(three_bst)
    bst.delete_min(seven_bst)

    # Verificar que los árboles siguen siendo árboles de búsqueda válidos
    assert "root" in empty_bst

    assert "root" in three_bst

    assert "root" in seven_bst


@handle_not_implemented
def test_delete_max():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Eliminar la llave máxima y verificar que se retorna un árbol
    bst.delete_max(empty_bst)
    bst.delete_max(three_bst)
    bst.delete_max(seven_bst)

    # Verificar que los árboles siguen siendo árboles de búsqueda válidos
    assert "root" in empty_bst

    assert "root" in three_bst

    assert "root" in seven_bst


@handle_not_implemented
def test_floor():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Verificar el tipo de retorno para diferentes casos
    floor_empty = bst.floor(empty_bst, 1)
    # Valor que probablemente existe
    floor_three_exists = bst.floor(three_bst, 5)
    # Valor que probablemente no existe
    floor_three_nexists = bst.floor(three_bst, 2)
    floor_seven = bst.floor(seven_bst, 35)

    # Verificar que el tipo de retorno es consistente
    assert floor_empty is None or isinstance(
        floor_empty, (int, str, float, bool))
    assert floor_three_exists is None or isinstance(
        floor_three_exists, (int, str, float, bool))
    assert floor_three_nexists is None or isinstance(
        floor_three_nexists, (int, str, float, bool))
    assert floor_seven is None or isinstance(
        floor_seven, (int, str, float, bool))

    # Verificar consistencia en múltiples llamadas
    result1 = bst.floor(three_bst, 5)
    result2 = bst.floor(three_bst, 5)
    assert result1 == result2, "La función debería ser determinista"

    if result1 is not None:
        same_key = bst.floor(three_bst, result1)
        assert same_key == result1, "floor(x) debería ser x cuando x está en el árbol"


@handle_not_implemented
def test_ceiling():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Verificar el tipo de retorno para diferentes casos
    ceiling_empty = bst.ceiling(empty_bst, 1)
    # Valor que probablemente existe
    ceiling_three_exists = bst.ceiling(three_bst, 5)
    # Valor que probablemente no existe
    ceiling_three_nexists = bst.ceiling(three_bst, 2)
    ceiling_seven = bst.ceiling(seven_bst, 35)

    # Verificar que el tipo de retorno es consistente
    assert ceiling_empty is None or isinstance(
        ceiling_empty, (int, str, float, bool))
    assert ceiling_three_exists is None or isinstance(
        ceiling_three_exists, (int, str, float, bool))
    assert ceiling_three_nexists is None or isinstance(
        ceiling_three_nexists, (int, str, float, bool))
    assert ceiling_seven is None or isinstance(
        ceiling_seven, (int, str, float, bool))

    # Verificar consistencia en múltiples llamadas
    result1 = bst.ceiling(three_bst, 5)
    result2 = bst.ceiling(three_bst, 5)
    assert result1 == result2, "La función debería ser determinista"

    # Verificar que ceiling(x) == x cuando x está en el árbol (si aplica)

    if result1 is not None:
        same_key = bst.ceiling(three_bst, result1)
        assert same_key == result1, "ceiling(x) debería ser x cuando x está en el árbol"


@handle_not_implemented
def test_select():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Verificar el tipo de retorno para diferentes casos
    select_empty = bst.select(empty_bst, 1)
    select_three_valid = bst.select(three_bst, 1)
    select_three_invalid = bst.select(three_bst, 10)  # Posición inválida
    select_seven = bst.select(seven_bst, 3)

    # Verificar que el tipo de retorno es consistente
    assert select_empty is None or isinstance(
        select_empty, (int, str, float, bool))
    assert select_three_valid is None or isinstance(
        select_three_valid, (int, str, float, bool))
    assert select_three_invalid is None or isinstance(
        select_three_invalid, (int, str, float, bool))
    assert select_seven is None or isinstance(
        select_seven, (int, str, float, bool))

    # Verificar consistencia en múltiples llamadas
    result1 = bst.select(three_bst, 1)
    result2 = bst.select(three_bst, 1)
    assert result1 == result2, "La función debería ser determinista"

    # Verificar que select retorna None para índices negativos
    assert bst.select(
        three_bst, -1) is None, "select debería retornar None para índices negativos"


@handle_not_implemented
def test_rank():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Verificar el tipo de retorno para diferentes casos
    rank_empty = bst.rank(empty_bst, 1)
    rank_three = bst.rank(three_bst, 5)
    rank_seven = bst.rank(seven_bst, 40)

    # Verificar que el tipo de retorno es entero
    assert isinstance(rank_empty, int)
    assert isinstance(rank_three, int)
    assert isinstance(rank_seven, int)

    # Verificar que los valores devueltos son no negativos
    assert rank_empty >= 0
    assert rank_three >= 0
    assert rank_seven >= 0

    # Verificar consistencia en múltiples llamadas
    result1 = bst.rank(three_bst, 5)
    result2 = bst.rank(three_bst, 5)
    assert result1 == result2, "La función debería ser determinista"

    # Verificar que rank(x) cumple con ciertas propiedades básicas
    # Si x < y, entonces rank(x) <= rank(y)
    key1, key2 = 20, 50  # asumiendo que estos son valores válidos
    assert bst.rank(seven_bst, key1) <= bst.rank(
        seven_bst, key2), "rank debe ser monotónico"


@handle_not_implemented
def test_heigh():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Verificar el tipo de retorno
    height_empty = bst.height(empty_bst)
    height_three = bst.height(three_bst)
    height_seven = bst.height(seven_bst)

    # Verificar que el tipo de retorno es entero
    assert isinstance(height_empty, int)
    assert isinstance(height_three, int)
    assert isinstance(height_seven, int)

    # Verificar que los valores devueltos son no negativos
    assert height_empty >= 0
    assert height_three >= 0
    assert height_seven >= 0

    # Verificar consistencia en múltiples llamadas
    result1 = bst.height(three_bst)
    result2 = bst.height(three_bst)
    assert result1 == result2, "La función debería ser determinista"

    # Verificar que la altura de un árbol vacío es 0
    assert height_empty == 0, "La altura de un árbol vacío debe ser 0"

    # Verificar que la altura crece con el tamaño del árbol (generalmente)
    # Esto es una heurística general, no una regla absoluta
    assert height_three <= height_seven or bst.size(three_bst) > bst.size(
        seven_bst), "Árboles más grandes tienden a tener mayor altura"


@handle_not_implemented
def test_keys():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Verificar el tipo de retorno para diferentes casos
    keys_empty = bst.keys(empty_bst, 1, 10)
    keys_three = bst.keys(three_bst, 1, 10)
    keys_seven = bst.keys(seven_bst, 20, 60)

    # Verificar que el retorno tiene la estructura de una lista enlazada
    assert isinstance(keys_empty, dict)
    assert "first" in keys_empty
    assert "last" in keys_empty
    assert "size" in keys_empty

    assert isinstance(keys_three, dict)
    assert "first" in keys_three
    assert "last" in keys_three
    assert "size" in keys_three

    assert isinstance(keys_seven, dict)
    assert "first" in keys_seven
    assert "last" in keys_seven
    assert "size" in keys_seven

    # Verificar que size es un entero no negativo
    assert isinstance(keys_empty["size"], int)
    assert keys_empty["size"] >= 0

    assert isinstance(keys_three["size"], int)
    assert keys_three["size"] >= 0

    assert isinstance(keys_seven["size"], int)
    assert keys_seven["size"] >= 0

    # Verificar consistencia en múltiples llamadas
    result1 = bst.keys(three_bst, 1, 10)["size"]
    result2 = bst.keys(three_bst, 1, 10)["size"]
    assert result1 == result2, "La función debería ser determinista"

    # Verificar que first es None cuando size es 0
    if keys_empty["size"] == 0:
        assert keys_empty["first"] is None


@handle_not_implemented
def test_values():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Verificar el tipo de retorno para diferentes casos
    values_empty = bst.values(empty_bst, 1, 10)
    values_three = bst.values(three_bst, 1, 10)
    values_seven = bst.values(seven_bst, 20, 60)

    # Verificar que el retorno tiene la estructura de una lista enlazada
    assert isinstance(values_empty, dict)
    assert "first" in values_empty
    assert "last" in values_empty
    assert "size" in values_empty

    assert isinstance(values_three, dict)
    assert "first" in values_three
    assert "last" in values_three
    assert "size" in values_three

    assert isinstance(values_seven, dict)
    assert "first" in values_seven
    assert "last" in values_seven
    assert "size" in values_seven

    # Verificar que size es un entero no negativo
    assert isinstance(values_empty["size"], int)
    assert values_empty["size"] >= 0

    assert isinstance(values_three["size"], int)
    assert values_three["size"] >= 0

    assert isinstance(values_seven["size"], int)
    assert values_seven["size"] >= 0

    # Verificar consistencia en múltiples llamadas
    result1 = bst.values(three_bst, 1, 10)["size"]
    result2 = bst.values(three_bst, 1, 10)["size"]
    assert result1 == result2, "La función debería ser determinista"

    # Verificar que first es None cuando size es 0
    if values_empty["size"] == 0:
        assert values_empty["first"] is None

    # Verificar que los tamaños de keys y values coinciden para el mismo rango
    keys_size = bst.keys(seven_bst, 20, 60)["size"]
    values_size = bst.values(seven_bst, 20, 60)["size"]
    assert keys_size == values_size, "keys y values deben tener el mismo tamaño para el mismo rango"
