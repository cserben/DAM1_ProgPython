num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))
num3 = int(input("Introduce otro numero: "))

if num1 < num2 and num1 < num3:
    if num2 < num3:
        print(f"{num1} {num2} {num3}")
    else:
        print(f"{num1} {num3} {num2}")
else:
    if num2 < num1 and num2 < num3:
        if num1 < num3:
            print(f"{num2} {num1} {num3}")
        else:
            print(f"{num2} {num3} {num1}")
    else:
        if num3 < num1 and num3 < num2:
            if num1 < num2:
                print(f"{num3} {num1} {num2}")
            else:
                print(f"{num3} {num2} {num1}")