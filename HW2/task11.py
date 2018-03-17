# Вывести какой-либо символ по диагоналям воображаемого квадрата

nums = 10
symbol = 's'

for i in range(nums):
    values = list()

    for j in range(nums):
        j_inverse_idx = nums - 1 - j

        if not i - j or j_inverse_idx == i:
            item = str(symbol)
        else:
            item = str(i + j)

        value = '{:^4}'.format(item)
        values.append(value)

    line = ''.join(values)
    print('\n', line)
