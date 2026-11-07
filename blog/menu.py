"""Módulo de interfaz: muestra el menú principal y gestiona la entrada del usuario."""


def mostrar_menu():
    """Muestra las opciones en pantalla y captura la opción con manejo de errores."""
    print("\n--- MENÚ DEL BLOG ---")
    print("1. Listar todos los posts")
    print("2. Buscar posts por título")
    print("3. Filtrar posts por tag")
    print("4. Validar posts")
    print("5. Salir")
    try:
        opcion = int(input("Seleccioná una opción (1-5): "))
        return opcion
    except ValueError:
        print("Error: Debés ingresar un número válido.")
        return -1