# Creamos un diccionario
diccionario = {
    "marca": "Mercedes",
    "modelo": "a200",
    "precio": 20000
}
# Mostramos el valor para la clave marca
print(diccionario.get("marca"))

# Pedimos al usuario que introduzca la clave que quiere modificar
clave = input(f"¿Que clave desea modificar?(marca, modelo o precio)")

# Modificar una clave inroducida y le pedimos que introduzca el nuevo valor
diccionario.update({clave: input("Introduzca el nuevo valor:")})

# Mostramos el valor modifcado para la clave marca
print(diccionario.get("marca"))
