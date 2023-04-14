import random
import math

l = int(input("Введите длину массива: "))
x = int(input("Введите число для поиска: "))

a = []
for i in range(l):
    a.append(random.randint(1, 9))

elem = a[0]
differ = abs(elem-x) 
for j in a:
    if  abs(j-x) <= differ :
        differ = abs(j-x)
        elem = j
        
print (a)
print (elem)