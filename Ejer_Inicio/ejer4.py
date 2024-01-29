
usuario = input("Introduce una cadena de números separados por comas: ")

lista = usuario.split(',')

for i in range(len(lista)):
    lista[i] = int(lista[i])

print("La lista de numeros es: ", lista)