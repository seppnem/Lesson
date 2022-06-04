lst = [50, 89, 12, 5, 789]

lst.sort()
print(lst)

lst = [50, 89, 12, 5, 789]
lst.sort(reverse=True)
print(lst)
s_list = sorted(lst)  #lst sort edilmez sort edilmiş yeni liste return edilir

lst2 = ["Canakkale", "Izmir", "Ankara", "Istanbul", "Yozgat"]

lst2.sort(reverse=True)
print(lst2)

def sort_by_len(city):
    return len(city)

def sort_by_last_three(city):
    return city[len(city) - 3::]

lst2.sort(key=sort_by_len)
print(lst2)


lst2.sort(key=lambda city : city[len(city) - 3::]) #alternatif yöntem sort_by_last_three
print(lst2)

a = lambda x : x ** 2
a(10) #100


def foo():
    print("hello")


a = foo
a()

def bar(f):
    f()

bar(foo)

def foo():
    a  = 10
    def tar():
        print("world")