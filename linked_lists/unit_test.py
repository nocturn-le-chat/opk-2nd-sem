from main import Linked_list as subj

assert subj.to_str(subj.from_list(["яблоко", "витамины", "мускулы", "секс", "спид", "смерть"])) == "яблоко -> витамины -> мускулы -> секс -> спид -> смерть", "ERROR, bad string deconstructor"
