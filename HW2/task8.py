"""
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры
"""

from random import randint

count = 0
index = 0
result = 0
numlist = []

num = int(input("Enter quantity if numbers >>> "))
digit = input("Enter desirable digit >>> ")

while count < num:
    temp = str(randint(0, 100))
    numlist.append(temp)
    count += 1

print("Numlist is: ", numlist)

for index in range(len(numlist)):
    temp = numlist[index].count(digit)
    result += temp
    index += 1

print('Result is: ', result)
