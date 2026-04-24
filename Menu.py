import time
import devspaces.devspace as Ds

def menu_usuario():
    """Establecer un menu para el usuario ingresado, con opcciones para seguir a otros usuarios, ver publicaciones,ver sus publicaciones  y cerrar sesion  """
    print("\033c", end="")
    print("\033[34m!Bienvenido al sistema de DevSpace {nombre_usuario}¡\033[0m\n")
    while True:
        print("\033[34mseleccione la accion que desea realizar: \033[0m")
        print("1-ver Spaces\n" 
        "2-Ver mis spaces\n" 
        "3-Ver Spaces seguidos\n"
        "4-Solicitudes de amistad\n"
        "5-Cerrar sesión\n")
        try:
            respuesta=int(input("ingrese el numero de la opción deseada: "))
            if respuesta==1:
                pass
            elif respuesta==2:
                pass
            elif respuesta==3:
                pass
            elif respuesta==4:
                pass    
            elif respuesta==5:
                break
        except ValueError:
            print("\033c", end="")
            print("Opción no válida. Por favor, seleccione una opción válida.")
            time.sleep(2)  # Esperar 2 segundos antes de salir para que el usuario pueda leer el mensaje


def menu_ingresar_usuario()->bool:
    """Establecer el menú de opciones para el ingreso de un usuario existente en el sistema de DevSpace
    """
    print("\033c", end="")
    print ("Ingresar al sistema\n")
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    success, data = Ds.login(nombre_usuario, contrasena)
    if success:
        print("Ingreso exitoso. Bienvenido, {}.".format(nombre_usuario))
        # Aquí puedes agregar la lógica para mostrar el menú principal del sistema después del ingreso exitoso
        menu_usuario()
        return True
    else:        
        print("Error al ingresar. Por favor, verifique su nombre de usuario y contraseña e intente nuevamente.") 
    time.sleep(2)  # Esperar 2 segundos antes de regresar al menú principal
    return False

def menu_crear_cuenta_usuario():
    """Establecer el menú de opciones para la creación de un nuevo usuario en el sistema de DevSpace
    """
    print("\033c", end="")
    print ("Crear un nuevo usuario\n")
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    correo_electronico = input("Ingrese su correo electrónico: ")
    contrasena = input("Ingrese su contraseña: ")

    success, data = Ds.create_user(nombre_usuario, correo_electronico, contrasena)
    if success:
        print("Usuario creado exitosamente.")
    else:        
        print("Error al crear el usuario. Por favor, intente nuevamente.") 
    time.sleep(2)  # Esperar 2 segundos antes de regresar al menú principal

def menu_principal():
    while True:
        """Establecer el menú de opciones principales del sistema en terminal, ingreso y creación de usuario
        """
        print("\033c", end="")
        print ("Bienvenido al sistema de DevSpace\n")
        print ("Seleccione una opción:")
        print ("1. Crear un nuevo usuario")
        print ("2. Ingresar al sistema")
        print ("3. Salir")

        respuesta_usuario = input("Ingrese el número de la opción deseada: ")   
        if respuesta_usuario == "1":
            menu_crear_cuenta_usuario()
        elif respuesta_usuario == "2":
            if menu_ingresar_usuario():
                print("\033c", end="")
                print("Bienvenido al sistema de DevSpace")
            else:
                print("\033c", end="")
                print("Usuario no válido. Por favor, intente nuevamente.")
            # Aquí puedes agregar la lógica para ingresar al sistema
        elif respuesta_usuario == "3":
            ##limpiamos la terminal antes de salir
            print("\033c", end="")
            print("Gracias por usar DevSpace. ¡Hasta luego!")
            time.sleep(2)  # Esperar 2 segundos antes de salir para que el usuario pueda leer el mensaje
            print("\033c", end="")
            break
        else:
            print("\033c", end="")

            print("Opción no válida. Por favor, seleccione una opción válida.")
            time.sleep(2)  # Esperar 2 segundos antes de salir para que el usuario pueda leer el mensaje
