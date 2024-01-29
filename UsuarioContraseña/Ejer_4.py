# Con a escribimos en el archivo sin sobreescribir el contenido anterior

opcion = input("Desea añadir texto (a) o sobreescribir (w): ")

file = open("hola.txt", opcion)
file.write(input("¿Qué desea escribir?: "))