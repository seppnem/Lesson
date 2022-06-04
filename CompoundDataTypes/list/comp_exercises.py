lst = list(range(1, 20))
#lst = list("hello")

print(lst)

c = []
for i in lst:
    c.append(i ** 3)



cubes = [i ** 3 for i in lst]
print(cubes)


#conditional exp
#true_exp if log_exp else false_exp

boolean_lst = [True if i % 2 == 0 else False for i in lst]
print(boolean_lst)
boolean_lst = [1 if i % 2 == 0 else -1 for i in lst]

boolean_lst = [i % 2 == 0 for i in lst]
print(boolean_lst)

names = ["ali", "fatma", "zeynep", "veli"]
#print(names[-4])
#names[0]

print(len(names))

n = "ali"
len(n)


name_len = [len(name) for name in names]
sum(name_len)


name_len = [len(name) for name in names]
print(name_len)

upper_name = [a.upper() for a in names]
print(upper_name)

reverse_names = [n[::-1] for n in names]
print(reverse_names)

rev_names_lst = names[::-1]
print(rev_names_lst)

#names[-1][0]

reverse_names_2 = [n[::-1] for n in names[::-1]]
print(reverse_names_2)


names_starts_with_z = [n for n in names if n[0].lower() == 'z']
res = []
for n in names:
    if n[0].lower() == "z":
        res.append(n)




names_starts_with_z = [n for n in names if n.startswith("z")]
print(names_starts_with_z)