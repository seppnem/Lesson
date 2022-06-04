def countrange(lst, min, max):
    counter = 0
    for i in lst:
        if min <= i <= max:
            counter += 1
    return counter


def main():
    lst = [40, 4, 5, 15, 100]
    min = 2
    max = 10
    print(countrange(lst, min, max)) # 2

main()
