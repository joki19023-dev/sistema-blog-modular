"""Módulo de validaciones: verifica las reglas de negocio de cada post."""


def validar_post(post):
    """Comprueba la existencia de las claves requeridas, campos no vacíos y autor como diccionario."""
    claves_requeridas = ("id", "titulo", "autor", "categoria", "tags", "estado")
    errores = []

    for clave in claves_requeridas:
        if clave not in post:
            errores.append(f"falta la clave '{clave}'")
        elif not post.get(clave):
            errores.append(f"el campo '{clave}' está vacío")

    if "autor" in post and not isinstance(post.get("autor"), dict):
        errores.append("'autor' debe ser un diccionario")

    id_post = post.get("id", "Desconocido")
    if errores:
        print(f"Post ID {id_post}: Inválido ({', '.join(errores)}).")
        return False

    print(f"Post ID {id_post}: Válido.")
    return True