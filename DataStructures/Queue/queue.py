from DataStructures.List import array_list as lt
#from DataStructures.List import single_linked_list as lt
def new_queue():
    x=lt.new_list()
    return x

def enqueue(my_queue, element):
    x=lt.add_last(my_queue,element)
    return x
    
def dequeue(my_queue):
    if my_queue["size"]==0:
        raise Exception('EmptyStructureError: queue is empty')
    else:
        #lt.remove_first(my_queue)
        return lt.remove_first(my_queue)

def peek(my_queue):
    if my_queue["size"]==0:
        raise Exception('EmptyStructureError: queue is empty')
    else:  
        return lt.first_element(my_queue)

def is_empty(my_queue):
    return lt.is_empty(my_queue)

def size(my_queue):
    return lt.size(my_queue)

#######################

