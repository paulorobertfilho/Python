a = input("Primeiro value: ")
b = input("Segundo value: ")
if a > b:
    print("Maior nº é o {}".format(a))
else:
    print("Maior nº é o {}".format(b))


c = int(input("Entre com valor inteiro: "))
resto = c % 2
if resto == 0:
    print("Par")
else:
    print("Impar")
