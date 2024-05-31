"""
Diccionario: conjunto de datos estructurados mediante "clave" : valor
Se definen con {}
Claves pueden ser textos números y cadenas
Valores pueden ser cualquier tipo de dato
"""

#1ra manera
diccionaro_1 = {
    "Marca" : "Toyota",
    "Modelo" : "Yaris",
    "Año" : 2020
}

#2da manera
diccionario_alumnos = dict(nombre="Miguel", apellido="Perez", edad= 30)
print(type(diccionario_alumnos))

#actualizar un elemento: llamo a mi diccionario["clave"]= valor o string ""

diccionaro_1["Año"]= 2017
print(diccionaro_1)

#actualizar con .update: nombre diccionario.update({"clave": dato a actualizar})

diccionaro_1.update({"Marca": "Ford"})
print(diccionaro_1)

"""
eliminar elementos
del 
pop() elimina el último elemento clave
popitem() elimina el ultimo par "clave:valor"
clear() vacia el diccionario, borra todo

diccionaro_1 = {
    "Marca" : "Toyota",
    "Modelo" : "Yaris",
    "Año" : 2020
}
"""
#pop()
#diccionaro_1.pop("Año")
print(diccionaro_1)

#popitem() no necesita argumento, elimina el ultimo item del diccionario
diccionaro_1.popitem()
print(diccionaro_1)

#clear()
diccionaro_1.clear()
print(diccionaro_1)

"""
len() cuenta
str() retorna una representación del diccionario en cadena
keys() Claves
values() Valor
items() una vista de todos los pares clave valor
copy() realiza una copia de diccionario
"""

diccionaro_auto = {
    "Marca" : "Toyota",
    "Modelo" : "Yaris",
    "Año" : 2020
}

#len()
print(len(diccionaro_auto))

#str()
print(str(diccionaro_auto))

#keys()
print(diccionaro_auto.keys())

#values()
print(diccionaro_auto.values())

#items
print(diccionaro_auto.items())

#copiar un diccionario nombre_new_dict = diccionario.copy()
diccionario_autos_copia = diccionaro_auto.copy()
print(diccionario_autos_copia)

#Iterar sobre las claves "for" indice in "dict":
#print()
for key in diccionaro_auto:
    print(key)

# iterar sobre los valores .values()
for key in diccionaro_auto.values():
    print(key)

#iterar sobre clave valor: for indice1, indice2 in dict.items():
#print(indice1, indice2)
for key1, key2 in diccionaro_auto.items():
    print(key1, key2)

