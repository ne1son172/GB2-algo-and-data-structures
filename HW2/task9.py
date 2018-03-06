"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

nums = []
index = 0
summ = 0
count = 0

while True:
    tempnum = input("Enter some natural number or Q further actions >>> ")
    if tempnum == 'q' or tempnum == 'Q':
        break
    nums.append(tempnum)

while index < len(nums):
    sumtemp = 0

    for i in range(len(nums[index])):
        temp00 = nums[index]
        digit = int(temp00[i])
        sumtemp += digit

    if sumtemp > summ:
        summ = sumtemp
        count = index
        index += 1
    else:
        index += 1

print('Number is: {}; Sum is: {}'.format(nums[count], summ))

