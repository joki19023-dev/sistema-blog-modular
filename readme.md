# Sistema de Blog Modular en Python

Sistema interactivo en consola organizado en paquetes y módulos independientes para separar las responsabilidades de datos, lógica de negocio, interfaz de usuario y validaciones.

## Estructura del Proyecto

```text
.
├── blog/
│   ├── __init__.py       # Define a 'blog' como un paquete de Python
│   ├── datos.py          # Diccionario de autor, tupla de estados, set de etiquetas y lista de posts
│   ├── menu.py           # Función mostrar_menu() y manejo de input() con try-except
│   ├── operaciones.py    # Funciones listar_posts(), buscar_por_titulo() y filtrar_por_tag()
│   └── validaciones.py   # Función validar_post() para verificar claves requeridas y tipos de datos
├── main.py               # Punto de entrada principal que importa desde el paquete blog
└── README.md             # Documentación de la arquitectura y guía de ejecución
```

## Requisitos

- Tener instalado **Python 3.x**.

## Cómo Ejecutar el Sistema

1. Cloná el repositorio y ubicáte en la carpeta raíz del proyecto (donde se encuentra `main.py` y la carpeta `blog/`):
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. Ejecutá el archivo principal:
   ```bash
   python main.py
   ```

3. Usá las opciones del menú numérico (del 1 al 5) para:
   - **1**: Listar todas las publicaciones en memoria.
   - **2**: Buscar publicaciones por título (sin distinguir mayúsculas de minúsculas).
   - **3**: Filtrar publicaciones por etiqueta/tag (sin distinguir mayúsculas de minúsculas).
   - **4**: Validar que cada post contenga todas las claves obligatorias, campos completos y el autor como diccionario.
   - **5**: Salir del programa.
