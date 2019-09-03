lista = [1, 3, 5, 7]
lista_animal = ["cat", "dog", "elephant"]

lista_animal[0] = "macaco"
print(lista_animal)

tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_num = list(tupla)
print(type(lista_num))
lista_num[0]=100
print(lista_num)


# print(lista_animal[1])
# nova_lista = lista_animal*3
# print(nova_lista)
# lista.sort()
# for x in lista_animal:
#   print(x)
