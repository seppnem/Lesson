#      0    1   2
lst = [10, 20, 30]

lst[0]  # read
lst[0] = 20
lst.append(40)

d = {}  #empty dict
d = {0 : 10, 1 : 20, 2 : 30}
d[0]
d[0] = 20
d[3] = 40
print(d)
"""
students = {"ayse": [235, 25], "fatma":[569, 25]}
print(students["ayse"])
print(students)
"""

students = {235 : ["ayse", 25], 569 : ["fatma", 25]}
print(students[569])
students[569] = ["deniz", 25] # update
print(students)
students[601] = ["ali", 18] # append
print(students)
del students[601]
print(students)


"""
a = 10
print(a)
del a
print(a) # NameError: name 'a' is not defined
"""
"""
l = [10, 20]
del l[0]
print(l)
del l
print(l) # NameError: name 'l' is not defined
"""




