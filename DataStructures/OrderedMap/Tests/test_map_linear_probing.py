from DataStructures.Map import map_linear_probing as mp
from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.Utils.utils import handle_not_implemented


def setup_tests(scale, shift):
    new_map = mp.new_map(5, 0.5, 7)
    if scale is not None and shift is not None:
        new_map["scale"] = scale
        new_map["shift"] = shift
    return new_map


def test_new_map():
    map = mp.new_map(5, 0.5, 7)
    assert map["capacity"] == 11
    assert map["size"] == 0


def test_new_map():
    map = mp.new_map(5, 0.5, 7)
    assert map["prime"] == 7
    assert map["capacity"] == 11
    assert map["scale"] >= 1 and map["scale"] < 7
    assert map["shift"] >= 0 and map["shift"] < 7
    assert map["table"] is not None
    assert map["current_factor"] == 0
    assert map["limit_factor"] == 0.5
    assert map["size"] == 0

    map = mp.new_map(10, 0.5)
    assert map["prime"] == 109345121


def test_put():
    map = mp.new_map(5, 0.5, 7)
    mp.put(map, 1, "A")
    assert map["size"] == 1
    assert mp.get(map, 1) == "A"


def test_contains():
    map = mp.new_map(5, 0.5, 7)
    mp.put(map, 1, "A")
    assert mp.contains(map, 1)
    assert not mp.contains(map, 2)


def test_get():
    map = mp.new_map(5, 0.5, 7)
    mp.put(map, 1, "A")
    assert mp.get(map, 1) == "A"
    assert mp.get(map, 2) is None


def test_remove():
    map = mp.new_map(5, 0.5, 7)
    mp.put(map, 1, "A")
    mp.remove(map, 1)
    assert mp.get(map, 1) is None
    assert map["size"] == 0


def test_size():
    map = mp.new_map(5, 0.5, 7)
    assert mp.size(map) == 0
    mp.put(map, 1, "A")
    assert mp.size(map) == 1


def test_is_empty():
    map = mp.new_map(5, 0.5, 7)
    assert mp.is_empty(map)
    mp.put(map, 1, "A")
    assert not mp.is_empty(map)


def test_key_set():
    map = mp.new_map(5, 0.5, 7)
    mp.put(map, 1, "A")
    mp.put(map, 2, "B")
    mp.put(map, 3, "C")

    key_set = mp.key_set(map)
    assert lt.size(key_set) == 3
    assert {1, 2, 3} == set(key_set["elements"])

    mp.remove(map, 1)
    key_set = mp.key_set(map)
    assert lt.size(key_set) == 2
    assert 1 not in key_set["elements"]

    assert lt.size(mp.key_set(mp.new_map(5, 0.5, 7))) == 0


def test_value_set():
    map = mp.new_map(5, 0.5, 7)
    mp.put(map, 1, "X")
    mp.put(map, 2, "Y")
    mp.put(map, 3, "Z")

    value_set = mp.value_set(map)
    assert lt.size(value_set) == 3
    assert {"X", "Y", "Z"} == set(value_set["elements"])

    mp.remove(map, 1)
    value_set = mp.value_set(map)
    assert lt.size(value_set) == 2
    assert "X" not in value_set["elements"]

    assert lt.size(mp.value_set(mp.new_map(5, 0.5, 7))) == 0


def test_find_slot():
    map = mp.new_map(5, 0.5, 7)
    mp.put(map, 1, "A")
    mp.put(map, 2, "B")
    mp.put(map, 3, "C")

    # Caso 1: La clave existe en la tabla
    occupied, pos = mp.find_slot(map, 1, mf.hash_value(map, 1))
    assert occupied is True
    assert pos >= 0

    occupied, pos = mp.find_slot(map, 2, mf.hash_value(map, 2))
    assert occupied is True
    assert pos >= 0

    # Caso 2: La clave no existe y se indica una posición disponible
    occupied, pos = mp.find_slot(map, 8, mf.hash_value(map, 8))
    assert occupied is False
    assert pos >= 0

    # Caso 3: Se elimina una clave y se verifica la posición libre
    mp.remove(map, 2)
    occupied, pos = mp.find_slot(map, 2, mf.hash_value(map, 2))
    assert occupied is False
    assert pos >= 0


def test_is_available():
    map = mp.new_map(5, 0.5, 7)
    mp.put(map, 1, "A")

    assert not mp.is_available(map["table"], mf.hash_value(map, 1))
    assert mp.is_available(map["table"], mf.hash_value(map, 3))

    mp.remove(map, 1)
    assert mp.is_available(map["table"], mf.hash_value(map, 1))


def test_rehash():
    map = mp.new_map(5, 0.5, 7)
    for i in range(5):
        mp.put(map, i, str(i))

    map = mp.rehash(map)

    assert mp.size(map) == 5
    assert map["capacity"] > 5

    for i in range(5):
        assert mp.contains(map, i)
