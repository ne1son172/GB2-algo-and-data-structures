"""
В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, то вывести загаданное число.
"""

from random import randint

count = 0
num = randint(0, 100)

while count < 10:
    guess = int(input("Make a guess >>> "))
    count += 1

    if guess == num:
        print('You win!!!')
        break
    elif guess < num:
        print('Guess < Num')
    else:
        print('Guess > Num')

print('You lose. Num is: ', num)
