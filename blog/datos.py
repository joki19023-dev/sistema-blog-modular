"""Módulo de datos: almacena las estructuras base en memoria del blog."""

perfil_autor = {
    "nombre": "Guido van Rossum",
    "redes_sociales": [
        "https://github.com/gvanrossum",
        "https://gist.github.com/gvanrossum",
        "https://gvanrossum.github.io/"
    ]
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {
    "python",
    "desarrollo web",
    "bases de datos",
    "inteligencia artificial",
    "python"
}

posts = [
    {
        "id": 1,
        "titulo": "Introducción a Python",
        "autor": perfil_autor,
        "categoria": "Programación",
        "tags": ["python", "desarrollo web"],
        "estado": estados_post[1]
    },
    {
        "id": 2,
        "titulo": "Estructuras de datos en memoria",
        "autor": perfil_autor,
        "categoria": "Bases de Datos",
        "tags": ["python", "bases de datos"],
        "estado": estados_post[1]
    },
    {
        "id": 3,
        "titulo": "El futuro de la inteligencia artificial con Python",
        "autor": perfil_autor,
        "categoria": "Tecnología",
        "tags": ["python", "inteligencia artificial"],
        "estado": estados_post[0]
    },
    {
        "id": 4,
        "titulo": "",  # Post incompleto de prueba (título vacío y sin clave 'categoria')
        "autor": perfil_autor,
        "tags": ["python"],
        "estado": estados_post[0]
    }
]