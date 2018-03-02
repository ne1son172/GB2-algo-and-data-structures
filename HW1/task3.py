# По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через эти точки.

x1 = int(input("Enter x1 >>> "))
y1 = int(input("Enter y1 >>> "))
x2 = int(input("Enter x2 >>> "))
y2 = int(input("Enter y2 >>> "))

temp1 = x1 - x2
temp2 = y1 - y2
k = temp2 / temp1

temp3 = k * x1
b = y1 - temp3

print("The required equation is: Y = {} * X + ({})". format(k, b))
