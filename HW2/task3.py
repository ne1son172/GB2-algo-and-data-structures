"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843
"""

num = input('Enter some natural number >>> ')
temp = num[::-1]
print('Reverse number is: ', temp)

# не совсем понял задачу: можно, конечно, реализовать через циклы
# но это же неоптимальное решение
