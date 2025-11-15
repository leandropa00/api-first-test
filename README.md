# Requerimientos Funcionales y No Funcionales

## Análisis del Proyecto

Este documento define los requerimientos funcionales y no funcionales del proyecto **API First Example**, una API REST desarrollada con FastAPI que gestiona usuarios e items, y genera reportes basados en estos datos.

---

## 1. Requerimientos Funcionales

### 1.1. Gestión de Usuarios

#### RF-001: Crear Usuario
- **Descripción**: El sistema debe permitir crear nuevos usuarios con email y nombre completo.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - El email debe ser válido y único en el sistema
  - El nombre completo debe tener entre 1 y 100 caracteres
  - El sistema debe asignar automáticamente un ID único y timestamps de creación
  - Debe retornar el usuario creado con todos sus datos

#### RF-002: Listar Usuarios
- **Descripción**: El sistema debe permitir obtener la lista de todos los usuarios registrados.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - Debe retornar todos los usuarios sin filtros
  - Cada usuario debe incluir: ID, email, nombre completo, fecha de creación y última actualización

#### RF-003: Obtener Usuario por ID
- **Descripción**: El sistema debe permitir obtener la información de un usuario específico por su ID.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - Debe retornar error 404 si el usuario no existe
  - Debe retornar todos los datos del usuario si existe

#### RF-004: Actualizar Usuario
- **Descripción**: El sistema debe permitir actualizar la información de un usuario existente.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - Debe permitir actualizar email y/o nombre completo de forma parcial
  - El nuevo email debe ser válido y único si se proporciona
  - Debe actualizar el timestamp de última modificación
  - Debe retornar error 404 si el usuario no existe

#### RF-005: Eliminar Usuario
- **Descripción**: El sistema debe permitir eliminar un usuario del sistema.
- **Prioridad**: Media
- **Criterios de Aceptación**:
  - Debe retornar error 404 si el usuario no existe
  - Debe eliminar completamente el usuario del sistema
  - Debe retornar código 204 (No Content) al eliminar exitosamente

### 1.2. Gestión de Items

#### RF-006: Crear Item
- **Descripción**: El sistema debe permitir crear nuevos items asociados a un usuario.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - El item debe tener título (1-200 caracteres), descripción opcional (máx. 1000 caracteres) y precio (mayor a 0)
  - Debe estar asociado a un usuario mediante owner_id
  - El sistema debe asignar automáticamente un ID único y timestamps de creación
  - Debe retornar el item creado con todos sus datos

#### RF-007: Listar Items
- **Descripción**: El sistema debe permitir obtener la lista de todos los items con soporte de paginación.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - Debe soportar paginación mediante parámetros skip y limit
  - El límite por defecto debe ser 100 items
  - Cada item debe incluir: ID, título, descripción, precio, owner_id, fecha de creación y última actualización

#### RF-008: Obtener Items por Usuario
- **Descripción**: El sistema debe permitir obtener todos los items pertenecientes a un usuario específico.
- **Prioridad**: Media
- **Criterios de Aceptación**:
  - Debe filtrar items por owner_id
  - Debe soportar paginación mediante parámetros skip y limit
  - Debe retornar lista vacía si el usuario no tiene items

#### RF-009: Obtener Item por ID
- **Descripción**: El sistema debe permitir obtener la información de un item específico por su ID.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - Debe retornar error 404 si el item no existe
  - Debe retornar todos los datos del item si existe

#### RF-010: Actualizar Item
- **Descripción**: El sistema debe permitir actualizar la información de un item existente.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - Debe permitir actualizar título, descripción y/o precio de forma parcial
  - El precio debe ser mayor a 0 si se proporciona
  - Debe actualizar el timestamp de última modificación
  - Debe retornar error 404 si el item no existe

#### RF-011: Eliminar Item
- **Descripción**: El sistema debe permitir eliminar un item del sistema.
- **Prioridad**: Media
- **Criterios de Aceptación**:
  - Debe retornar error 404 si el item no existe
  - Debe eliminar completamente el item del sistema
  - Debe retornar código 204 (No Content) al eliminar exitosamente

