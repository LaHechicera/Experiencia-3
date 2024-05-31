"""
Tuplas: son estructuras de datos parecidas a las listas, pero con algunas diferencias.
- Son inmutables
- Se definen mediante ()
- Son una secuencia de elementos.
"""

#1- definir una tupla
tupla_1 = (1,2,3,4,5)

#2- definir una tupla
tupla_2 = 1,2,3,4,5, "holi"

#3- deninir una tupla
tupla_3 = tuple([1,"chaus" , 333, True])
print(type(tupla_3))

#acceder a datos
print(tupla_3[1])

#rangos dentro de las tuplas
print(tupla_3[1:3]) #en el ultimo se detiene, no cuenta la posicion 3, si no declaro nada al final imprimira toda la tupla

tupla_4 = (33,5,8,33,5,888,45,7,32,8,0,6,3443,6,5,6,3,5,6,5,7,8)

# funciones len, max, min, sum. count, index
#número máximo de mi tupla_4
print(max(tupla_4))

#numero minimo
print(min(tupla_4))

#contar las posiciones de mi tupla 
print(len(tupla_4))

#sumar todos los numeros de mi tupla
print(sum(tupla_4))

#metodos y tuplas Count, Index
#Count: cuenta un elemento especifico
#Cuantos números 5 tiene mi tupla_4
print(tupla_4.count(5))

#posición exacta del número 888
print(tupla_4.index(888))

#desempaquetado de tuplas
tupla_5 = (1,2,3)
a,b,c = tupla_5

print(a)
print(b)
print(c)

#20 minutos aprox :v