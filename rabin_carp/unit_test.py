from re import findall
from main import rabin_carp
from random import randint


print("Executing tests...")
assert rabin_carp(1, "one") == None, "ERROR: non-string argument chewing"
assert rabin_carp(False, 0) == None, "ERROR: non-string argument chewing"
assert rabin_carp(0, ["zero", "hero"]) == None, "ERROR: non-string argument chewing"
assert rabin_carp("1234567890", "123") == None, "ERROR: chewing pattern bigger than origin string"
print("Static tests done...\n")

sample_text = "Психосфера была на острие общественного и делового интереса, как космос и космонавтика в эпоху первых полетов середины-конца XX-го века. " \
              "Однако, не все шло гладко. Скоро стало понятно, что открытые пространства - это не райские кущи. " \
              "Люди столкнулись с явлением, получившим название Реакция Психосферы."

try:
    pattern_len = randint(1, 20)
    cursor = randint(0, len(sample_text)-pattern_len)
    pattern = sample_text[cursor:cursor+pattern_len+1]
    if findall(pattern, sample_text) != rabin_carp(pattern, sample_text): raise ValueError
    else: print("Dynamic tests done...\n")
except ValueError: print("ERROR: bad searching algorithm")

print("\t\t...Done!")