
"""
for i in range(1, 5):
    for j in range(1, 5):
        print(i * j, end=" ")
    print("-")
"""
"""
*
**
***
****
*****
"""

N = int(input("Enter a row count"))

for i in range(N):
    for j in range(i + 1):
        print("*", end="")
    print()


"""
    *   i 0     4 " "  1 *
   **   i 1     3 " "  2 *
  ***
 ****
*****   i 4     0 " "  5 *  
"""
s = N - 1
a = 1
for i in range(N):
    for j in range(s - i):
        print(" ", end="")
    for j in range(a + i):
        print("*", end="")
    print()