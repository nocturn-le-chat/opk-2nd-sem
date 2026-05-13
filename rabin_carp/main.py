def rabin_carp_operator(pattern, string):
    p_hash = sum([ord(pattern[k])*2048**k for k in range(len(pattern))])%2099
    p_len, s_len = len(pattern), len(string)

    matchbox = list()
    for cursor in range(0, s_len-p_len+1):
        slice = string[cursor : cursor+p_len]
        sl_hash = sum([ord(slice[k])*2048**k for k in range(len(slice))])%2099
        if p_hash == sl_hash:
            matchbox.append(slice)
    p_letter_hash = [ord(k) for k in pattern]
    for n in matchbox:
        n_letter_hash = [ord(k) for k in n]
        if p_letter_hash != n_letter_hash:
            matchbox.remove(n)
    return matchbox

print(rabin_carp_operator("leet", "leetspeakleet"))