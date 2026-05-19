from main import Linked_list as subj
from random import randint

sample_list, sample_list2 = [randint(-1000, 1000) for k in range(randint(1, 100))], [randint(-1000, 1000) for k in range(randint(1, 100))]
l_samp_list, l_samp_list2 = subj.from_list(sample_list), subj.from_list(sample_list2)

print("Executing tests...")
print("\nNow doing constructor/deconstructors...")
assert subj.to_str(subj.from_list(["яблоко", "витамины", "мускулы", "секс", "спид", "смерть"])) == "яблоко -> витамины -> мускулы -> секс -> спид -> смерть", "ERROR, bad string deconstructor"
assert subj.to_list(l_samp_list) == sample_list, "ERROR: bad list deconstructor"

print("\nNow doing paramethers...")
assert subj.length(l_samp_list) == len(sample_list), "ERROR: bad length counter"

print("\nNow doing link operations...")
assert subj.to_list(subj.append(sample_list[-1], l_samp_list2)) == [sample_list[-1]] + sample_list2, "ERROR: bad append additor"
assert subj.prepend(sample_list2[0], l_samp_list) == sample_list + [sample_list2[0]], "ERROR: bad prepend additor"
assert subj.to_list(subj.copy(l_samp_list)) == sample_list, "ERROR: bad duplicator"
assert subj.to_list(subj.concat(l_samp_list, l_samp_list2)) == sample_list + sample_list2, "ERROR, bad merging method"
assert subj.to_list(subj.remove(l_samp_list, 0)) == sample_list[1::], "ERROR: bad removing method"
assert subj.to_list(subj.remove_all(sample_list[0], l_samp_list)) == None
                    

