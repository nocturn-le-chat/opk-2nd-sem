def workhorse(iterable):
    #Рабочая часть
    for old_pos in range(1, len(iterable)):
        if iterable[old_pos]<iterable[old_pos-1]:
            for new_pos in range(0, old_pos):
                if iterable[old_pos] < iterable[new_pos]:
                    iterable[old_pos], iterable[new_pos] = iterable[new_pos], iterable[old_pos]
                    continue
    return iterable

def insertion_sort(iterable):
    #Фильтрационная часть
    if type(iterable)!= list: return "ERROR: unsupported input type"
    elif iterable == []: return []
    elif not all([type(k) in [int, str] for k in iterable]): return "ERROR: incorrect input containments"
    else: return workhorse(iterable)