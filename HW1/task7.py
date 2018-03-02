"""
По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков.
Если такой треугольник существует,
то определить, является ли он
равносторонним, равнобедренным или равносторонним.
"""

a = float(input('Enter 1st length >>> '))
b = float(input('Enter 2nd length >>> '))
c = float(input('Enter 3rd length >>> '))
summ1 = a + b
summ2 = a + c
summ3 = b + c

if (c < summ1) and (b < summ2) and (a < summ3):
    print('There is a possibility for triangle')
    if a == b and b == c:
        print('It is equilateral triangle')
    elif a == b or b == c or a == c:
        print('It is isosceles triangle')
    else:
        print('It is versatile triangle')
else:
    print('There is NO possibility for triangle')
