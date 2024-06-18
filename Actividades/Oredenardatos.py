# Ejercicio 1: Frecuencia de Palabras en un Texto

texto = input("Ingrese un texto: ")

palabras = texto.split()
frecuencia_palabras = {}

for palabra in palabras:
    palabra = palabra.lower()  

for palabra, frecuencia in frecuencia_palabras.items():
    frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1
    print(f"{palabra}: {frecuencia}")


    

print("Frecuencia de palabras:")