"""
Написать программу, которая генерирует в указанных пользователем границах
    -случайное целое число,
    -случайное вещественное число,
    -случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

from random import randint, uniform, choice

while True:
    mode = input("Choose Int, Float, Char or Quit (type only 1st letter) >>> ")
    if mode == 'q' or mode == 'Q':
        break
    elif mode == 'i' or mode == 'I':
        leftborder = int(input('Enter left border >>> '))
        rightborder = int(input('Enter right border >>> '))
        intresult = randint(leftborder, rightborder)
        print('Random integer in [{}, {}] is: {}'. format(leftborder, rightborder, intresult))
    elif mode == 'f' or mode == 'F':
        leftborder = float(input('Enter left border >>> '))
        rightborder = float(input('Enter right border >>> '))
        floatresult = uniform(leftborder, rightborder)
        print('Random float in [{}, {}] is: {}'.format(leftborder, rightborder, floatresult))
    elif mode == 'c' or mode == 'C':
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        leftborder = input('Enter left border >>> ')
        rightborder = input('Enter right border >>> ')
        leftindex = alphabet.find(leftborder)
        rightindex = alphabet.find(rightborder)
        subaplhabet = alphabet[leftindex:rightindex:1]
        charresult = choice(subaplhabet)
        print('Random char in [{}, {}] is: {}'.format(leftindex, rightindex, charresult))
    else:
        print('Wrong choice; try again')
