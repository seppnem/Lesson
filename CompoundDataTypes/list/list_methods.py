lst = [10, 20, 30]


lst.append(40)

print(lst)
lst.extend([50, 60, 70])
print(lst)

print(lst.pop(0))
print(lst)

print(lst.remove(70))
print(lst)

lst.reverse()
print(lst)

rev_lst = lst[::-1]
print(lst)
print(rev_lst)

lst.insert(3, 999)
print(lst)



lst.clear()
print(lst)

"""
self metotdu çağıran nesnedir 
class  mylst:
    def insert(self, ind, value):
        pass
"""
