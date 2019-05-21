while True:
    print("Если введете 0, то программа завершит работу")
    s = input("Введите знак : (+,-,*,/) ")
    if s == "0":
        break
    if s in ("+","-","*","/"):
        try:
            a = float(input("Введите а: "))
            b = float(input("Введите b: "))
        except ValueError:
            print("Нужно ввести число")
        else:
            if s == "+":
                print(a + b)
            elif s == "-":
                print(a - b)
            elif s == "*":
                print(a * b)
            elif s == "/":
                if b == 0:
                    print("Деленеие на 0!")
                else:
                    print(a / b)
    else:
        print("Неправильный знак!")
