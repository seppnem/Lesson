
def sum_range_of_number(start, end):
    total = 0
    for x in range(start, end):
        total = total+x
    return total



result = sum_range_of_number(0, 100)

print(result)

if result > 100:
    print("100 den büyük")

result = sum_range_of_number(1000, 5000)

print(result)


def print_hello_5_times():
    for i in range(5):
        print("hello")

def print_times(times, msg):
    for i in range(times):
        print(msg)

x = print_hello_5_times()
print(x)

print_times(3, "world")

print_times(5, "hello")


