"""Punto de entrada principal del sistema modular de Blog."""

from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post


if __name__ == "__main__":
    while True:
        opcion_elegida = mostrar_menu()

        if opcion_elegida == 1:
            listar_posts(posts)

        elif opcion_elegida == 2:
            termino_busqueda = input("Ingresá el término de búsqueda: ")
            buscar_por_titulo(posts, termino_busqueda)

        elif opcion_elegida == 3:
            tag_busqueda = input("Ingresá el tag a filtrar: ")
            filtrar_por_tag(posts, tag_busqueda)

        elif opcion_elegida == 4:
            for post in posts:
                validar_post(post)

        elif opcion_elegida == 5:
            print("¡Gracias por usar el sistema del blog! ¡Hasta pronto!")
            break

        elif opcion_elegida != -1:
            print("Opción fuera de rango. Elegí un número entre 1 y 5.")