### 1.3. Generación de Reportes

#### RF-012: Reporte de Resumen de Usuarios
- **Descripción**: El sistema debe generar un reporte con resumen de todos los usuarios y estadísticas de sus items.
- **Prioridad**: Media
- **Criterios de Aceptación**:
  - Debe incluir el total de usuarios
  - Para cada usuario debe mostrar: total de items, valor total de items, precio promedio de items
  - Debe incluir la lista completa de items de cada usuario

#### RF-013: Reporte de Resumen de Items
- **Descripción**: El sistema debe generar un reporte con resumen de todos los items e información de sus propietarios.
- **Prioridad**: Media
- **Criterios de Aceptación**:
  - Debe incluir estadísticas generales: total de items, valor total, precio promedio, precio mínimo, precio máximo
  - Cada item debe incluir información de su propietario
  - Debe manejar items sin propietario válido

#### RF-014: Reporte Detallado de Usuario
- **Descripción**: El sistema debe generar un reporte detallado de un usuario específico con todos sus items.
- **Prioridad**: Media
- **Criterios de Aceptación**:
  - Debe incluir información completa del usuario
  - Debe incluir todos los items del usuario
  - Debe incluir estadísticas: total de items, valor total, precio promedio, precio mínimo, precio máximo
  - Debe retornar error 404 si el usuario no existe

#### RF-015: Reporte de Visión General del Sistema
- **Descripción**: El sistema debe generar un reporte completo con visión general de todo el sistema.
- **Prioridad**: Baja
- **Criterios de Aceptación**:
  - Debe incluir: total de usuarios, total de items, valor total, precio promedio
  - Debe incluir top 5 usuarios por cantidad de items
  - Debe incluir top 5 usuarios por valor total de items
  - Debe incluir estadísticas de todos los usuarios

#### RF-016: Reporte de Items por Rango de Precio
- **Descripción**: El sistema debe permitir filtrar items por rango de precios.
- **Prioridad**: Baja
- **Criterios de Aceptación**:
  - Debe permitir filtrar por precio mínimo (opcional)
  - Debe permitir filtrar por precio máximo (opcional)
  - Debe retornar items con información de propietario
  - Debe incluir el total de items que cumplen el filtro

### 1.4. Funcionalidades Generales

#### RF-017: Health Check
- **Descripción**: El sistema debe proveer un endpoint de health check para monitoreo.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - Debe retornar el estado de salud de la API
  - Debe ser accesible sin autenticación

#### RF-018: Documentación Automática
- **Descripción**: El sistema debe generar automáticamente documentación OpenAPI/Swagger.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - Debe estar disponible en `/docs` (Swagger UI)
  - Debe estar disponible en `/redoc` (ReDoc)
  - Debe estar disponible en `/openapi.json` (OpenAPI JSON)
  - La documentación debe estar siempre actualizada con el código

#### RF-019: Validación de Datos
- **Descripción**: El sistema debe validar automáticamente todos los datos de entrada.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - Debe validar formato de email
  - Debe validar longitudes de strings
  - Debe validar rangos numéricos (precio > 0)
  - Debe retornar errores descriptivos en caso de validación fallida

#### RF-020: Manejo de Errores
- **Descripción**: El sistema debe manejar errores de forma consistente.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - Debe retornar código 404 para recursos no encontrados
  - Debe retornar código 400 para datos inválidos
  - Debe retornar mensajes de error descriptivos
  - Debe usar códigos de estado HTTP apropiados

---

## 2. Requerimientos No Funcionales

### 2.1. Rendimiento

#### RNF-001: Tiempo de Respuesta
- **Descripción**: Los endpoints deben responder en un tiempo razonable.
- **Prioridad**: Media
- **Criterios de Aceptación**:
  - Endpoints de lectura (GET) deben responder en menos de 500ms
  - Endpoints de escritura (POST, PUT, DELETE) deben responder en menos de 1s
  - Endpoints de reportes pueden tomar hasta 2s

