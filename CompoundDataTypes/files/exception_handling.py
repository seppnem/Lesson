"""
try:
    file = open("not_found.txt")
except FileNotFoundError:
    print("File not found, ")
"""

"""
try:
    val = int(input("Enter an integer"))
    result = 100 / val
    print(result)

except ZeroDivisionError as zde:
    print("sıfıra bölme hatası")
except ValueError as ve:
    print("tam sayı girmdiniz")
except Exception as e:
    print(type(e), "Bilinmeyen hata")
finally:
    print("finally block")

print("hello")
"""
"""
is_valid = False
while not is_valid:
    try:
        val = int(input("Enter an integer"))
        is_valid = True

    except ValueError as ve:
        print("geçersiz tam sayı")

print(val / 5)
"""

while True:
    try:
        val = int(input("Enter an integer"))
        break

    except ValueError as ve:
        print("geçersiz tam sayı")

print(val // 5)