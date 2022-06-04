def find_min_max(lst):
    a = min(lst)
    b = max(lst)
    return a, b


def swap_values(a, b):
    b, a = a, b  #unpacking
    return a, b



l = [50, 40, 10, 89, 1258]
result = find_min_max(l)
print(result)

print("Min is", result[0], "Max is ", result[1])



#x, y, _ = foo()


t = swap_values(10, 20)
print(t[0])
print(t[1])

