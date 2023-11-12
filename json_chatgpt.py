import json

# Crear datos en formato Python (un diccionario, en este caso)
data = {
    "nombre": "Ejemplo",
    "edad": 30,
    "ciudad": "Ciudad Ejemplo"
}

# Nombre del archivo en el que deseas guardar los datos en formato JSON
nombre_archivo = "datos.json"

# Abrir el archivo en modo escritura ("w")
with open(nombre_archivo, "w") as archivo:
    # Utilizar json.dump() para escribir los datos en el archivo
    json.dump(data, archivo)

# El archivo "datos.json" ahora contiene los datos en formato JSON
import json

# Nombre del archivo que contiene los datos en formato JSON
nombre_archivo = "datos.json"

# Abrir el archivo en modo lectura ("r")
with open(nombre_archivo, "r") as archivo:
    # Utilizar json.load() para cargar los datos desde el archivo
    data = json.load(archivo)

# Los datos ahora están disponibles en la variable "data" como un diccionario de Python
print(data)
