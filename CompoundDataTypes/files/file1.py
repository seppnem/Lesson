# r w a    text dosyalar
# rb wb ab  binary files


file = open("hello.abc", "w")
file.write("hello \n world")
file.close()

file = open("names.dat", "w")
lst = ["ayse", "fatma", "ali"]

for name in lst:
    file.write(name + "\n")

file.close()

file = open("names.dat", "a")
file.write("berke\n")
file.close()


f = open("names.dat", "r")
name1 = f.readline()
print("First line", name1, end="")
print(f.tell())
f.seek(0)
for line in f.readlines():
    print(line, end="")

f.seek(0) #file pointer dosyanın başına getirir
for line in f:
    print(line)

f.close()

f = open("hello.abc", "r")
#file operations
f.close()

with open("hello.abc", "r") as f:
    # file operations
    print(f.read(2))
    # f.seek(0)
    print(f.read())





