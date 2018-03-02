# Определить, является ли год, который ввел пользователем, високосным или не високосным

while True:
    year = input('Enter q for quit or enter some year >>> ')
    if year == 'Q' or year == 'q':
        break
    else:
        year = int(year)
        temp = year % 4
        if temp == 0:
            print('{} year is leap-year'.format(year))
        else:
            print("{} is regualr year".format(year))
            