print("\nNow doing main_recursion.py...")

from main_recursion import qsort
from random import randint

print("Executing tests...")
assert qsort("string") == "ERROR: unsupported input type", "Input type error"
assert qsort(1) == "ERROR: unsupported input type", "Input type error"
assert qsort({"key": "value"}) == "ERROR: unsupported input type", "Massive type error"
assert qsort([[]]) == "ERROR: incorrect input containments", "List containments error"
assert qsort([]) == [], "Sorting empty list error"
assert qsort([1, 2, 3]) == [1, 2, 3], "Non-sorting error"
assert qsort([1, 2, 2]) == [1, 2, 2], "Repeating elements sorting error"
assert qsort([0, 2, 3]) == [0, 2, 3], "Sorting zero error"
assert qsort([1, -2, 3]) == [-2, 1, 3], "Sorting negatives error"
print("Static tests done...")
try:
    probe = []
    for k in range(1, len([raw:=[randint(-1000, 1000) for k in range(10, 21)]])):
        probe.append(raw[k-1]>raw[k])
    if any(probe): raise ValueError
except ValueError:
    print("Basic sorting error")
print("Dynamic tests done...")
print("\t\t...done!")


print("\nNow doing main_cycle.py...")
from main_cycle import qsort
from random import randint

print("Executing tests...")
assert qsort("string") == "ERROR: unsupported input type", "Input type error"
assert qsort(1) == "ERROR: unsupported input type", "Input type error"
assert qsort({"key": "value"}) == "ERROR: unsupported input type", "Massive type error"
assert qsort([[]]) == "ERROR: incorrect input containments", "List containments error"
assert qsort([]) == [], "Sorting empty list error"
assert qsort([1, 2, 3]) == [1, 2, 3], "Non-sorting error"
assert qsort([1, 2, 2]) == [1, 2, 2], "Repeating elements sorting error"
assert qsort([0, 2, 3]) == [0, 2, 3], "Sorting zero error"
assert qsort([1, -2, 3]) == [-2, 1, 3], "Sorting negatives error"
print("Static tests done...")
try:
    probe = []
    for k in range(1, len([raw:=[randint(-1000, 1000) for k in range(10, 21)]])):
        probe.append(raw[k-1]>raw[k])
    if any(probe): raise ValueError
except ValueError:
    print("Basic sorting error")
print("Dynamic tests done...")
print("\t\t...done!")