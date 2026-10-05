# BiblioTQ Web

Una página web desarrollada con Django para cotizar muebles y estanterías personalizadas. El proyecto fue realizado como trabajo final para la materia de Computación Gráfica en la Facultad de Ingeniería de la Universidad Nacional de Colombia.

## Descripción general

BiblioTQ Web permite a un usuario seleccionar un modelo de estantería, ingresar dimensiones y configuraciones específicas, y registrar una cotización para diferentes tipos de muebles. La aplicación está orientada a una experiencia de venta basada en formularios web, sin una API REST como capa principal.

El proyecto combina:

- Django como framework principal
- Plantillas HTML para la interfaz
- Modelos de datos para guardar cotizaciones y usuarios
- Servicios de base de datos configurados por variable de entorno
- Contenedores Docker para facilitar la ejecución

## Características principales

- Catálogo de tres modelos de estanterías:
  - Modelo 1: dos secciones laterales y repisas ajustables
  - Modelo 2: vertical con repisas y altura personalizable
  - Modelo 3: repisas pequeñas con cajón integrado
- Captura de dimensiones y atributos personalizados del producto
- Registro de usuario por email
- Persistencia de cotizaciones en base de datos
- Flujo de compra/cotización con páginas de éxito y confirmación
- Soporte para despliegue en Render y ejecución local con Docker

## Arquitectura

La aplicación sigue una arquitectura sencilla de Django MVC-like:

- Frontend: plantillas HTML, CSS y archivos estáticos
- Backend: Django Views y rutas URL
- Model layer: modelos de Django para usuarios y cotizaciones
- Persistence: base de datos configurable mediante DATABASE_URL

Diagrama conceptual:

```text
Usuario
  ↓
Navegador
  ↓
Django App (price)
  ├── landing()
  ├── shop()
  ├── success()
  ↓
Models (Cotizacion1, Cotizacion2, Cotizacion3, SimpleUsuario)
  ↓
Base de datos (MySQL/PostgreSQL configurable vía DATABASE_URL)
```

## Estructura del proyecto

```text
BiblioTQ-web/
├── BiblioTQ/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── price/
│   ├── templates/
│   │   ├── landing.html
│   │   ├── shop.html
│   │   ├── success.html
│   │   └── home.html
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static/
│   └── images/
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yaml
├── .gitignore
└── README.md
```

## Stack tecnológico

- Python 3.10
- Django 5.1.5
- HTML, CSS y archivos estáticos
- PyMySQL para integración con MySQL
- dj-database-url para configuración de base de datos
- python-dotenv para variables de entorno
- Docker y Docker Compose

## Modelo de datos

La aplicación define los siguientes modelos principales:

- `SimpleUsuario`
  - `email`: correo electrónico único
- `Cotizacion1`
  - `usuario`
  - `fecha`
  - `alto`
  - `ancho`
  - `fondo`
  - `n_cajones_der`
  - `n_cajones_izq`
  - `status`
- `Cotizacion2`
  - `usuario`
  - `fecha`
  - `alto`
  - `ancho`
  - `fondo`
  - `alturarepisa`
  - `Nrepisas`
  - `puerta`
  - `status`
- `Cotizacion3`
  - `usuario`
  - `fecha`
  - `alto`
  - `ancho`
  - `fondo`
  - `altura_1`
  - `altura_2`
  - `N_repisas_p`
  - `cajon`
  - `status`
- `insumo`
  - información de materiales o insumos asociados a precios

## Endpoints y rutas

Este proyecto no expone una API REST JSON, sino rutas web basadas en vistas Django.

| Ruta | Método | Descripción |
| --- | --- | --- |
| `/` | GET | Página de inicio / landing |
| `/shop/` | GET, POST | Formulario para registrar cotizaciones |
| `/success/` | GET | Página de confirmación de envío |
| `/admin/` | GET | Panel administrativo de Django |

### Flujo principal

1. El usuario entra a `/`
2. Selecciona un modelo de estantería
3. Completa dimensiones y datos opcionales
4. Envía el formulario a `/shop/`
5. Se guarda la cotización en la base de datos
6. El sistema redirige a `/success/`

## Requisitos previos

- Python 3.10+
- pip
- Entorno virtual recomendado (`venv`)
- Base de datos compatible con Django (por ejemplo MySQL)
- Docker (opcional, si se quiere ejecutar por contenedor)

## Instalación y configuración local

### 1) Clonar el repositorio

```bash
git clone https://github.com/dfbello/BiblioTQ-web.git
cd BiblioTQ-web
```

### 2) Crear entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

En Windows:

```powershell
.venv\Scripts\activate
```

### 3) Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4) Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto con contenido similar a:

```env
DATABASE_URL=mysql://usuario:password@localhost:3306/bibliotq
```

También puedes ajustar otros valores según tu entorno de desarrollo.

### 5) Ejecutar migraciones

```bash
python manage.py migrate
```

### 6) Iniciar el servidor

```bash
python manage.py runserver 0.0.0.0:8000
```

Abre en el navegador:

```text
http://localhost:8000/
```

## Ejecución con Docker

El repositorio incluye `Dockerfile` y `docker-compose.yaml` para facilitar la ejecución.

```bash
docker compose up --build
```

Esto levantará la aplicación sobre el puerto `8000`.

## Variables de entorno relevantes

| Variable | Descripción |
| --- | --- |
| `DATABASE_URL` | Cadena de conexión a la base de datos |
| `DEBUG` | Habilita/deshabilita el modo depuración (si se configura) |
| `SECRET_KEY` | Clave secreta de Django |

## Consideraciones de despliegue

El proyecto está configurado para usar una base de datos definida por `DATABASE_URL`, y en la configuración actual también se incluye una referencia a una instancia en Render (`CSRF_TRUSTED_ORIGINS`). Esto hace que el proyecto sea apropiado para despliegue en plataformas como Render, aunque el código principal sigue siendo un proyecto Django estándar.

## Mejoras sugeridas

- Separar lógica de negocio en servicios
- Crear una API REST para consumo externo
- Agregar autenticación de usuario
- Añadir panel de administración para gestionar materiales y precios
- Añadir validaciones más robustas para cotizaciones
- Mejorar la estructura de templates con componentes reutilizables

## Licencia

No se especifica una licencia en el repositorio. Si el proyecto va a reutilizarse o publicarse, se recomienda definir una licencia explícita antes de compartirlo ampliamente.

## Contacto

Proyecto desarrollado por `dfbello`.

---

Si quieres, también puedo dejarte una versión de este README en inglés, o una variante más elegante con badges y una tabla de contenido más visual.
