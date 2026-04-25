#archivo para poner las funciones que se van a usar en el menu, para no saturar el codigo del menu
import time
from devspaces import devspace
import devspaces as ds


def mostrar_usuarios():
    success,usuarios = devspace.get_users()
    if success:
        print("usuarissios registrados en el sistema:")
        for usuario in usuarios:
            print("- {}".format(usuario[0]))
        opcion = input("¿Desea ver los espacios de un usuario específico? (s/n): ")
        if opcion.lower() == 's':
            show_spaces_by_user()
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

def show_own_spaces(username:str):
    success, spaces = devspace.get_spaces_by_user(username)
    if success:
        if spaces:
            print("Tus espacios, {}:".format(username))
            for space in spaces:
                print("- {}".format(space[0]))
        else:
            print("No tienes espacios registrados, {}.".format(username))
            crear = input("¿Deseas crear un nuevo espacio? (s/n): ")
            if crear.lower() == 's':
                    create_space(username)
            else:
                    print("No se creará un nuevo espacio. Regresando al menú principal.")
                    time.sleep(2)  # Esperar 2 segundos antes de regresar al menú principal
                    print("\033c", end="")
    else:
        print("Error al obtener tus espacios, {}.".format(username))

def create_space(username:str):
    print("\033c", end="")
    print("Crear un nuevo espacio\n")
    nombre_space = input("Ingrese el nombre del espacio: ")
    descripcion = input("Ingrese la descripción del espacio: ")
    visibilidad = input("Ingrese la visibilidad del espacio (públic/private): ")

    success, data = devspace.create_space(username, nombre_space, descripcion,visibilidad)
    if success:
        print("Espacio creado exitosamente. ¡Bienvenido a {}!".format(nombre_space))
    else:
        print("Error al crear el espacio. Por favor, intente nuevamente.")

def get_following_spaces(username):
    print("\033c", end="")
    success, spaces = devspace.get_following_spaces(username)
    if success:
        if spaces:
            print("Espacios que sigues, {}:".format(username))
            for space in spaces:
                print("- {}".format(space[0]))
        else:
            print("No sigues ningún espacio registrado, {}.".format(username))
    else:
        print("Error al obtener los espacios que sigues, {}.".format(username)) 

def get_friend_requests(username):
    print("\033c", end="")
    print(" SOLICITUDES POR SPACE\n")

    success, followers = ds.get_followers(username)

    if not success or not followers:
        print("No tienes solicitudes.")
        input("\nPresione Enter para continuar...")
        return

    spaces = {}

    for follower in followers:
        follower_username, space_id, space_name, accepted = follower

        if space_name not in spaces:
            spaces[space_name] = []

        spaces[space_name].append((follower_username, accepted))

    for space_name, seguidores in spaces.items():
        print(f" Space: {space_name}")
        for usuario, accepted in seguidores:
            estado = " Aceptado" if accepted else "⏳ Pendiente"
            print(f" - {usuario} ({estado})")
        print("-" * 30)

    input("\nPresione Enter para continuar...")