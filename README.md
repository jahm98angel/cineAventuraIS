# cineAventura
# Cine Aventura

Cine Aventura es una plataforma web de películas de aventura desarrollada con Django, que permite a los usuarios explorar, calificar, reseñar y disfrutar de contenido cinematográfico en una comunidad interactiva.

## Tabla de Contenidos

- [Características](#características)
- [Tecnologías](#tecnologías)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Funcionalidades Principales](#funcionalidades-principales)
- [Licencia](#licencia)

##  Características

-  Catálogo de Películas: Exploración completa de películas de aventura
-  Sistema de Calificaciones: Califica películas del 1 al 10
-  Reseñas: Escribe y lee reseñas de otros usuarios
-  Mensajería: Sistema de chat privado entre usuarios
-  Social Hub: Conecta con otros cinéfilos
-  Watch Parties: Organiza eventos para ver películas en grupo
-  Recomendaciones: Sistema de recomendaciones personalizado
-  Favoritos: Guarda tus películas favoritas
-  Notificaciones: Sistema de notificaciones en tiempo real
-  Autenticación: Registro y login de usuarios

##  Tecnologías

- Backend: Django 5.1.3
- Frontend: HTML5, CSS3, JavaScript
- Base de Datos: SQLite (desarrollo)
- Estilos: CSS personalizado con diseño responsivo
- Fuentes: Google Fonts (Poppins)

##  Requisitos Previos

- Python 3.12+
- Anaconda o Miniconda
- Git
- Navegador web

##  Instalación

### 1. Clonar el Repositorio
```bash
git clone https://github.com/jahm98angel/cineAventuraIS.git
```

### 2. Navegar a la Carpeta del Proyecto
```bash
cd "C:\Users\TU_USUARIO\Downloads\cineAventuraIS"
cd cineAventura
```

### 3. Cambiar a la Rama Principal
```bash
git checkout main
```

### 4. Crear el Entorno Virtual (Anaconda)

Abre Anaconda Prompt y ejecuta:
```bash
# Asegúrate de estar en la carpeta principal del proyecto
cd "C:\Users\TU_USUARIO\Downloads\cineAventuraIS\cineAventura"

# Crear entorno virtual
conda create --name cine python=3.12

# Activar entorno virtual
conda activate cine
```

## Configuración

### 1. Crear Archivo `.env`

En la carpeta principal del proyecto (donde está `manage.py`), crea un archivo llamado `.env` con el siguiente contenido:
```env
SECRET_KEY='django-insecure-aka-films-2024-change-in-production'
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 2. Instalar Dependencias

Con el entorno virtual activado:
```bash
pip install -r requirements.txt
pip install requests
```

### 3. Configurar Base de Datos
```bash
# Crear base de datos y aplicar migraciones
python manage.py migrate

# Cargar datos iniciales de películas
python manage.py loaddata peliculas/fixtures/initial_data.json
```

##  Uso

### Iniciar el Servidor
```bash
python manage.py runserver
```

### Acceder a la Aplicación

Abre tu navegador y visita:
```
http://127.0.0.1:8000/
```

### Crear un Usuario

1. Haz clic en "Registrarse" en la barra de navegación
2. Completa el formulario con tus datos
3. Acepta los términos y condiciones
4. ¡Listo! Ya puedes explorar Cine Aventura

##  Estructura del Proyecto
```
cineAventura/
├── cineAventura/          # Configuración principal del proyecto
│   ├── settings.py        # Configuración de Django
│   ├── urls.py           # URLs principales
│   └── wsgi.py           # Configuración WSGI
│
├── peliculas/            # Aplicación principal
│   ├── static/           # Archivos estáticos
│   │   └── peliculas/
│   │       ├── css/      # Hojas de estilo
│   │       └── img/      # Imágenes y logos
│   │
│   ├── templates/        # Plantillas HTML
│   │   └── peliculas/
│   │       ├── base.html              # Plantilla base
│   │       ├── index.html             # Página de inicio
│   │       ├── detalle.html           # Detalle de película
│   │       ├── social_hub.html        # Hub social
│   │       ├── mensajeria/            # Templates de mensajería
│   │       └── watch_parties/         # Templates de watch parties
│   │
│   ├── fixtures/         # Datos iniciales
│   ├── migrations/       # Migraciones de base de datos
│   ├── models.py        # Modelos de datos
│   ├── views.py         # Vistas
│   ├── urls.py          # URLs de la aplicación
│   └── forms.py         # Formularios
│
├── manage.py            # Script de gestión de Django
├── requirements.txt     # Dependencias del proyecto
├── .env                # Variables de entorno (crear manualmente)
└── db.sqlite3          # Base de datos SQLite
```

##  Funcionalidades Principales

###  Exploración de Películas

- Catálogo completo con búsqueda y filtros
- Carrusel destacado en la página principal
- Búsqueda por género y filtros avanzados
- Información detallada de cada película

###  Sistema de Reseñas

- Calificación del 1 al 10
- Escribir reseñas con título y contenido
- Ver reseñas de otros usuarios
- Sistema de utilidad de reseñas

###  Sistema Social

- Chat privado entre usuarios
- Social Hub para descubrir usuarios
- Perfiles de usuario públicos
- Sistema de notificaciones

###  Watch Parties

- Crear eventos para ver películas
- Invitar usuarios con código único
- Chat grupal en tiempo real
- Gestión de participantes

###  Recomendaciones

- Algoritmo personalizado basado en:
  - Películas favoritas
  - Calificaciones previas
  - Géneros preferidos
  - Actividad de usuarios similares

##  Licencia

Este proyecto está bajo la licencia Creative Commons BY-NC-SA 4.0.

Todo el contenido generado por los usuarios está bajo esta misma licencia.

📄 [Ver términos y condiciones completos](https://creativecommons.org/licenses/by-nc-sa/4.0/)



## Contribuciones

Este proyecto fue desarrollado como parte del curso de Ingeniería de Software.

### Desarrolladores

- Equipo Cine Aventura - 

1. García Gómez Luis Enrique
2. Hernández Morales José Angel
3. Rosas Lira Pablo Elías
4. Sánchez Cruz Norma Selene
5. Súarez Ortíz Joshua Daniel



**¡Disfruta explorando Cine Aventura! 🎬🍿**