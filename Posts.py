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
