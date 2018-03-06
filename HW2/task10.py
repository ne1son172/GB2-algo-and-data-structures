"""
Вывести на экран "прямоугольник", образованный из двух видов символов.
Контур прямоугольника должен состоять из одного символа, а в "заливка" - из другого
"""

indexw = 0
length = int(input('Enter length of rectangle >>> '))
width = int(input('Enter width of rectangle >>> '))

print('*' * length)
indexw += 1

while True:
    if indexw == width - 1:
        print('*' * length)
        break

    print('*' + ('-' * (length - 2)) + '*')
    indexw += 1
