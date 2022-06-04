# and or not
"""
True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""
x = 15
print((x % 5 == 0) and (x % 6 == 0))

"""
True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
x = 15
print((x % 5 == 0) or (x % 6 == 0))
"""
not True -> False
not False -> True
"""

print(6 != 7)

print(not (6 == 7))