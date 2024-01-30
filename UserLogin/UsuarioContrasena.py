# Se tratará de un programa de registro y login. La consola va a pedir un nombre de usuario y una contraseña.
# Tendrá que distinguir si existe el usuario, y si no existe preguntará para ver si se quiere crear uno nuevo.
# En caso de que se registre, se realizará un hash (encriptado) de la contraseña que quiera meter (doble comprobación)
# y se guardará en un fichero diccionario con los nombres de usuario y las contraseñas encriptadas.
# En caso de login, se comprobará que el usuario y la contraseña son correctos.
import hashlib
import json

# Función para leer el archivo JSON e introducir los datos leidos en un array que devuelve
def leer_json():
    usuarios = {}
    file = open("usuarios.json", "r")
    usuarios = json.load(file)
    return usuarios

# Función para registrar usuarios que necesitra un array de usuarios
def registro(usuarios):
    file = open("usuarios.json", "w")
    json.dump(usuarios, file)


usuarios = leer_json()
nombre_usuario = input("Ingrese un nombre de usuario: ")

# Si el nombre de usuario se encuentra en el array devuelto por la función leer, pedimos contraseña
if nombre_usuario in usuarios:

    while True:
        password = input("Introduzca su contraseña")
        # Encriptamos la contraseña para poder compararla con la que está guardada
        hash_password = hashlib.sha1(password.encode()).hexdigest()
        if usuarios[nombre_usuario] == hash_password:
            # Si coincide iniciamos sesión y cerramos el bucle
            print(f"Bienvenido {nombre_usuario}")
            break
            # Si no coincide volvemos a pedir la contraseña
        else:
            print("Contraseña incorrecta!!")

else:
    opcion = input("Nombre de usuario disponible ¿Quiere registrarse?(s/n)")
    if opcion.lower() == "s":
        while True:
            password = input("Introduzca una contrseña: ")
            password2 = input("Introduzca la contrseña otra vez: ")
            if password == password2:
                # Encriptamos la contaraseña que se ha introducido
                hash_password = hashlib.sha1(password.encode()).hexdigest()
                # Añadimos el nuevo nombre de usuario(clave) y su contraseña(valor) al array de diccionarios
                usuarios[nombre_usuario] = hash_password
                # Le pasamos el array de diccionarios a la función registro para meterlos en el archivo JSON
                registro(usuarios)
                print("Registro realizado con éxito")
                break
            else:
                print("Las contraseñas no coinciden")