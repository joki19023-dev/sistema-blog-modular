"""Módulo de operaciones: funciones para listar, buscar por título y filtrar por tag."""


def listar_posts(lista):
    """Recorre la lista de posts y formatea la salida en consola."""
    if not lista:
        print("No se encontraron posts para mostrar.")
        return
    for post in lista:
        id_post = post.get("id", "Sin ID")
        titulo = post.get("titulo") or "Sin título"
        autor_info = post.get("autor", {})
        nombre_autor = (
            autor_info.get("nombre", "Autor desconocido")
            if isinstance(autor_info, dict)
            else "Autor inválido"
        )
        estado = post.get("estado", "Sin estado")
        print(f"[{id_post}] Título: {titulo} | Autor: {nombre_autor} | Estado: {estado}")


def buscar_por_titulo(lista, termino):
    """Filtra los posts por título ignorando mayúsculas y minúsculas con .lower()."""
    resultados = []
    termino_limpio = termino.lower()
    for post in lista:
        titulo = post.get("titulo", "")
        if termino_limpio in titulo.lower():
            resultados.append(post)
    listar_posts(resultados)
    return resultados


def filtrar_por_tag(lista, tag):
    """Filtra los posts por tag ignorando mayúsculas y minúsculas con .lower()."""
    resultados = []
    tag_limpio = tag.lower()
    for post in lista:
        tags_post = [t.lower() for t in post.get("tags", [])]
        if tag_limpio in tags_post:
            resultados.append(post)
    listar_posts(resultados)
    return resultados