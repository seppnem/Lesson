s = "Hello"

#+ ve *

s1 = s + " " + "World"
print(s1)

s2 = s * 3
print(s2)

print(len(s))
print(max(s))
print(min(s))
# print(sum(s))

# < > <= >= != ==

s1 = "abc"
s2 = "ad"

print(s1 > s2)
print(s1 < s2)

print(s1 == s2)
print(s1 != s2)


# in not in    -> contains

s = "Hello"
print("h" in s)
print("H" in s)
print("el" in s)

print("Hel" not in s)


# getitem , index ops
#01234
s = "Hello"
#-5-4-3-2-1
print(s[0])
print(s[1])

print(s[len(s) - 1])

print(s[-1])
print(s[-2])
print(s[-len(s)])


# s[0] = "M" #str' object does not support item assignment


#slicing


