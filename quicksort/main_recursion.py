# "Рабочая лошадка" = обработка данных
def workhorse(iterable):
    if len(iterable) <=1: return iterable
    anchor = iterable[len(iterable)//2]
    left = [k for k in iterable if k < anchor]
    right = [k for k in iterable if k > anchor]
    
    return workhorse(left) + [k for k in iterable if k == anchor] + workhorse(right)

# "Фильтрационная часть" = проверка входних данных
def qsort(iterable):
    if type(iterable) != list: return "ERROR: unsupported input type"
    elif not all([type(k) in [int, str] for k in iterable]): return "ERROR: incorrect input containments"
    else: return workhorse(iterable)