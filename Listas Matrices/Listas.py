""""
LISTAS
Tipos de datos que permiten almacenar cualquier tipo de  dato.
- Mantienen el orden con el que fueron definidas.
- Se pueden anidar
- Son mutables: pueden ser modificadas
- Son dinamicas: que se pueden añadir y eliminar elementos.
"""

#Definimos las listas con []
lista = [1,2,3,4,5,6,7,8,9]
lista_variada = [123,"Hola", 3.4, True]

#imprimir un dato especifico
print(lista_variada[3])
print(lista_variada[-1])

#cambiar un elemento
lista_variada[3] = False
print(lista_variada)

#eliminar un elemento
del lista_variada[3]
print(lista_variada)

#agregar un rango a mi lista
lista[9:12]=[10,11,12]
print(lista)

#asignar una lista a variables
lista_numeros = [1,2,3]
a,b,c=lista_numeros
print(a)
print(b)
print(c)

#iterar una lista
#lista = [1,2,3,4,5,6,7,8,9]
for l in lista:
    print(l)

#imprimir la posicion de la lista
for index, l in enumerate(lista):
    print(f"Indice: {index}, número lista: {l}")

#unir dos listas
lista1=[2,5,9]
lista2=["Jazz", "Rock", "Metal"]
#unimos las listas
for l1, l2 in zip(lista1, lista2):
    print(l1, l2)

#agregar elemento a una lista (se agregar al final de la lista)
lista.append(14)
print(lista)

#ordenar lista (con funcion .sort)
lista_desordenada=[6,8,7,4,2,3,96,15]
lista_desordenada.sort()#oordena de menor a mayor
lista_desordenada.sort(reverse=True) #ordena de mayor a menor
print(lista_desordenada)

#eliminar el ultimo elemento
lista_nueva=[1,2,3]
lista_nueva.pop()
print(lista_nueva)

lista_desordenada.reverse #otra manera de ordenar de mayor a menor
print(lista_desordenada)