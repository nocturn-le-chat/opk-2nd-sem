from rational import Rational as subj
from random import randint

print("Executing tests...")
sample_1= subj.create(randint(-1000, 1000), randint(-1000, 1000))
sample_2= subj.create(randint(-1000, 1000), randint(-1000, 1000))

# Тесты конструктора
print("\nNow doing constructors...")
assert subj.to_list(subj.create(0, randint(-1000, 1000))) == [0, 1], "ERROR: creating witn 0 numerator"
assert subj.create(1, 0) == None, "ERROR: creating witn 0 denominator"
print("\t\t...done")

# Тесты деконструктора
print("\nNow doing deconstructors...")
assert subj.to_float(sample_1) == sample_1.num/sample_1.den,   "ERROR: bad 2 float convert"
assert subj.to_int(sample_1) == sample_1.num//sample_1.den,    "ERROR: bad 2 int convert"
assert subj.to_list(sample_1) == [sample_1.num, sample_1.den], "ERROR: bad 2 list convert"
print("\t\t...done")

# Тесты арифметических
print("\nNow doing ariphmetical...")
assert subj.to_list(subj.add(subj.create(1, 2), subj.create(2, 3))) ==   [7, 6],  "ERROR: bad >0/>0 additor"
assert subj.to_list(subj.add(subj.create(-1, -2), subj.create(2, 3))) == [7, 6],  "ERROR: bad <0/<0 additor"
assert subj.to_list(subj.add(subj.create(-1, 2), subj.create(2, 3))) ==  [1, 6],  "ERROR: bad <0/>0 additor"
assert subj.to_list(subj.add(subj.create(1, -2), subj.create(2, 3))) ==  [1, 6],  "ERROR: bad >0/<0 additor"

assert subj.to_list(subj.sub(subj.create(1, 2), subj.create(2, 3))) == [-1, 6],   "ERROR: bad >0/>0 substractor"
assert subj.to_list(subj.sub(subj.create(-1, -2), subj.create(2, 3))) == [-1, 6], "ERROR: bad >0/>0 substractor"
assert subj.to_list(subj.sub(subj.create(-1, 2), subj.create(2, 3))) == [-7, 6],  "ERROR: bad <0/>0 substractor"
assert subj.to_list(subj.sub(subj.create(1, -2), subj.create(2, 3))) ==  [-7, 6], "ERROR: bad >0/<0 substractor"

assert subj.to_list(subj.mul(subj.create(1, 2), subj.create(2, 3))) == [1, 3],    "ERROR: bad >0/>0 multiplicator"
assert subj.to_list(subj.mul(subj.create(-1, -2), subj.create(2, 3))) == [1, 3],  "ERROR: bad <0/<0 multiplicator"
assert subj.to_list(subj.mul(subj.create(-1, 2), subj.create(2, 3))) == [-1, 3],  "ERROR: bad <0/>0 multiplicator"
assert subj.to_list(subj.mul(subj.create(1, -2), subj.create(2, 3))) == [-1, 3],  "ERROR: bad >0/<0 multiplicator"

assert subj.to_list(subj.div(subj.create(1, 2), subj.create(2, 3))) == [3, 4],    "ERROR: bad >0/>0 divider"
assert subj.to_list(subj.div(subj.create(-1, -2), subj.create(2, 3))) == [3, 4],  "ERROR: bad <0/<0 divider"
assert subj.to_list(subj.div(subj.create(-1, 2), subj.create(2, 3))) == [-3, 4],  "ERROR: bad <0/>0 divider"
assert subj.to_list(subj.div(subj.create(1, -2), subj.create(2, 3))) == [-3, 4],  "ERROR: bad >0/<0 divider"

assert subj.compare(subj.create(2, 3), subj.create(1, 2)) == 1,                   "ERROR: bad >0/>0 comparator"
assert subj.compare(subj.create(-2, -3), subj.create(1, 2)) == 1,                 "ERROR: bad <0/<0 comparator"
assert subj.compare(subj.create(-2, 3), subj.create(1, 2)) == -1,                 "ERROR: bad <0/>0 comparator"
assert subj.compare(subj.create(2, -3), subj.create(1, 2)) == -1,                 "ERROR: bad >0/<0 comparator"
print("\t\t...done")

# Тесты алгебраических
print("\nNow doing algebraical...")
assert subj.to_list(subj.power(subj.create(1, 2), 3)) == [1, 8],                  "ERROR: bad >0/>0 >0 powerator"
assert subj.to_list(subj.power(subj.create(-1, -2), 3)) == [1, 8],                "ERROR: bad <0/<0 >0 powerator"
assert subj.to_list(subj.power(subj.create(-1, 2), 3)) == [-1, 8],                "ERROR: bad <0/>0 >0 powerator"
assert subj.to_list(subj.power(subj.create(1, -2), 3)) == [-1, 8],                "ERROR: bad >0/<0 >0 powerator"

assert subj.to_list(subj.power(subj.create(1, 2), 0)) == [1, 1],                  "ERROR: bad >0/>0 =0 powerator"
assert subj.to_list(subj.power(subj.create(-1, -2), 0)) == [1, 1],                "ERROR: bad <0/<0 =0 powerator"
assert subj.to_list(subj.power(subj.create(-1, 2), 0)) == [1, 1],                 "ERROR: bad <0/>0 =0 powerator"
assert subj.to_list(subj.power(subj.create(1, -2), 0)) == [1, 1],                 "ERROR: bad >0/<0 =0 powerator"

assert subj.to_list(subj.power(subj.create(1, 2), -3)) == [8, 1],                 "ERROR: bad >0/>0 <0 powerator"
assert subj.to_list(subj.power(subj.create(-1, -2), -3)) == [8, 1],               "ERROR: bad <0/<0 <0 powerator"
assert subj.to_list(subj.power(subj.create(-1, 2), -3)) == [-8, 1],               "ERROR: bad <0/>0 <0 powerator"
assert subj.to_list(subj.power(subj.create(1, -2), -3)) == [-8, 1],               "ERROR: bad >0/<0 <0 powerator"

assert subj.power(subj.create(0, -2), -3) == None,                                "ERROR: bad >0/<0 <0 powerator"
print("\t...done")

print("...Done!")