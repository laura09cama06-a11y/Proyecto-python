#archivo para poner las funciones que se van a usar en el menu, para no saturar el codigo del menu
import time
from devspaces import devspace
import devspaces as Ds

def enter_to_continue():
    input("\nPresione Enter para continuar...")

def access_space(username:str):
    print("\033c", end="")
    print("Acceder a un space\n")
    space_id = input("Ingrese el ID del space al que desea acceder: ")
    if not space_id.isdigit():
        print("ID inválido. Por favor, ingrese un número válido.")
        time.sleep(2)
        return None
    return int(space_id)

def show_spaces(username:str):
    print("\033c", end="")
    print("Espacios disponibles\n")
    success, spaces = devspace.get_spaces_by_user(username)
    if success:
        if spaces:
            print("Espacios de {}:".format(username))
            for space in spaces:
                print("- {} (ID: {})".format(space[0], space[1]))
            nombre_space = input("Ingrese el nombre del space al que desea acceder: ")
            return nombre_space
        else:
            print("No tiene espacios registrados, {}.".format(username))
    else:
        print("Error al obtener espacios, {}.".format(username))


def show_space_posts(username: str):
    print("Posts del space\n")
    success,id_space = devspace.get_spaces_by_user(username)
    if success and id_space:
        space_id = id_space[0][1]  # Obtener el ID del primer espacio
        success, posts = devspace.get_posts(space_id, username)
        if success:
            if posts:
                print("Posts del space {}:".format(username))
                for post in posts:
                    print("- {} (ID: {})".format(post[0], post[1]))
                
            else:
                print("No hay posts registrados en este space.")
        
        else:
            print("Error al obtener los posts del space.")
    else:
        print("Error al obtener el ID del space.")
    enter_to_continue()

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
    enter_to_continue()

def show_own_spaces(username:str):
    success, spaces = devspace.get_spaces_by_user(username)
    if success:
        if spaces:
            print("Tus espacios, {}:".format(username))
            for space in spaces:
                print("- {}".format(space[0]))
                enter_to_continue()
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
                enter_to_continue()
        else:
            print("No sigues ningún espacio registrado, {}.".format(username))
            enter_to_continue()
    else:
        print("Error al obtener los espacios que sigues, {}.".format(username)) 

def manage_friend_request(username: str, id_space: int, accept: bool) -> bool:
    """
    Acepta o rechaza una solicitud de seguimiento.
    """
    success = Ds.manage_friend_request(username, id_space, accept)
    return success
def gestionar_solicitudes(username):
    success, followers = Ds.get_followers(username)

    if not success:
        print("Error al obtener solicitudes.")
        input("Presione Enter para continuar...")
        return

    pendientes = [f for f in followers if f[3] is False]

    if not pendientes:
        print("No tienes solicitudes pendientes.")
        input("Presione Enter para continuar...")
        return

    print("\nSolicitudes de seguimiento:\n")

    for i, follower in enumerate(pendientes, start=1):
        follower_username, space_id, space_name, accepted = follower
        print(f"{i}. Usuario: {follower_username} | Space: {space_name}")

    try:
        opcion = int(input("\nSeleccione una solicitud (0 para salir): "))
        if opcion == 0:
            return

        follower_username, space_id, space_name, accepted = pendientes[opcion - 1]

        print("\n1. Aceptar")
        print("2. Rechazar")
        decision = input("Seleccione una opción: ")

        if decision == "1":
            result = Ds.handle_follower(username, space_id, follower_username, True)
        elif decision == "2":
            result = Ds.handle_follower(username, space_id, follower_username, False)
        else:
            print("Opción no válida.")
            return

        print("✅ Operación realizada correctamente." if result else "❌ Error en la operación.")

    except (ValueError, IndexError):
        print("Entrada inválida.")

    input("\nPresione Enter para continuar...")