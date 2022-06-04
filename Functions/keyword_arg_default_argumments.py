def myrange(stop):
    if not isinstance(stop, str):
        print("TypeError: 'str' object cannot be interpreted as an integer")
        return



def print_times(times, msg="hello", arg1=8):
    for i in range(times):
        print(msg)


#positional arg.
print_times(5, "hello", 8)

#keyword arg
print_times(msg="world", times=3, arg1=8)

print_times(5, arg1=8, msg="hello")


print(5)
print(3, "merhaba")


