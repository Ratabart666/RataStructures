
from DataStructures.Stack import stack as stack
from DataStructures.Utils.utils import handle_not_implemented

def setup_stack():
    # Inicializa una pila vacía para pruebas
    return stack.new_stack()

@handle_not_implemented
def test_new_stack():
    #verifica que la pila esté vacía
    my_stack = setup_stack()

    assert type(my_stack) == dict
    assert stack.is_empty(my_stack) is True
    assert stack.size(my_stack) == 0
    
@handle_not_implemented
def test_push():
    # Verifica que los elementos se agregan correctamente en la pila
    my_stack = setup_stack()
    stack.push(my_stack, 10)
    assert stack.size(my_stack) == 1
    assert stack.top(my_stack) == 10

    stack.push(my_stack, 20)
    assert stack.size(my_stack) == 2
    assert stack.top(my_stack) == 20
    
@handle_not_implemented
def test_pop():
     # Verifica que `pop` retira y devuelve el último elemento de la pila
    my_stack = setup_stack()
    stack.push(my_stack, 10)
    stack.push(my_stack, 20)

    assert stack.pop(my_stack) == 20
    assert stack.size(my_stack) == 1
    assert stack.top(my_stack) == 10

    assert stack.pop(my_stack) == 10
    assert stack.is_empty(my_stack) is True
    
@handle_not_implemented
def test_is_empty():
    # Verifica si la pila detecta correctamente si está vacía o no
    my_stack = setup_stack()
    assert stack.is_empty(my_stack) is True

    stack.push(my_stack, "test")
    assert stack.is_empty(my_stack) is False

    stack.pop(my_stack)
    assert stack.is_empty(my_stack) is True

@handle_not_implemented
def test_top():
    # Verifica que `top` devuelve el último elemento sin eliminarlo
    my_stack = setup_stack()
    stack.push(my_stack, "A")
    stack.push(my_stack, "B")

    assert stack.top(my_stack) == "B"
    assert stack.size(my_stack) == 2  
    
@handle_not_implemented
def test_size():
     # Verifica que `size` devuelve el número correcto de elementos
    my_stack = setup_stack()
    assert stack.size(my_stack) == 0

    stack.push(my_stack, 5)
    stack.push(my_stack, 15)
    stack.push(my_stack, 25)

    assert stack.size(my_stack) == 3

    stack.pop(my_stack)
    assert stack.size(my_stack) == 2
