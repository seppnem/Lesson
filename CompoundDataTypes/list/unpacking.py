lst = [10, 20]

x = lst[0]
y = lst[1]

print(x, y)

x, y = lst

print(x, y)

lst = [10, [5, [1, 2]], 20]

x, [m, [a, b]], z = lst

print(x, m, a, b, z)


t = (10, 20, 30)
a, _, c = t
print(a, c)
