import devspaces.devspace as ds
import time

def obtener_o_crear_space(username: str):
    success, spaces = ds.get_spaces_by_user(username)

    if success and spaces and len(spaces[0]) > 0:
        return spaces[0][0]["id"]

    success_space, space = ds.create_space(
        username,
        "General",
        "Space por defecto",
        "public"
    )

    if success_space and space:
        return space["id"]

    print("Error al crear el space:", space)
    return None


def crear_Post_nuevo(username: str):
    print("\n=== Crear un nuevo post ===\n")

    space_id = obtener_o_crear_space(username)
    if not space_id:
        return

    title = input("Ingrese el título del post: ").strip()
    content = input("Ingrese el contenido del post: ").strip()
    post_type = input("Tipo de post (post / snippet): ").lower().strip()

    if not title or not content:
        print("El título y el contenido no pueden estar vacíos.")
        time.sleep(2)
        return

    if post_type not in ("post", "snippet"):
        post_type = "post"

    success, data = ds.create_post(
        space_id,
        title,
        content,
        post_type
    )

    if success:
        print("Post creado exitosamente.")
    else:
        print("Error al crear el post:", data)

    time.sleep(2)

"""Función para seguir un espacio específico, solicitando al usuario el ID del espacio a seguir y utilizando la función follow_space de la API de DevSpace para seguir el espacio en el sistema."""
def seguir_space(username: str):
    try:
        space_id = int(input("ID del space a seguir: "))
    except:
        print("ID inválido")
        return

    success, data = ds.follow_space(username, space_id)

    if success:
        print(" Ahora sigues este space")
    else:
        print(" Error:", data)
        pass

"""Funcion para ver los post de un usuario"""
def ver_posts():
    print("\033c", end="")
    print("📄 Posts disponibles:\n")

    try:
        with open("posts.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            print(contenido if contenido else "No hay posts aún.")
    except FileNotFoundError:
        print("No hay posts aún.")

    input("\nPresione Enter para volver...")
