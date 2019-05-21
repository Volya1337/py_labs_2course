s = float(input("Введите корень, который хотите извлечь: "))

x = 1
while abs(x * x - s) > 0.00001:
    x = (x * x + s) / 2 / x
print(x)