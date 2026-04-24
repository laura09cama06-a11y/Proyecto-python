import devspaces.devspace as ds
import time

def crear_Post_nuevo(username: str):
    print("\033c", end="")
    print("=== Crear un nuevo post ===\n")

    # 1️ Obtener spaces del usuario
    success, spaces = ds.get_spaces_by_user(username)

    if not success or not spaces:
        print(" No tienes spaces disponibles para publicar.")
        time.sleep(2)
        return

    # 2️⃣ Mostrar spaces disponibles
    print("Seleccione el Space donde desea publicar:\n")
    for space in spaces:
        print(f"{space['id']} - {space['name']}")

    # 3️⃣ Seleccionar space
    try:
        space_id = int(input("\nIngrese el ID del Space: "))
    except ValueError:
        print(" ID inválido.")
        time.sleep(2)
        return

    # 4️⃣ Datos del post
    title = input("\nIngrese el título del post: ").strip()
    description = input("Ingrese el contenido del post: ").strip()
    visualization = input("Tipo de post (public / private): ").lower().strip()

    if not title or not description:
        print(" El título y contenido no pueden estar vacíos.")
        time.sleep(2)
        return

    if visualization not in ("public", "private"):
        visualization = "public"

    # ✅ 5️⃣ CREAR POST (ESTA ES LA PARTE CORREGIDA)
    success, data = ds.create_post(
        space_id,
        title,
        description,
        visualization
    )
    if success:
        print(" Post creado exitosamente.")   
    else:
        print(" Error al crear el post:", data) 
    time.sleep(2)
    print("\033c", end="")
   


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
