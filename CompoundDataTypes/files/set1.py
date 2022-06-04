s1 = set()

s2 = {10, 20}   # {"hello": 3, "World":5}

lst = [10, 10, 30, 89, 10, 20, 20]
lst2 = []
for num in lst:
    if num not in lst2:
        lst2.append(num)

print(lst2)

distinct_nums = set(lst)
print(distinct_nums)

s1 = {10, 20, 30}
s2 = {30, 50}

us = s1.union(s2)
us = s2.union(s1)
us = s1 | s2
print(us)

ins = s1.intersection(s2)
ins = s2.intersection(s1)
ins = s1 & s2
print(ins)

ds = s1.difference(s2)
ds = s1 - s2
print(ds)

print(s1.issubset(s2))
s1 = {10}
s2 = {10, 20}
print(s1.issubset(s2))
print(s2.issuperset(s1))

s2.add(50)
print(s2)





