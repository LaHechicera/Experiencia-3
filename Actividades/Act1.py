"1)	Escriba un programa que permita almacenar 3 nombres solicitados por pantalla en una lista, luego el sistema deberá mostrar el nombre que tenga mayor cantidad de caracteres en un mensaje de salida por pantalla."

print("----Escriba los 3 nombres de alumnos en su grupo----")
print(" ")
nom1 = input("Primer nombre: ")
nom2 = input("Segundo nombre: ")
nom3 = input("Tercer nombre: ")

lista_nombres = [nom1, nom2, nom3]

if len(nom1) > len(nom2) and len(nom1) > len(nom3):
    print(f"El nombre con más caracteres es {nom1}")
elif len(nom2) > len(nom1) and len(nom2) > len(nom3):
    print(f"El nombre con más caracteres es {nom2}")
elif len(nom3) > len(nom2) and len(nom3) > len(nom1):
    print(f"El nombre con más caracteres es {nom3}")

nombres = []
for i in range(3):
    nombres.append(input(f'Introduce el nombre número {i+1}: '))

# Encontrar el nombre con mayor cantidad de caracteres
nombre_largo = max(nombres, key=len)

# Mostrar el resultado
print(f'El nombre con mayor cantidad de caracteres es: **{nombre_largo}**')