#### RNF-002: Escalabilidad
- **Descripción**: La arquitectura debe permitir escalar horizontalmente.
- **Prioridad**: Baja (actualmente no implementado)
- **Criterios de Aceptación**:
  - La aplicación debe ser stateless
  - Debe ser compatible con balanceadores de carga

### 2.2. Disponibilidad y Confiabilidad

#### RNF-003: Disponibilidad
- **Descripción**: El sistema debe estar disponible para su uso.
- **Prioridad**: Media
- **Criterios de Aceptación**:
  - Debe incluir health check endpoint para monitoreo
  - Debe manejar errores sin caer completamente

#### RNF-004: Persistencia de Datos
- **Descripción**: Los datos deben persistir entre reinicios (requerimiento futuro).
- **Prioridad**: Baja (actualmente en memoria)
- **Criterios de Aceptación**:
  - Actualmente los datos se pierden al reiniciar (almacenamiento en memoria)
  - En producción se requiere base de datos persistente

### 2.3. Seguridad

#### RNF-005: CORS
- **Descripción**: El sistema debe permitir acceso desde diferentes orígenes.
- **Prioridad**: Media
- **Criterios de Aceptación**:
  - Actualmente permite todos los orígenes (*)
  - En producción debe configurarse para orígenes específicos

#### RNF-006: Autenticación y Autorización
- **Descripción**: El sistema debe implementar autenticación y autorización (requerimiento futuro).
- **Prioridad**: Baja (no implementado actualmente)
- **Criterios de Aceptación**:
  - Actualmente no hay autenticación
  - En producción se requiere implementar autenticación (JWT, OAuth2, etc.)

#### RNF-007: Validación de Entrada
- **Descripción**: El sistema debe validar y sanitizar todas las entradas.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - Debe usar Pydantic para validación automática
  - Debe prevenir inyección de datos maliciosos
  - Debe validar tipos de datos y formatos

### 2.4. Mantenibilidad

#### RNF-008: Código Modular
- **Descripción**: El código debe estar organizado de forma modular.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - Debe usar routers separados por dominio (users, items, reports)
  - Debe separar modelos de lógica de negocio
  - Debe seguir principios SOLID

#### RNF-009: Documentación de Código
- **Descripción**: El código debe estar documentado.
- **Prioridad**: Media
- **Criterios de Aceptación**:
  - Debe incluir docstrings en funciones y clases
- **Estado**: Parcialmente implementado

#### RNF-010: Type Hints
- **Descripción**: El código debe usar type hints de Python.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - Todas las funciones deben tener type hints
  - Los modelos deben usar Pydantic con validación de tipos

### 2.5. Despliegue y Operaciones

#### RNF-011: Containerización
- **Descripción**: El sistema debe estar containerizado con Docker.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - Debe incluir Dockerfile
  - Debe incluir docker-compose.yml
  - Debe poder ejecutarse con un solo comando

#### RNF-012: Health Check en Docker
- **Descripción**: El contenedor debe incluir health check.
- **Prioridad**: Media
- **Criterios de Aceptación**:
  - Debe configurarse health check en docker-compose.yml
  - Debe verificar que la API esté respondiendo

#### RNF-013: Hot Reload en Desarrollo
- **Descripción**: El sistema debe soportar hot reload durante desarrollo.
- **Prioridad**: Media
- **Criterios de Aceptación**:
  - Debe usar volúmenes en docker-compose para desarrollo
  - Debe recargar automáticamente al cambiar código

### 2.6. Estándares y Convenciones

#### RNF-014: API First Approach
- **Descripción**: El proyecto debe seguir el enfoque API First.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - Los modelos Pydantic definen el contrato de la API
  - La documentación OpenAPI se genera automáticamente
  - La validación es automática basada en los modelos

#### RNF-015: Versionado de API
- **Descripción**: La API debe estar versionada.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - Todos los endpoints deben estar bajo `/api/v1/`
  - Debe permitir versionado futuro sin romper compatibilidad

