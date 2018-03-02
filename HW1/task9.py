# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

a = float(input('Enter 1st number >>> '))
b = float(input('Enter 2nd number >>> '))
c = float(input('Enter 3rd number >>> '))

if a > b:
    if a < c:
        print('The middle number is: ', a)
    else:
        if b > c:
            print('The middle number is: ', b)
        else:
            print('The middle number is: ', c)
else:
    if a > c:
        print('The middle number is: ', a)
    else:
        if b > c:
            print('The middle number is: ', c)
        else:
            print('The middle number is: ', b)
