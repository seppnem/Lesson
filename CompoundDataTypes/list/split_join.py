s = "Merhaba, hello, nasılsın, iyiyim, nerelisin"

lst = s.split()
print(lst)

lst = s.split(",")
print(lst)

lst2 = []
for word in lst:
    lst2.append(word.strip())

print(lst2)

for i in range(len(lst)):
    lst[i] = lst[i].strip().title()

print(lst)


result_str = ";".join(lst)
print(result_str)

