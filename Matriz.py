"""
Objetivos de la clase:
- Comprender que es una matriz y como se utiliza en python
- Diferenciar entre una matriz unidimensioinal, bidimensional y multidimiensional
"""
"""
Definición de una matriz: es una estructura de datos que puede tener multiples dimensiones.
"""

#Matriz unidimensional,, pueden ser en orden vertical y horizontal
matriz_1d = [1,2,3,4,5,6] #Lista o Vector

#acceder a un dato especifico
dato_especifico = matriz_1d[0]

#actualizar dato especifico
matriz_1d[0]= 100
print(matriz_1d)

#Agregar un elemento a mi matriz con .append()
matriz_1d.append(23)
print(matriz_1d)

#Eliminar un alemento con .remove()
matriz_1d.remove(3)
print(matriz_1d)

#oredenar matriz con .sort() de menor a mayor y .sort(reverse=True) de mayor a menor 
matriz_desordenada= [1,4,56,7,4,3,2,99,100,2333,4,0,]

matriz_desordenada.sort()
print(matriz_desordenada)
matriz_desordenada.sort(reverse=True)
print(matriz_desordenada)

#Matriiz bidimensional: Es una lista de listas
matriz_2d = [
    [1,2,3], #0
    [4,5,6] #1
]
#Acceder a un elemento especifico, El: 6 [Fila][Columna]
resultado_m2d = matriz_2d[1][1]
print(resultado_m2d)

#Modificar el número 6 por un número 60
matriz_2d[1][2] = 60
print(matriz_2d)
print(matriz_2d[1][2])

#Recorrer una matriz bidimensional con ciclo for: 1er for recorre filas y el 2do for recorre columnas: for fila in matriz_2d y luego abajo for columna in fila:

for fila in matriz_2d:
    for columna in fila:
        print(columna)


#Mtriz multidimensionales: es una matriz que extiende su contenido a multiples dimensiones.

matriz_3d = [
    [#0
        [1,2,3,4,5],#0
        [6,7,8,9,10]#1
        #0,1,2,3,4
    ],
    [#1
        [11,12,13,14],#0
        [15,16,17,18]#1
        #0,1,2,3
    ]
]
#Acceder a un elemento especifico de matriz_3d Ej: [][][]
resul_m3d = matriz_3d[1][1][2]
print(resul_m3d)

#Modificar número 13 por número 133
matriz_3d [1][0][2] = 133
print(matriz_3d)
print(matriz_3d[1][0][2])

#Recorrer matriz con un ciclo for x3:
for f in matriz_3d:
    for c in f:
        for l in f:
            print(l)

