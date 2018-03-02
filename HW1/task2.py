# Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
# Объяснить полученный результат.

a = 5
b = 6
print("a = {}; b = {}".format(a, b))

andres = a & b
print("Result of (a & b) is: ", andres)

orres = a | b
print("Result of (a | b) is: ", orres)

xorres = a ^ b
print("Result of (a ^ b) is: ", xorres)

aleft = a << 2
print("Result of (a << 2) is: ", aleft)

aright = a >> 2
print("Result of (a >> 2) is: ", aright)
