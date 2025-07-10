#from DataStructures.List import array_list as sl
from DataStructures.List import single_linked_list as sl

def new_stack():
    return sl.new_list()

def is_empty(my_stack):
    x=sl.is_empty(my_stack)
    return x

def size(my_stack):
    x=sl.size(my_stack)
    return x

def top(my_stack):
    if my_stack["size"]==0:
        raise Exception('EmptyStructureError: stack is empty')
    else:
        return sl.first_element(my_stack)
    
def push(my_stack,element):
    return sl.add_first(my_stack,element)

def pop(my_stack):
    if my_stack["size"]==0:
        raise Exception('EmptyStructureError: stack is empty')
    else:
        x= sl.remove_first(my_stack)
        return x