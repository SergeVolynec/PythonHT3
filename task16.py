import random

l = int(input("Введите длину массива: "))
x = int(input("Введите число для поиска: "))

a = []
for i in range(l):
    a.append(random.randint(1, 9))

count = 0
for j in range(l):
    if a[j] == x:
        count += 1
        
print (a)
print(count)
