# conj = {1,2,3,4,5}
# conj.add(5)
# conj.discard(2)
# print(type(conj))
# print(conj)

conj1 = {1, 2, 3, 4, 5}
conj2 = {5, 6, 7, 8, 9}
conj_uni = conj1.union(conj2)
print("uniao: {}".format(conj_uni))

conj_intersect = conj1.intersection(conj2)
print("intersect: {}".format(conj_intersect))

conj_diff1 = conj1.difference(conj2)
print("dif1: {}".format(conj_diff1))
conj_diff2 = conj2.difference(conj1)
print("dif2: {}".format(conj_diff2))


conj_dif1_simetric = conj1.symmetric_difference(conj2)
print("dif1_simetric: {}".format(conj_dif1_simetric))
conj_dif2_simetric = conj2.symmetric_difference(conj1)
print("dif2_simetric: {}".format(conj_dif2_simetric))


conj_a = {1, 2, 3}
conj_b = {1, 2, 3, 4, 5}
conj_subset1 = conj_a.issubset(conj_b)
print("subset1: {}".format(conj_subset1))
conj_subset2 = conj_b.issubset(conj_a)
print("subset2: {}".format(conj_subset2))

conj_superset1 = conj_a.issuperset(conj_b)
print("superset1: {}".format(conj_superset1))
conj_superset2 = conj_b.issuperset(conj_a)
print("superset2: {}".format(conj_superset2))


lista = ["dog", "dog", "cat", "cat", "elephant"]
conj_animal = set(lista)
print("conj_animal: {}".format(conj_animal))
lista_animal = list(conj_animal)
print("lista_animal: {}".format(lista_animal))
