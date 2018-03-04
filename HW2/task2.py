"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)
"""

naturnum = input('Enter some natural number >>> ')
count = 0
evensum = 0
oddsum = 0

for count in range(len(naturnum)):
    temp = int(naturnum[count])

    if temp % 2 == 0:
        evensum += temp
    else:
        oddsum += temp

print('Even sum = ', evensum)
print('Odd sum = ', oddsum)
