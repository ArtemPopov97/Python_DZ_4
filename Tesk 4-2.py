# 2 - Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности. 
# Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

def EnterCheckNumber():
    while True:
        try:
            n = int(input())
            break
        except:
            continue
    return n

import random
print('Ввведите число элементов последовательности: ')
N1 = EnterCheckNumber()
nums1 = []
for i in range(0,N1):
    nums1.append(random.randint(1,4))
print("List: ", nums1)
nums1new = []
for i in nums1:
    if i not in nums1new:
        nums1new.append(i)
print("Result: ", nums1new)