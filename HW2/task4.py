"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

quantity = int(input('Enter quantity of members of the series >>> '))
summ = 1
count = 1

while count < quantity:
    if count % 2 == 0:
        summ += 1 / (2 ** count)
        count += 1
    else:
        summ += (-1) * (1 / (2 ** count))
        count += 1

print('Sum of {} members of the series is:  {}'.format(quantity, summ))
