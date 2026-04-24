import devspaces.devspace as ds
import time
import Menu as m
Posts=[{

}]

"""Función para crear un nuevo post, solicitando al usuario el título, contenido y tipo de post a crear, y luego utilizando la función create_post de la API de DevSpace para crear el post en el sistema."""
def crear_Post_nuevo(username: str ):
    print("\033c", end="")
    print("===Crear un nuevo post==\n")
    username = input("Ingrese su nombre de usuario: ")
    title = input("Ingrese el título del post: ")   
    content = input("Ingrese el contenido del post: ")
    post_type = input("Ingrese el tipo de post (post/snippet): ")   
    success, data = ds.create_post(7, title, content, post_type)    
    if success:
            print("Post creado exitosamente.")
    else:        
            print("Error al crear el post. Por favor, intente nuevamente.")     

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
