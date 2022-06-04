
lst = []
while True:
  word = input("enter your word")
  if not word:
    break
  if word not in lst:
    lst.append(word)

print(lst)