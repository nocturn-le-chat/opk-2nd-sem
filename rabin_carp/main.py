def hash(string):
    # Хеширование отдельной функцией
    return sum([ord(string[k])*2048**k for k in range(len(string))])%2099

def rabin_carp_operator(pattern, string):
    p_hash = hash(pattern)
    p_len, s_len = len(pattern), len(string)

    # Первичная проверка
    for cursor in range(0, s_len-p_len+1):
        slice = string[cursor : cursor+p_len]
        sl_hash = hash(slice)
    
    # Вторичная побуквенная проверка
        if p_hash == sl_hash:
            p_letter_hash = [ord(k) for k in pattern]
            sl_letter_hash = [ord(k) for k in slice]
            if p_letter_hash == sl_letter_hash:
                result = slice
                break
    return result

def rabin_carp(pattern, string):
    try:
        if not all([type(k)==str for k in [pattern, string]]): raise TypeError
        elif len(pattern) > len(string): raise ValueError
        else: return rabin_carp_operator(pattern, string)
    except TypeError: print("ERROR: unsupported input type")
    except ValueError: print("ERROR: string shouldn't be shorter than searched pattern")