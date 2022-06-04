s = "hello"

print(s.count("l"))

print(s.count("ğ"))

lst = ["hello", "mello", "world"]

for s in lst:
    if s.endswith("lo"):
        print(s)
    if s.startswith("m"):
        print(s)

s = "hello"
name = "Sebnem"

greeting = s.upper() + " " + name
print(greeting)
print(s)

s = s.upper()


print(s)

s1 = s.replace("L", "x")
print(s1)
s = "hello"
s2 = s[0:s.find("l")] + "X" + s[s.find("l") + 1:]
print(s2)

s = "     Hello   "
s1 = s.strip()
s.lstrip()
s.rstrip()
print(s)
print(s1)
