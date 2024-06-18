#Manejo de archivos json y csv (separados por coma ',')
import json
import csv

#json/lista de estudiantes

estudiantes = [
    {"nombre": "Mauricio", "Edad": 30, "Notas": [40, 50, 65]},
    {"nombre": "Endy", "Edad": 27, "Notas": [46, 60, 65]},
    {"nombre": "Eduard", "Edad": 33, "Notas": [70, 50, 42]},
    {"nombre": "Campo", "Edad": 27, "Notas": [50, 61, 57]},
]
#crear un archivo json
def guardar_en_json(datos, nombre_archivo):
    with open(nombre_archivo, "w") as archivo_json: #enconding='utf-8', sirve para ver los acentos ensure_ascii=False, 
        json.dump(datos, archivo_json, indent=4) #dump transforma archivo json en lista
        print(f"Datos guardados en {nombre_archivo}")

guardar_en_json(estudiantes, "estudiantes_json.json")

#Crear un csv
def guardar_en_csv(datos, nombre_archivo):
    #abrimos el archivo e modo escritura
    with open(nombre_archivo, "w", newline="") as archivo_csv:
        campos = ['nombre', 'Edad', 'Notas']
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)

        escritor_csv.writeheader()
        #Escribir datos
        for estudiantes in datos:
            #Convertimos datos en una lista separados por comas
            estudiantes['Notas'] = ','.join(map(str,estudiantes['Notas']))#join une
            escritor_csv.writerow(estudiantes)

    print(f"Datos guardados en: {nombre_archivo}")

guardar_en_csv(estudiantes, "estudiantes.csv")


#Leer
def leer_json(nombre_archivo):
    with open(nombre_archivo, "r") as archivo_json:
        datos = json.load(archivo_json)
    return datos

def leer_csv(nombre_archivo):
    datos = []
    with open(nombre_archivo, "r") as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            fila['Notas']=list(map(int, fila['Notas'].split(',')))
            datos.append(fila)
    return datos

#Probar mis fx de lectura

datos_json = leer_json('estudiantes_json.json')
print("Datos json")
print(datos_json)

datos_csv = leer_csv('estudiantes.csv')
print("Datos csv")
print(datos_csv)

#1- Crear 2 funciones con estructuras similares
#2- Crear 2 funciones que creen estos archivos
#3- crear 2 funciones que lean estos archivos
