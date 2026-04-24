#archivo para poner las funciones que se van a usar en el menu, para no saturar el codigo del menu
import time
from devspaces import devspace

def mostrar_usuarios():
    success,usuarios = devspace.get_users()
    if success:
        print("usuarissios registrados en el sistema:")
        for usuario in usuarios:
            print("- {}".format(usuario[0]))
    else:
        print("Error al obtener los usuarios registrados en el sistema.")

def show_spaces_by_user():
    username = input("Ingrese el nombre de usuario para mostrar sus espacios: ")
    success, spaces = devspace.get_spaces_by_user(username)
    if success:
        if spaces:
            print("Espacios de {}:".format(username))
            for space in spaces:
                print("- {}".format(space[0]))
        else:
            print("El usuario {} no tiene espacios registrados.".format(username))
    else:
        print("Error al obtener los espacios del usuario {}.".format(username))


show_spaces_by_user()
