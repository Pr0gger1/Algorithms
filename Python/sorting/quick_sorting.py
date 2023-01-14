def quick_sort(iter_object: list, reverse: bool = False):   
    if len(iter_object) < 2: return iter_object
    # we need to choose a reference element
    # for example, the middle element
    ref_element = iter_object[round(len(iter_object) / 2)]

    # filtering elements that are smaller and larger than ref_element into other lists
    left = [el for el in iter_object[1:] if el <= ref_element]
    right = [el for el in iter_object[1:] if el > ref_element]

    # sort in descending order
    if reverse: left, right = right, left
    return quick_sort(left, reverse) + [ref_element] + quick_sort(right, reverse)