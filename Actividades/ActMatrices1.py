"1. Crear un Arreglo [3][4] para luego ingresar elementos numéricos por pantalla utilizando doble for, mostrar los elementos por pantalla de forma ordenada como una matriz, tal cual muestra el ejemplo:"
"3	10	 4	16"
"1	 7 	 8	-7"
"9	-1	 3	 9"

matriz2d = [
    [3,10,4,16],
    [1,7,8,-7],
    [9,-1,3,9]
]

for fila in matriz2d:
    print(fila)


"""
2. Crear un Arreglo [3][3][3] manualmente, los valores del arreglo pueden ser “amarillo”, “rojo”, “Naranja”, “Verde” y “Blanco”.
Una vez completado, mostrar la siguiente información:
●	Número de elementos “amarillo”.
●	Número de elementos “rojo”.
●	Número de elementos “Naranja”.
●	Número de elementos “Verde”.
●	Número de elementos “Blanco”"
"""

colores = [
    [
        ["amarillo","rojo","naranja"]
    ],
    [
        ["verde","blanco","amarillo"]
    ],
    [
        ["rojo","naranja","verde"]
    ]
]

for i in colores:
    for l in i:
        for c in i:
            print



#Codigo Eric
matriz_3d = [
    [
        ["amarillo","rojo","naranja"],
        ["rojo","verde","amarillo"],
        ["rojo","verde","amarillo"]
    ],
    [
        ["verde","amarillo","blanco"],
        ["amarillo","verde","naranja"],
        ["verde","amarillo","blanco"]
    ],
    [
        ["blanco","rojo","blanco"],
        ["naranja","verde","amarillo"],
        ["verde","amarillo","blanco"]
    ]
]

print(matriz_3d)
amarillo = 0
rojo = 0
naranja = 0
verde = 0
blanco = 0
len(matriz_3d)
for dimension in matriz_3d:
    for fila in dimension:
        for elemento in fila:
            if elemento == "amarillo":
                amarillo = amarillo + 1
            if elemento == "rojo":
                rojo = rojo + 1
            if elemento == "naranja":
                naranja = naranja + 1
            if elemento == "verde":
                verde = verde + 1
            if elemento == "blanco":
                blanco = blanco + 1

print (f"numero de elementos 'amarillo': {amarillo}")
print (f"numero de elementos 'rojo': {rojo}")
print (f"numero de elementos 'naranja': {naranja}")
print (f"numero de elementos 'verde': {verde}")
print (f"numero de elementos 'blanco': {blanco}")




    

    





