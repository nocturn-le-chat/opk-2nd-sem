# "Рабочая лошадка" = обработка данных
def workhorse(iterable):
    for median in iterable:
        median_chain = iterable.index(median)
        it_medianless = iterable[:median_chain] + iterable[median_chain+1:]
        for ever in it_medianless:
            current = iterable.pop(iterable.index(ever))
            if ever < median:    
                iterable.insert(iterable.index(median), current)
            else:
                iterable.insert(iterable.index(median)+1, current)
    return iterable

# "Фильтрационная часть" = проверка входних данных
def qsort(iterable):
    if type(iterable) != list: return "ERROR: unsupported input type"
    elif not all([type(k) in [int, str] for k in iterable]): return "ERROR: incorrect input containments"
    else: return workhorse(iterable)