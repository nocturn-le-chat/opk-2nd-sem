from main import insertion_sort
from random import randint

print("Executing tests...")
assert insertion_sort("string") == "ERROR: unsupported input type", "Input type error"
assert insertion_sort(1) == "ERROR: unsupported input type", "Input type error"
assert insertion_sort({"key": "value"}) == "ERROR: unsupported input type", "Massive type error"
assert insertion_sort([[]]) == "ERROR: incorrect input containments", "List containments error"
assert insertion_sort([]) == [], "Sorting empty list error"
assert insertion_sort([1, 2, 3]) == [1, 2, 3], "Non-sorting error"
assert insertion_sort([1, 2, 2]) == [1, 2, 2], "Repeating elements sorting error"
assert insertion_sort([0, 2, 3]) == [0, 2, 3], "Sorting zero error"
assert insertion_sort([1, -2, 3]) == [-2, 1, 3], "Sorting negatives error"
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
