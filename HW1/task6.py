# Пользователь вводит номер буквы в алфавите. Определить, какая это буква

alphabet = 'abcdefghijklmnopqrstuvwxyz'
numchar = int(input('Enter No. of char >>> ')) - 1
print('This is letter: {}'.format(alphabet[numchar]))