#### RNF-016: Estándares REST
- **Descripción**: La API debe seguir estándares REST.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - Debe usar métodos HTTP apropiados (GET, POST, PUT, DELETE)
  - Debe usar códigos de estado HTTP correctos
  - Debe usar nombres de recursos en plural
  - Debe usar estructura de URLs RESTful

### 2.7. Compatibilidad

#### RNF-017: Versión de Python
- **Descripción**: El sistema debe usar Python 3.11+.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - Dockerfile debe usar Python 3.11
  - Debe ser compatible con características modernas de Python

#### RNF-018: Compatibilidad de Dependencias
- **Descripción**: Las dependencias deben estar especificadas y ser compatibles.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - Debe incluir requirements.txt con versiones específicas
  - Las versiones deben ser compatibles entre sí

### 2.8. Usabilidad

#### RNF-019: Documentación Interactiva
- **Descripción**: La API debe proveer documentación interactiva.
- **Prioridad**: Alta
- **Criterios de Aceptación**:
  - Debe incluir Swagger UI para probar endpoints
  - Debe incluir ReDoc para documentación alternativa
  - Debe ser accesible sin configuración adicional

#### RNF-020: Mensajes de Error Claros
- **Descripción**: Los mensajes de error deben ser claros y descriptivos.
- **Prioridad**: Media
- **Criterios de Aceptación**:
  - Debe incluir mensajes de error en español/inglés según corresponda
  - Debe indicar qué campo causó el error
  - Debe sugerir cómo corregir el error

---

## 3. Requerimientos Técnicos Actuales

### 3.1. Stack Tecnológico
- **Framework**: FastAPI 0.104.1
- **Servidor ASGI**: Uvicorn 0.24.0
- **Validación**: Pydantic 2.5.0
- **Lenguaje**: Python 3.11+
- **Containerización**: Docker y Docker Compose

### 3.2. Almacenamiento Actual
- **Tipo**: En memoria (diccionarios Python)
- **Persistencia**: No (datos se pierden al reiniciar)
- **Limitación**: No escalable para producción

### 3.3. Arquitectura
- **Patrón**: API REST
- **Enfoque**: API First
- **Estructura**: Modular con routers separados
- **CORS**: Habilitado para todos los orígenes

---

## 4. Requerimientos Futuros (No Implementados)

### 4.1. Base de Datos
- Implementar base de datos persistente (PostgreSQL, MySQL, etc.)
- Implementar ORM (SQLAlchemy, Tortoise ORM, etc.)
- Implementar migraciones de base de datos

### 4.2. Autenticación y Autorización
- Implementar autenticación JWT
- Implementar roles y permisos
- Implementar OAuth2

### 4.3. Testing
- Implementar tests unitarios
- Implementar tests de integración
- Implementar tests de carga

### 4.4. Logging y Monitoreo
- Implementar logging estructurado
- Implementar métricas (Prometheus)
- Implementar tracing distribuido

### 4.5. CI/CD
- Implementar pipeline de CI/CD
- Implementar despliegue automático
- Implementar tests automatizados

---

## 5. Priorización de Requerimientos

### Prioridad Alta
- RF-001 a RF-011: Gestión básica de usuarios e items
- RF-017: Health check
- RF-018: Documentación automática
- RF-019: Validación de datos
- RF-020: Manejo de errores
- RNF-007: Validación de entrada
- RNF-008: Código modular
- RNF-010: Type hints
- RNF-011: Containerización
- RNF-014: API First approach
- RNF-015: Versionado de API
- RNF-016: Estándares REST

### Prioridad Media
- RF-012 a RF-016: Reportes
- RNF-001: Tiempo de respuesta
- RNF-003: Disponibilidad
- RNF-005: CORS
- RNF-009: Documentación de código
- RNF-012: Health check en Docker
- RNF-013: Hot reload
- RNF-020: Mensajes de error claros

### Prioridad Baja
- RNF-002: Escalabilidad
- RNF-004: Persistencia de datos
- RNF-006: Autenticación y autorización
- Todos los requerimientos futuros (Sección 4)
