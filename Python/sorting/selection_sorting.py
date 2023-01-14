def selectionSort(iter_object: list, reverse: bool = False):
    if len(iter_object) < 2: return iter_object

    sorted_object: list = []
    choose_element = (lambda x: max(x)) if reverse else (lambda x: min(x))
    
    for _ in range(len(iter_object)):
        # we should to find the smallest element and its index
        chosen_index: int = iter_object.index(choose_element(iter_object))

        # then we add this element to the beginning of the list
        chosen_item = iter_object.pop(chosen_index)
        sorted_object.append(chosen_item)

    return sorted_object