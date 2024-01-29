path = input("Introduce la ruta del archivo: ")

try:

    file = open(path)
    print(file.read())

except FileNotFoundError:
    print("El archivo no existe")