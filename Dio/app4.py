a = int(input("Entre com um numero: "))

div = 0
for x in range(1, +a + 1):
    resto = a % x
    print(a, resto)
    if resto == 0:
        div += 1

    if div == 2:
        print("num {} é primo".format(a))
    else:
        print("num {} é par".format(a))
