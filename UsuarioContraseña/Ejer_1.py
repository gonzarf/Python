# Leer el contenido de una carpeta diferenciando entre ficheros y directorios.
import os

path = input("Introduce la ruta del directorio: ")

try:
    contains = os.scandir(path)
    for x in contains:
        if x.is_file():
            print("Es un archivo")
        elif x.is_dir():
            print("Es un directorio")

except NotADirectoryError:
    print("Error. La ruta no es una carpeta.")

