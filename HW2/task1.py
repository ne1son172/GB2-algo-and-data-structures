"""
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
"""

num1 = 0
num2 = 0
sign = 0

while sign != '0':
    num1 = float(input('Insert number 1 >>> '))
    num2 = float(input('Insert number 2 >>> '))
    sign = input('Insert sign >>> ')

    if sign == '+':
        summ = num1 + num2
        print('Summ = ', summ)
    elif sign == '-':
        diff = num1 - num2
        print('Difference = ', diff)
    elif sign == '*':
        comp = num1 * num2
        print('Composition = ', comp)
    elif sign == '/':
        if num2 == 0:
            print('Error: you can not divide by zero. Please, try again')
        else:
            quot = num1 / num2
            print('Quotient = ', quot)
    elif sign == '0':
        continue
    else:
        print('Wrong sign-format! You can use  +, -, *, / or 0. Please, try again.')
