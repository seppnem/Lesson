students = {10: "ayse", 20 : "fatma"}

for key in students:  # students.keys()
    print(key, students[key])


for val in students.values():
    print(val)

t = (10, 20)
x = t[0]
y = t[1]
x, y = t  # tuple unpack

for k, v in students.items():   # (10, "ayse")
    #item[0]  item[1]
    print(k , v)


print(students.keys())
print(students.values())
print(students.items())


val = students.pop(10)
print(val)
print(students)

val = students.get(20)  # students[20]
print(val)
print(students)

val = students.get(100) # get olmayan key için valuyu None return eder
print(val)

#val = students[100] # KeyError: 100
#print(val)

students.clear()
print(students)