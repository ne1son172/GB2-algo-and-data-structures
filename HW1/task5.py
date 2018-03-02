#Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

from math import fabs

char1 = input('Print first char >>> ')
char2 = input('Print second char >>> ')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
index1 = alphabet.find(char1) + 1
index2 = alphabet.find(char2) + 1
quantity = int(fabs(index1 - index2))

print('{} is on the {}th place'.format(char1, index1))
print('{} is on the {}th place'.format(char2, index2))
print('There is {} letters between {} and {}'.format(quantity, char1, char2))
