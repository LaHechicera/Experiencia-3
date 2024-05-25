"2)	Cree 2 listas, en las cuales se guardará 3 nombres y 3 apellidos (1 lista para nombres y una 1 lista para apellidos), el sistema deberá mostrar de forma ordenada los nombres y apellidos."

print("----Escriba los 3 nombres y primer apellido del grupo----")
print(" ")
nom1 = input("Primer nombre: ")
ape1 = input("Primer apellido: ")
nom2 = input("Segundo nombre: ")
ape2 = input("Primer apellido: ")
nom3 = input("Tercer nombre: ")
ape3 = input("Primer apellido: ")
print(" ")

lista_nombres = [nom1, nom2, nom3]
lista_apellidos = [ape1, ape2, ape3]

for l1, l2 in zip(lista_nombres, lista_apellidos):
    print(l1, l2)

