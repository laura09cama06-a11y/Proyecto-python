import time
from devspaces.data import follow_space
import devspaces as ds  
"""funcion para optener un spaces por usuario"""
def get_space_by_user(username: str):
    success, spaces = ds.get_spaces_by_user(username)

    if success and spaces:
        #spaces = [[id, nombre,descripcion]]]]
        return spaces[0][0]

    success_space, space = ds.create_space(
        username,
        "General",
        "Space por defecto",
        "public"
    )

    if success_space and space:
        return space["1"]

    print("Error al crear el space:", space)
    return None

"""funcion para crear un nuevo post"""
def crear_Post_nuevo(username: str):
    print("\n=== Crear un nuevo post ===\n")

    space_id = get_space_by_user(username)
    if not space_id:
        print("No se pudo obtener un space.")
        time.sleep(2)
        return

    title = input("Ingrese el título del post: ").strip()
    content = input("Ingrese el contenido del post: ").strip()
    post_type = input("Tipo de post (post / snippet): ").lower().strip()

    if not title or not content:
        print(" El título y el contenido no pueden estar vacíos.")
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
        print(" Post creado exitosamente.")
    else:
        print(" Error al crear el post:", data)

    time.sleep(2)

"""Función para seguir un espacio específico, solicitando al usuario el ID del espacio a seguir y utilizando la función follow_space de la API de DevSpace para seguir el espacio en el sistema."""
def seguir_space_controller(username, space_id):
    success, data = follow_space(username, space_id)
    return success, data

"""Funcion para ver los post de un usuario"""
def ver_posts(space_id: int, username: str):
    print("\n=== Posts del space ===\n")

    success, posts = ds.get_posts(space_id, username)

    if not success or not posts:
        print("No hay publicaciones.")
        time.sleep(2)
        return

    index = 0

    while True:
        post = posts[index]

        print("\033c", end="")
        print(f"{post['title']}\n")

        if post["type"] == "post":
            for line in post["content"].split("\n"):
                print(line)
                time.sleep(0.3)
        else:
            print(post["content"])  # aquí luego puedes colorear keywords

        print("\n[A] anterior | [S] siguiente | [Q] salir")
        cmd = input("> ").lower()

        if cmd == "s" and index < len(posts) - 1:
            index += 1
        elif cmd == "a" and index > 0:
            index -= 1
        elif cmd == "q":
            break

