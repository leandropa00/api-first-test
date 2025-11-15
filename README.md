# API First Example - FastAPI

Este proyecto es un ejemplo de desarrollo **API First** utilizando FastAPI. Demuestra cómo diseñar y desarrollar una API RESTful siguiendo el enfoque API First, donde la especificación de la API (OpenAPI/Swagger) se genera automáticamente a partir del código.

## 🚀 Características

- **API First Development**: La documentación OpenAPI se genera automáticamente
- **Validación de Datos**: Usando Pydantic para validación automática
- **Documentación Interactiva**: Swagger UI y ReDoc incluidos
- **Dockerizado**: Listo para ejecutar con Docker y Docker Compose
- **Estructura Modular**: Código organizado con routers y modelos separados

## 📋 Requisitos Previos

- Docker y Docker Compose instalados
- O Python 3.11+ si prefieres ejecutar sin Docker

## 🏗️ Estructura del Proyecto

```
api-first/
├── app/
│   ├── __init__.py
│   ├── main.py              # Aplicación principal FastAPI
│   ├── models.py            # Modelos Pydantic (contrato de la API)
│   └── routers/
│       ├── __init__.py
│       ├── users.py         # Endpoints de usuarios
│       └── items.py         # Endpoints de items
├── Dockerfile
├── docker-compose.yml
├── Makefile                 # Comandos útiles para Docker
├── requirements.txt
└── README.md
```

## 🐳 Ejecución con Docker

### Opción 1: Makefile (Más fácil)

El proyecto incluye un Makefile con comandos útiles:

```bash
# Ver todos los comandos disponibles
make help

# Construir las imágenes
make build

# Iniciar los contenedores
make up

# Construir e iniciar en un solo comando
make up-build

# Detener y eliminar contenedores
make down

# Reiniciar los contenedores
make restart

# Ver logs
make logs

# Ver logs solo del API
make logs-api

# Ver estado de los contenedores
make ps

# Abrir una shell en el contenedor
make shell

# Limpiar contenedores y volúmenes
make clean
```

### Opción 2: Docker Compose (Directo)

```bash
# Construir y ejecutar el contenedor
docker-compose up --build

# Ejecutar en segundo plano
docker-compose up -d

# Ver logs
docker-compose logs -f

# Detener el contenedor
docker-compose down
```

### Opción 3: Docker directamente

```bash
# Construir la imagen
docker build -t api-first-fastapi .

# Ejecutar el contenedor
docker run -p 8000:8000 api-first-fastapi
```

## 💻 Ejecución Local (sin Docker)

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Linux/Mac:
source venv/bin/activate
# En Windows:
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 📚 Endpoints de la API

Una vez que la aplicación esté ejecutándose, puedes acceder a:

- **API Base**: http://localhost:8000
- **Documentación Swagger UI**: http://localhost:8000/docs
- **Documentación ReDoc**: http://localhost:8000/redoc
- **Especificación OpenAPI JSON**: http://localhost:8000/openapi.json
- **Health Check**: http://localhost:8000/health

### Endpoints de Usuarios (`/api/v1/users`)

- `POST /api/v1/users` - Crear un nuevo usuario
- `GET /api/v1/users` - Obtener todos los usuarios
- `GET /api/v1/users/{user_id}` - Obtener un usuario por ID
- `PUT /api/v1/users/{user_id}` - Actualizar un usuario
- `DELETE /api/v1/users/{user_id}` - Eliminar un usuario

### Endpoints de Items (`/api/v1/items`)

- `POST /api/v1/items?owner_id={id}` - Crear un nuevo item
- `GET /api/v1/items` - Obtener todos los items (con paginación)
- `GET /api/v1/items/{item_id}` - Obtener un item por ID
- `PUT /api/v1/items/{item_id}` - Actualizar un item
- `DELETE /api/v1/items/{item_id}` - Eliminar un item

## 🧪 Ejemplos de Uso

### Crear un usuario

```bash
curl -X POST "http://localhost:8000/api/v1/users" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "usuario@example.com",
    "full_name": "Juan Pérez"
  }'
```

### Obtener todos los usuarios

```bash
curl "http://localhost:8000/api/v1/users"
```

### Crear un item

```bash
curl -X POST "http://localhost:8000/api/v1/items?owner_id=1" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Laptop",
    "description": "Laptop de alta gama",
    "price": 1299.99
  }'
```

## 🎯 Enfoque API First

Este proyecto demuestra el enfoque **API First** de las siguientes maneras:

1. **Modelos Pydantic como Contrato**: Los modelos en `app/models.py` definen el contrato de la API antes de la implementación
2. **Documentación Automática**: FastAPI genera automáticamente la especificación OpenAPI desde el código
3. **Validación Automática**: Pydantic valida automáticamente las solicitudes y respuestas
4. **Type Hints**: El uso de type hints permite mejor autocompletado y validación en tiempo de desarrollo

### Ventajas del Enfoque API First

- ✅ La documentación siempre está actualizada
- ✅ Los clientes pueden generar código desde la especificación OpenAPI
- ✅ Validación automática de datos
- ✅ Mejor experiencia de desarrollo con autocompletado
- ✅ Contrato claro entre frontend y backend

## 🔧 Tecnologías Utilizadas

- **FastAPI**: Framework web moderno y rápido para Python
- **Pydantic**: Validación de datos usando type hints de Python
- **Uvicorn**: Servidor ASGI de alto rendimiento
- **Docker**: Containerización de la aplicación

## 📝 Notas

- Este es un ejemplo educativo. En producción, deberías usar una base de datos real en lugar de almacenamiento en memoria
- Los datos se pierden al reiniciar el contenedor (almacenamiento en memoria)
- Para producción, considera agregar autenticación, logging, y manejo de errores más robusto

## 📄 Licencia

Este proyecto es un ejemplo educativo y está disponible para uso libre.

