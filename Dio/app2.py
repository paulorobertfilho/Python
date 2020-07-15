a = 10
b = 5
soma = a + b
sub = a - b
mult = a * b
div = a / b
resto = a % b

resultado = (
    "Soma: {soma}. \nSubtração: {sub}. \nMultiplicação: {mult}."
    "\nDivisão: {div}. \nResto:{resto}.".format(
        soma=soma, sub=sub, resto=resto, mult=mult, div=div
    )
)
print(resultado)

# print(type(soma))
# print("soma: " + str(soma))
# print(sub)
# print(mult)
# print(div)
# print(resto)
