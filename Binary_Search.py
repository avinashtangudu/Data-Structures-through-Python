
'''

Author: Tangudu Avinash
Posted: Github
Topic: Data Structures through Python

'''

def binary_search(array, value):   
    last, first = len(array), 0
    
    while first < last:
        middle = (last - first)//2
        item = array[middle]
        
        if item == value:
            return True
        
        elif item < value:
            last = middle
        
        else:
            first = middle 
    
    return False

def binary_search_rec(array, value, first=0, last=None):
    last = last or len(array)
    if len(array[first:last]) < 1:
        return False
    
    middle = (last - first)//2
    if array[middle] == value:
        return True
    elif array[middle] < value:
        return binary_search_rec(array, value, first=first, last=middle)
    else:
        return binary_search_rec(array, value, first=middle, last=last)

    
if __name__ == '__main__':    
    array = [2, 4, 6, 8, 10, 12, 18, 28, 32]
    value = 6
    assert(binary_search(array, value) == True)   
    assert(binary_search_rec(array, value) == True)  
    value = 8
    assert(binary_search(array, value) == False)
    assert(binary_search_rec(array, value) == False)  
    array = [8]
    assert(binary_search(array, value) == True)
    assert(binary_search_rec(array, value) == True)  
    array = []
    assert(binary_search(array, value) == False)
    assert(binary_search_rec(array, value) == False)  