# Se tratará de un programa de registro y login. La consola va a pedir un nombre de usuario y una contraseña.
# Tendrá que distinguir si existe el usuario, y si no existe preguntará para ver si se quiere crear uno nuevo.
# En caso de que se registre, se realizará un hash (encriptado) de la contraseña que quiera meter (doble comprobación)
# y se guardará en un fichero diccionario con los nombres de usuario y las contraseñas encriptadas.
# En caso de login, se comprobará que el usuario y la contraseña son correctos.
import json

# Añadimos un objeto más a la lista
#diccionario_usuarios.append({"user": "pedro", "password": "1234"})

# Recogemos un objeto de la lista y despues buscamos por clave
#print(diccionario_usuarios.__getitem__(1).get("user"))
diccionario_usuario = {
    "usuario": "",
    "password": 0000
}

# Abrimos el archivo en modo lectura para poder acceder a los datos más adelante
file = open("usuarios.json", "r")
datos_json = json.load(file)

user = input("Introduzca el nombre de usuario: ")
for data in datos_json:
    if data['usuario'] == user:
        password = input("Introduzca su contraseña: ")

    else:
        password = input("Intruce una contraseña")


diccionario_usuario.update({"usuario": user, "password": password})
json.dump(diccionario_usuario, file)
file.close()

file = open("usuarios.json")


print(datos['usuario'])

