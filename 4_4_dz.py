# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
n = int(input('Задайте число: '))

l = list()
l2 = []
f1 = 0
f2 = 1
for i in range(n):        
    f1,f2 = f2,f1 - f2
    l.append(f1)
l.reverse()
l.append(0)
for i in range(len(l)):
    l2.append(abs(l[i]))        
l2.reverse()
lst = l + l2[1:]
print(lst)

# или

list_negafib = [1, 0]
for i in range(7):
    list_negafib.insert(0, list_negafib[1] - list_negafib[0])
for i in range(8):
    list_negafib.append(list_negafib[-2] + list_negafib[-1])

print(list_negafib)
