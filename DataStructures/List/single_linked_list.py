from DataStructures.List import list_node as node

def new_list(): 
    newlist={
        "first":None,
        "last":None,
        "size":0,
    }
    return newlist

def add_first(my_list, element):
    if my_list["size"]==0:
        my_list["size"]+=1
        my_list["first"]={"info":element,"next":None}
        my_list["last"]={"info":element,"next":None}
    elif my_list["size"]>=1:
        my_list["size"]+=1
        my_list["first"]={"info":element, "next":my_list["first"]}
    return my_list

def add_last (my_list,element):
    x=my_list["first"]
    if my_list["size"]==0:
        my_list["size"]+=1
        my_list["first"]={"info":element,"next":None}
        my_list["last"]={"info":element,"next":None}
    else:
        while x["next"] is not None:
            x=x["next"]
        x["next"]={"info":element,"next":None}
        my_list["last"]["info"]=element
        my_list["size"]+=1
    return my_list

def is_empty(my_list):
    if my_list["size"]==0:
        x=True
    else:
        x=False
    return x

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["first"]["info"]
   
def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["last"]["info"] 

def get_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        searchpos=0
        node = my_list["first"]
        while searchpos<pos:
            node=node["next"]
            searchpos +=1
        return node["info"]

def remove_first(my_list):
    if my_list["size"]==0:
        raise Exception('IndexError: list index out of range')
    elif my_list["size"]==1:
        x=my_list["first"]["info"]
        my_list["first"]=[None]
        my_list["last"]=[None]
        my_list["size"]-=1
    else:       
        my_list["size"]-=1
        x=my_list["first"]["info"]
        my_list["first"]=my_list["first"]["next"]
    return x

def remove_last(my_list):
    if my_list["size"]==0:
        raise Exception ('IndexError: list index out of range')
    elif my_list["size"]==1:
        lu=my_list["last"]["info"] 
        my_list={'first': None,  'last': None, 'size': 0}
    elif my_list["size"]>1:
        lu=my_list["last"]["info"] 
        y=my_list["first"]
        for i in range(my_list["size"]-2):
            y=y["next"]
        y["next"]=None
        x=my_list["first"]
        for i in range(my_list["size"]-2):
            x=x["next"]
        my_list["last"]=x
        my_list["size"]-=1
    return lu

def insert_element(my_list, element, pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        
        m=my_list["first"]
        y={'first': None,  'last': None, 'size': 0}     
        for i in range(my_list["size"]):
            if i==pos:
                y=add_last(y,element)
            p=m["info"]  
            m=m["next"]
            y=add_last(y,p)
    return y

def is_present(my_list,element,cmp_function):
    is_in_array=False
    temp=my_list["first"]
    count=0
    while not is_in_array and temp is not None:
        if cmp_function(element,temp["info"])==0:
            is_in_array=True
        else:
            temp=temp["next"]
            count +=1
    
    if not is_in_array:
        count= -1
    return count

def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        m=my_list["first"]
        y={'first': None,  'last': None, 'size': 0}     
        for i in range(my_list["size"]):
            if i==pos:
                p=m["info"]  
                m=m["next"]
                continue
            p=m["info"]  
            m=m["next"]
            y=add_last(y,p)
        
        
        return y

def change_info(my_list,pos,new_info):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        p=my_list["first"]
        for i in range(pos):
            p=p["next"]
        p["info"]=new_info
        o=my_list["first"]
        for i in range(my_list["size"]-1):
            o=o["next"]
        my_list["last"]=o
    return my_list
      
def exchange(my_list, pos_1, pos_2):
    if pos_2 < 0 or pos_2 >= size(my_list) or pos_1 < 0 or pos_1 >= size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        p=my_list["first"]
        for i in range(my_list["size"]):
            if i==pos_1:
                uno=p["info"]
            if i== pos_2:
                dos=p["info"]
            p=p["next"]
            
        my_list=change_info(my_list,pos_1,dos)
        my_list=change_info(my_list,pos_2,uno)
        
    return my_list  

def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= size(my_list) or pos+num_elements>size(my_list) :
        raise Exception('IndexError: list index out of range')
    else:
        z={"first":None,"last":None, "size": 0}
        p=my_list["first"]
        j=0
        for i in range(my_list["size"]):
            if i>=pos:
                j+=1
                z=add_last(z,p["info"])
                if j== num_elements:
                    break
            p=p["next"]
        return z


#######################

def default_sort_criteria(element_1, element_2):

   is_sorted = False
   if element_1 < element_2:
      is_sorted = True
   return is_sorted

def selection_sort(my_list, sort_crit):


    for i in range(size(my_list)):
        pos=0
        menor=get_element(my_list,i)
        for j in range(i, size(my_list)):
            
            if sort_crit(get_element(my_list,j),menor)==True:
            #if es[j]<= menor:
                menor =get_element(my_list,j)
                pos= j

        exchange(my_list,pos,i)
        
    return my_list

def insertion_sort(my_list, sort_crit):
    es=my_list["first"]
    #vac=[]
    vac=new_list()
    if my_list["size"]==0:
        None
    else:
        #vac.append(get_element(my_list,0))
        add_last(vac,get_element(my_list,0))
        for i in range(1,size(my_list)):    
            pos=0
            for j in range(vac["size"]):
                if sort_crit(get_element(my_list,i),get_element(vac,j))==True:
                #if es[i]<vac[j]:
                    break
                pos+=1 
            insert_element(vac,get_element(my_list,i),pos)   
        my_list=vac
    return my_list


def shell_sort(my_list, sort_crit):
    n = my_list["size"] 
    gap = n // 2 
    while gap > 0:
        for i in range(gap, n):
            temp= get_element(my_list,i)
            j = i
            while j >= gap and not sort_crit(get_element(my_list,j-gap), temp):
                change_info(my_list,j,get_element(my_list,j-gap))
                j -= gap
            change_info(my_list,j,temp)
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
    
