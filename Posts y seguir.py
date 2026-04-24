import devspaces.devspace as ds
Posts=[{

}]

def crear_Post_nuevo(username: str ):
    print("\033c", end="")
    print("===Crear un nuevo post==\n")
    success, spaces = ds.get_spaces_by_user(username)

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