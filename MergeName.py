def unique_names(names1, names2):
	set1=set(names1)
	set2=set(names2)
	return list(set1.union(set2))

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]

print(unique_names(names1, names2))