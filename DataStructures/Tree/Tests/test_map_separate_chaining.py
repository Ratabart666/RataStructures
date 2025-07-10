from DataStructures.Utils.utils import handle_not_implemented
from DataStructures.Map import map_separate_chaining as mp
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.List import array_list as lt


def setup_tests(scale, shift):
    new_map = mp.new_map(5, 0.5, 7)
    if scale is not None and shift is not None:
        new_map["scale"] = scale
        new_map["shift"] = shift
    return new_map


def test_new_map():
    map = mp.new_map(5, 0.5, 7)
    assert isinstance(map, dict)
    assert "capacity" in map
    assert "size" in map
    assert map["size"] == 0



def test_put():
    map = setup_tests(None, None)
    mp.put(map, 1, 2)
    assert map["size"] == 1
    mp.put(map, 1, 3)
    assert map["size"] == 1



def test_contains():
    map = setup_tests(None, None)
    # Caso: mapa vacío
    assert not mp.contains(map, 1)
    # Caso: elemento existente
    mp.put(map, 1, 2)
    assert mp.contains(map, 1)
    # Caso: elemento no existente
    assert not mp.contains(map, 2)



def test_get():
    map = setup_tests(None, None)
    mp.put(map, 1, 2)
    # Test para el caso en que la llave existe
    assert mp.get(map, 1) == 2

    # Test para el caso en que la llave no existe
    assert mp.get(map, 2) is None

    # Test para el caso en que la tabla está vacía
    new_map = mp.new_map(5, 0.5, 7)
    assert mp.get(new_map, 1) is None



def test_remove():
    map = setup_tests(1, 0)
    # Caso: mapa vacío
    mp.remove(map, 1)
    assert map["size"] == 0
    # Caso: eliminar elemento existente
    mp.put(map, 1, 2)
    mp.remove(map, 1)
    assert map["size"] == 0
    assert not mp.contains(map, 1)
    # Caso: eliminar elemento no existente
    mp.put(map, 1, 2)
    mp.remove(map, 2)
    assert map["size"] == 1



def test_size():
    map = setup_tests(None, None)
    mp.put(map, 1, 2)
    mp.put(map, 2, 3)
    mp.put(map, 3, 4)

    assert mp.size(map) == 3

    new_map = mp.new_map(5, 0.5, 7)
    assert mp.size(new_map) == 0



def test_is_empty():
    map = setup_tests(None, None)
    # Caso: mapa vacío
    assert mp.is_empty(map)
    # Caso: mapa no vacío
    mp.put(map, 1, 2)
    assert not mp.is_empty(map)


def test_key_set():
    map = setup_tests(None, None)
    # Caso: mapa vacío
    keys = mp.key_set(map)
    assert lt.size(keys) == 0
    # Caso: mapa con elementos
    mp.put(map, "a", 1)
    mp.put(map, "b", 2)
    keys = mp.key_set(map)
    assert lt.size(keys) == 2
    # Verificar sin depender del orden
    elements = keys["elements"]
    assert "a" in elements
    assert "b" in elements



def test_value_set():
    map = setup_tests(None, None)
    # Caso: mapa vacío
    values = mp.value_set(map)
    assert lt.size(values) == 0
    # Caso: mapa con elementos
    mp.put(map, "x", 100)
    mp.put(map, "y", 200)
    values = mp.value_set(map)
    assert lt.size(values) == 2
    # Verificar sin depender del orden
    elements = values["elements"]
    assert 100 in elements
    assert 200 in elements



def test_rehash():
    map = mp.new_map(5, 0.5, 7)
    initial_capacity = map["capacity"]
    print(initial_capacity)
    for i in range(6):
        mp.put(map, i, i*10)
    assert map["capacity"] > initial_capacity
    for i in range(6):
        assert mp.contains(map, i)
        assert mp.get(map, i) == i*10
