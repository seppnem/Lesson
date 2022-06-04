"""
s = "hello"

for i in range(len(s)):
    print(s[i])


for ch in s:
    print(ch)


for i, ch in enumerate(s, 10):
    print(i, ch)
"""


def print_indexes(s, search):
    for i, ch in enumerate(s):
        if ch == search:
            print(i)



def print_substrings(s, search):
    start = 0
    for i, ch in enumerate(s):
        if ch == search:
            print(s[start:i + 1])
            start = i
    print(s[start + 1:])

s = "Hello world mars jupyter space"

search = "a"
print_indexes(s, search)

print_substrings(s, search)



