# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь


while True:
    print("insert some 3-digit number or Q for quit")
    m = input()
    if m == 'q' or m == 'Q':
        break
    else:
        a = int(m[0])
        b = int(m[1])
        c = int(m[2])
        sum = a + b + c
        comp = a * b * c
        print("Summ of figits is: ", sum)
        print("Composition of digits is: ", comp)
