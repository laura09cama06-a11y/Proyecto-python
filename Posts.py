import time
from devspaces import devspace
import devspaces as ds
"""funcion para optener un spaces por usuario"""
def get_space_by_user(username: str):
    success, spaces = devspace.get_spaces_by_user(username)

    if success and spaces:
        #spaces = [[id, nombre,descripcion]]]]
        return spaces[0][0]

    success_space, space = devspace.create_space(
        username,
        "General",
        "Space por defecto",
        "public"
    )

    if success_space and space:
        return space[1]

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

    success, data = devspace.create_post(
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
    success, data = ds.follow_space(username, space_id)
    return success, data

"""Funcion para ver los post de un usuario"""
def ver_posts(space_id: int, username: str):
    print("\n=== Posts del space ===\n")

    success, posts = ds.get_posts(space_id, username)

    if not success or not posts or not isinstance(posts, list) or len(posts) == 0:
        print("No hay publicaciones.")
        time.sleep(2)
        return

    index = 0

    while True:
        post = posts[index]
        # post es una lista: [id, título, contenido, tipo]
        post_id, post_title, post_content, post_type = post[0], post[1], post[2], post[3]

        print("\033c", end="")
        print(f"{post_title}\n")

        if post_type == "post":
            for line in post_content.split("\n"):
                print(line)
                time.sleep(0.3)
        else:
            print(post_content)  

        print("\n[A] anterior | [S] siguiente | [Q] salir")
        cmd = input("> ").lower()

        if cmd == "s" and index < len(posts) - 1:
            index += 1
        elif cmd == "a" and index > 0:
            index -= 1
        elif cmd == "q":
            break



# Colores ANSI
AZUL = "\033[34m"
AMARILLO = "\033[33m"
RESET = "\033[0m"

KEYWORDS = {
    "def", "if", "else", "elif", "return", "for", "while",
    "break", "continue", "import", "from", "class",
    "try", "except", "True", "False", "None"
}


def mostrar_texto_animado(contenido: str):
    """Muestra texto línea por línea con animación"""
    for linea in contenido.split("\n"):
        print(linea)
        time.sleep(0.3)


def mostrar_snippet(contenido: str):
    """Muestra código resaltando palabras clave"""
    for palabra in contenido.split():
        if palabra in KEYWORDS:
            print(f"{AMARILLO}{palabra}{RESET}", end=" ")
        else:
            print(palabra, end=" ")
    print()


def ver_spaces_de_otro_usuario_interactivo():
    print("\033c", end="")
    otro_usuario = input("Ingrese el nombre del usuario: ").strip()

    if not otro_usuario:
        print("Debe ingresar un nombre de usuario.")
        time.sleep(2)
        return None

    success, spaces = devspace.get_spaces_by_user(otro_usuario)

    if not success or not spaces:
        print("Este usuario no tiene spaces disponibles.")
        time.sleep(2)
        return None

    index = 0
    total = len(spaces)

    while True:
        print("\033c", end="")

        space_id, nombre, descripcion = spaces[index]

        print(f" Usuario: {otro_usuario}")
        print(" SPACE")
        print("-" * 40)
        print(f"Nombre: {nombre}")
        print(f"Descripción: {descripcion}")
        print(f"\nSpace {index + 1} de {total}")

        print("\nOpciones:")
        print("[A] Anterior | [S] Siguiente | [E] Entrar | [Q] Salir")

        opcion = input("> ").lower()

        if opcion == "s" and index < total - 1:
            index += 1
        elif opcion == "a" and index > 0:
            index -= 1
        elif opcion == "e":
            return space_id    
        elif opcion == "q":
            return None
        
def crear_post_interactivo(space_id: int, username: str):
    print("\n=== Crear un nuevo post ===\n")

    title = input("Ingrese el título del post: ").strip()
    content = input("Ingrese el contenido del post: ").strip()
    post_type = input("Tipo de post (post / snippet): ").lower().strip()

    if not title or not content:
        print(" El título y el contenido no pueden estar vacíos.")
        time.sleep(2)
        return
    sucess,data = devspace.create_post(
        space_id,
        title,
        content,
        post_type
    )
    if sucess:
        print(" Post creado exitosamente.")
    else:
        print(" Error al crear el post:", data)
