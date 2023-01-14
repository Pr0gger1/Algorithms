import random
import time

def bubble_sort(iter_object: list, reverse: bool = False) -> list:
    if len(iter_object) < 2: return iter_object
    
    # do 2 loops for swapping all elements
    for i in range(len(iter_object)):
        for j in range(len(iter_object) - i - 1):
            if iter_object[j] > iter_object[j + 1]:
                iter_object[j], iter_object[j + 1] = iter_object[j + 1], iter_object[j]
    
    if reverse: iter_object = iter_object[::-1]
    return iter_object