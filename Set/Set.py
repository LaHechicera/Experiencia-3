"""
set:
- Se crean utilizando{}
- Usando la función set()
- Sirven para agrupar conjunto de datos
- No se puede acceder a los datos por un indice, sino que directamente por el valor
- Se pueden iterar
- Los datos no estan ordenados
"""
#1ra manera de definir set
set1 ={10,20,30,40,50}

#2 da manera de definir set
set2 = set([60,70,80,90,100])

#iterar sobre un set
for indice in set1:
    print(indice)

"""
Agregar y eliminar elementos en set()
add(): Agrega un solo elemento
update(): agregamos multiples elementos
remove(): eliminamos un elemento especifico (genera un error, si el elemento no existe)
discard(): eliminamos un elemento especifico (NO genera un error, si el elemento no existe)
clear(): vacia un set
pop(): elimina un elemento aleatorio
"""
#crear un diccionario con set() y agregar un elemento con add
set3 = {1,2,3,4,5}
set3.add(6)
print(set3)

#update
set3.update([1,2,3,4,5,60])
print(set3)

#remove remover un elemento esspecifico
set3.remove(60)
print(set3)

#discard() elemento que no existe en la lista
set3.discard(70)
print(set3)

#discard() elemento que existe en la lista
set3.discard(5)
print(set3)

#ejemplo de .pop()
elemento = set3.pop()
print(f"Elemento eliminado: {elemento}")
print(set3)

#vaciar el diccionario con clear()
set3.clear()
print(set3)

"""
Operaciones de conjuntos:
union(): retorna union de 2 set o conjuntos
intersection(): retorna la interseccion de 2 sets
difference(): retorna la diferencia de 2 sets
symetric_difference(): retorna la diferencia simetrica entre 2 sets

Operadores de conjunto:
| union
& para la interseccion
- para la diferencia
^ para la diferencia simétrica

"""
set_a = {1,2,3,4,5}
set_b = {3,4,5,6,7}

#union de 2 set nombre_nuevo_set = set1.union(set2)
set_nuevo= set_a.union(set_b)
print(set_nuevo)

#intersección .intersection()
set_nuevo2= set_a.intersection(set_b)
print(set_nuevo2)

#symetric_difference()
setsymetric = set_a.symmetric_difference(set_b)
print(f"La diferencia simetrica es: {setsymetric}")

#diference() da la diferencia de un set con el otro
setdiference = set_a.difference(set_b)
print(f"Set con diference {setdiference}")

setdiference2 = set_b.difference(set_a)
print(f"Set con diference {setdiference2}")

"""
| = union
& = interseccion
- = diferencia
^ = diferencia simetrica
"""
#Union con operador |  ... set_nuevo = se1 | set2
setnuevo_union = set_a | (set_b)
print(setnuevo_union)

# & 
setnuevo_inter = set_a & (set_b)
print(setnuevo_inter)

#-
setnuevo_dif = set_a - (set_b)
print(setnuevo_dif)

# ^
setnuevo_difsim = set_a ^ (set_b)
print(setnuevo_difsim)

""""
Principales métodos
.copy()
isdisjoint(): retorna un booleano True si entre dos sets no hay elementos en comun
issubset(): retorna un si, sui es un subconjunto de otro set
issupertset(): retorna True si un superconjunto de otro
"""
set_h = {1,2,3}
set_i = {2,3,4}
set_j = {1,2,3,4,5}
set_k = {5,6,7}

#copiar un set con copy()
setcopia = set_a.copy()
print(setcopia)

#verificar si no tienen elementos en comun
print (set_h.isdisjoint(set_k))# devuelve True por que los set tienen elementos diferentes
print(set_h.isdisjoint(set_i)) #devuelve un False por que los sets tienen elementos en comun



