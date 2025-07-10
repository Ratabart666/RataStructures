
from DataStructures.Queue import queue as queue
from DataStructures.Utils.utils import handle_not_implemented

def setup_queue():
    # Inicializa una cola vacía para pruebas
    return queue.new_queue()

@handle_not_implemented
def test_new_queue():
    # Verifica que la cola se crea correctamente y está vacía
    my_queue = setup_queue()

    assert type(my_queue) == dict
    assert queue.is_empty(my_queue) is True
    assert queue.size(my_queue) == 0

@handle_not_implemented
def test_enqueue():
    # Verifica que los elementos se agregan correctamente al final de la cola
    my_queue = setup_queue()
    queue.enqueue(my_queue, 1)
    assert queue.size(my_queue) == 1
    assert queue.peek(my_queue) == 1  

    queue.enqueue(my_queue, 10)
    assert queue.size(my_queue) == 2
    assert queue.peek(my_queue) == 1

@handle_not_implemented
def test_dequeue():
    # Verifica que el `dequeue` retira y devuelve el primer elemento de la cola
    my_queue = setup_queue()
    queue.enqueue(my_queue, 10)
    queue.enqueue(my_queue, 20)

    assert queue.dequeue(my_queue) == 10
    assert queue.size(my_queue) == 1
    assert queue.peek(my_queue) == 20  

    assert queue.dequeue(my_queue) == 20
    assert queue.is_empty(my_queue) is True

@handle_not_implemented
def test_is_empty():
    # Verifica si la cola detecta correctamente si está vacía o no
    my_queue = setup_queue()
    assert queue.is_empty(my_queue) is True

    queue.enqueue(my_queue, 5)
    assert queue.is_empty(my_queue) is False

    queue.dequeue(my_queue)
    assert queue.is_empty(my_queue) is True

@handle_not_implemented
def test_peek():
    # Verifica que `peek` devuelve el primer elemento sin eliminarlo
    my_queue = setup_queue()
    queue.enqueue(my_queue, "A")
    queue.enqueue(my_queue, "B")

    assert queue.peek(my_queue) == "A"
    assert queue.size(my_queue) == 2

@handle_not_implemented
def test_size():
    # Verifica que `size` devuelve el número correcto de elementos
    my_queue = setup_queue()
    assert queue.size(my_queue) == 0

    queue.enqueue(my_queue, "X")
    queue.enqueue(my_queue, "Y")
    queue.enqueue(my_queue, "Z")

    assert queue.size(my_queue) == 3

    queue.dequeue(my_queue)
    assert queue.size(my_queue) == 2
