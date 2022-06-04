#mutable
#farklı türler saklayabilir


lst = []  #empty list
print(lst)

lst = [10, 20, "hello", True]
print(lst)

lst1 = [10, 20, 50]
lst2 = [10, 40]
print(lst1 + lst2)
print(lst1 * 3)


lst[0]
lst[-1]

lst[0] = 99
print(lst)


lst5 = lst[0:2]
print(lst5)

if 99 in lst:
    print("YES")

lst = [99, 20,  True]  #'hello',
print(len(lst))
print(max(lst))
print(min(lst))
print(sum(lst))

