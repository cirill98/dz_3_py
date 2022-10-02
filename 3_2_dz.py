# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
value = int(input('Введите кол-во значений: '))
l = []
l2 = []
for i in range(value):
    num = int(input('Введите значение: '))
    l.append(num)
while l:
    if len(l) == 1:
        c = l.pop(0)
        c *=c
        l2.append(c)
    else:
        count = l.pop(0) * l.pop(-1)
        l2.append(count)
print(l2)

# или

import math
list = [2, 3, 5, 6]
result = []              

n = math.ceil(len(list) / 2)
for i in range(n):
    result.append(list[i] * list[-i - 1])
print(result)
