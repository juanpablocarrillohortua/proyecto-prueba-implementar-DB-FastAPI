# Ejemplo de integracion de SQLModel y FastAPI

## Descripción del proyecto

Este proyecto es un breve ejemplo del despliegue de una web que recopila datos basándose en la conexión de una base de datos MySQL, alojada en Aiven, y una API construida con FastAPI. La web fue desplegada utilizando el servicio gratuito de Render.

## Objetivos

### Objetivo general

Realizar un proyecto simple que permita mostrar, de manera breve, la creación y conexión de una web sencilla a una base de datos alojada en la nube.
---
## Autor

- **Juan Pablo Carrillo Hortua**  

---

## Estructura del repositorio
```text
proyecto-prueba-implementar-DB-FastAPI/
├── README.md              # Presentación del proyecto
├── .gitignore             # Archivos y carpetas a ignorar
├── engine.py              # Gestiona la conexión a la base de datos
├── main.py                # Aloja la lógica de la API y autorizaciones de URLs
├── models_database.py     # Creación de la estructura de la base de datos
├── public/                # Aloja el frontend
└── requirements.txt       # Librerías y dependencias del proyecto
```
---
## Tecnologías Utilizadas

El proyecto se desarrolló utilizando un stack moderno enfocado en el rendimiento y la facilidad de despliegue:

* **Lenguaje de programación:** [Python 3.14.2](https://www.python.org/)
* **Framework Web (Backend):** [FastAPI](https://fastapi.tiangolo.com/) para la creación de la API REST.
* **Manejo de Base de Datos (ORM):** [SQLModel](https://sqlmodel.tiangolo.com/) (basado en SQLAlchemy y Pydantic).
* **Motor de Base de Datos:** [MySQL](https://www.mysql.com/)
* **Infraestructura de Base de Datos (Cloud):** [Aiven](https://aiven.io/) (Hosting de base de datos administrada).
* **Servidor ASGI:** [Uvicorn](https://www.uvicorn.org/) para la ejecución local y en producción.
* **Despliegue (Hosting):** [Render](https://render.com/) para el alojamiento del servicio web y el frontend.

---
