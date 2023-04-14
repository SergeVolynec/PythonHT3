

word = input("Введите слово: ").lower()
points = {tuple('aeioulnstrавеинорст'): 1, tuple('dgдкллмпу'): 2, tuple('bcmpбгёья'): 3,  tuple('fhvwyйы'): 4, 
        tuple('kжзхцч'): 5, tuple('jxшэю'): 8, tuple('qzфщъ'): 10 }
total = 0
for i in word:
    for j in points:
        if i in j:
            total += points.get(j)
print(total)
