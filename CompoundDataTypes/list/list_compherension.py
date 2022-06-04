
lst = []
for i in range(0, 20):
    #if i % 2 == 0:
    lst.append(i * 10)

print(lst)

# new_lst = [expression for v in iterable]

lst = [i * 10 for i in range(0, 20)]
print(lst)

lst = []
for i in range(0, 20):
    if i % 2 == 0:
        lst.append(i * 10)

lst = [i for i in range(0, 20) if i % 2 == 0]
print(lst)


# conditional expression
x = 10
sign = 0
if x > 0:
    sign = 1
else:
    sign = -1

sign = 1 if x > 0 else -1



lst = [-20, -23, 10, 56, -2, 89]
# lst2 = [-1, -1, 1, 1, -1, 1]

lst = [1 if i > 0 else -1 for i in lst]
print(lst)
