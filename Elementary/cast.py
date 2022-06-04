a = "10"

b = 3 * a
print(b)

b = 3 * int(a)
print(b)

a = "sebnem"
#b = 3 * int(a) # ValueError: invalid literal for int() with base 10: 'sebnem'

a = str(100)
print(type(a))
print(a + "hello", 200, sep="*")

f = float(10)
print(f)

print(bool(5.))
print(bool(-5.))
print(bool(0.))

print(bool(""))
print(bool(" "))
print(bool("hello"))