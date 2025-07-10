
def new_list():
    newlist= {
        "elements": [],
        "size": 0, 
    }
    return newlist

def add_first(newlist, element): 
    newlist["elements"].insert(0,element)
    newlist["size"]+=1
    return newlist

def add_last(newlist,element):
    
    newlist["elements"].insert(len(newlist["elements"]),element)
    newlist["size"]+=1
    return newlist

def is_empty(my_list):
    
    if my_list["size"]== 0:
        x=True
    else:
        x=False
    return x

def size(newlist):
    return newlist["size"]

def first_element(newlist):
    if newlist["size"]==0:
        raise Exception('IndexError: list index out of range')
    else:
        x=newlist["elements"][0]
        return x
    
def last_element(newlist):
    if new_list["size"]==0:
        raise Exception('IndexError: list index out of range')
    else:
        x=newlist["elements"][-1]
        return x

def get_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["elements"][pos]

def remove_first(my_list):
    if my_list["size"]==0:
        raise Exception('IndexError: list index out of range')
    else:
        my_list["size"]-=1
        x=my_list["elements"][0]
        del my_list["elements"][0]
        return x
    
def remove_last(my_list):
    if my_list["size"]==0:
        raise Exception('IndexError: list index out of range')
    else:
        my_list["size"]-=1
        x=my_list["elements"][-1]
        del my_list["elements"][0]
        return x

def insert_element(my_list, element, pos):
    my_list["elements"].insert(pos,element)
    my_list["size"]+=1
    return my_list

def is_present(my_list, element, cmp_function):
    
    size = my_list["size"]
    if size > 0:
        keyexist =False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info)==0:
                keyexist=True
                break
        if keyexist:
            return keypos
    return -1

def delete_element(my_list,pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        my_list["size"]-=1
        del my_list["elements"][pos]
        return my_list
    
def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        my_list["elements"][pos]=new_info
        return my_list

def exchange(my_list,pos_1, pos_2):
    if pos_2 < 0 or pos_2 >= size(my_list) or pos_1 < 0 or pos_1 >= size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        x= my_list["elements"][pos_2]
        my_list["elements"][pos_2]=my_list["elements"][pos_1]
        my_list["elements"][pos_1]=x
        return my_list

def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i >= size(my_list) or pos_i+num_elements>size(my_list) :
        raise Exception('IndexError: list index out of range')
    else:
        sublist = new_list()
        counter = 0
        while counter < num_elements:
            add_last(sublist, my_list['elements'][pos_i + counter])
            counter += 1
        
        return sublist
########################


def default_sort_criteria(element_1, element_2):
   is_sorted = False
   if element_1 < element_2:
      is_sorted = True
   return is_sorted

def selection_sort(my_list, sort_crit):
    
    es=my_list["elements"]

    for i in range(size(my_list)):
        pos=0
        menor = es[i]
        for j in range(i, size(my_list)):
            
            if sort_crit(es[j],menor)==True:
            #if es[j]<= menor:
                menor =es[j]
                pos= j
        
        exchange(my_list,pos,i)
        
    return my_list

def insertion_sort(my_list,sort_crit):
    
    es=my_list["elements"]
    vac=[]
    if my_list["size"]==0:
        None
    else:
        vac.append(es[0])
        for i in range(1,size(my_list)):    
            pos=0
            for j in range(len(vac)):
                if sort_crit(es[i],vac[j])==True:
                #if es[i]<vac[j]:
                    break
                pos+=1    
            vac.insert(pos,es[i])
        my_list["elements"]=vac
    return my_list


def shell_sort(my_list, sort_crit):
    n = my_list["size"]
    arr = my_list["elements"]
    
    gap = n // 2 
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and not sort_crit(arr[j - gap], temp):
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2 
    return my_list



def merge_sort(list, sort_criteria):
    
    num_elements = size(list)
    if num_elements > 1:
        mid = num_elements // 2
        left_list = sub_list(list, 0, mid)
        right_list = sub_list(list, mid, num_elements-mid)
        
        merge_sort(left_list, sort_criteria)
        merge_sort(right_list, sort_criteria)
        
        i = j = k = 0
        
        left_elements = size(left_list)
        right_elements = size(right_list)
        
        while i < left_elements and j < right_elements:
            elem_i = get_element(left_list, i)
            elem_j = get_element(right_list, j)
            
            if sort_criteria(elem_j, elem_i):
                change_info(list, k, elem_j)
                j += 1
            else:
                change_info(list, k, elem_i)
                i += 1
            k += 1
        
        while i < left_elements:
            change_info(list, k, get_element(left_list, i))
            i += 1
            k += 1
        
        while j < right_elements:
            change_info(list, k, get_element(right_list, j))
            j += 1
            k += 1
    return list
        
def quick_sort(list, sort_criteria=default_sort_criteria):
    quick_sort_recursive(list, 0, size(list) - 1, sort_criteria)
    return list

def quick_sort_recursive(list, lo, hi, sort_criteria):
    if lo < hi:
        pivot = partition(list, lo, hi, sort_criteria)
        quick_sort_recursive(list, lo, pivot - 1, sort_criteria)
        quick_sort_recursive(list, pivot + 1, hi, sort_criteria)

def partition(list, lo, hi, sort_criteria):
    follower = leader = lo
    while leader < hi:
        if sort_criteria(get_element(list, leader), get_element(list, hi)):
            exchange(list, follower, leader)
            follower += 1
        leader += 1
    exchange(list, follower, hi)
    return follower
