"""
Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n - любое натуральное число
"""

count = 0
summ = 0
n = int(input('Enter number if members of the series >>> '))

comp = 0.5 * n * (n+1)

while count < n:
    count += 1
    summ += count

if summ == comp:
    print('Equality is proved: Sum = Comp = ', summ)
else:
    print('Error in program: check the code')
