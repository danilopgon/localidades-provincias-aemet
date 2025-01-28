# Provincias y Municipios para AEMET

Este repositorio contiene archivos JSON actualizados con información sobre las provincias y municipios de España, adaptados específicamente para ser utilizados con la API de la AEMET.

## Características del repositorio

### Inspiración y Créditos

Este repositorio se basa en los datos originales del proyecto [angular-consuming-aemet](https://github.com/ivanalbizu/angular-consuming-aemet), con modificaciones realizadas para mejorar la compatibilidad con la API de la AEMET.

### Cambios realizados

1. **Formato de los IDs de municipios**:

   - Original: `"id":"alegria-dulantzi-id01001"`
   - Actualizado: `"id":"01001"`

2. **Codificación de caracteres**:

   - Original: `"Alegr\u00eda-Dulantzi"`
   - Actualizado: `"Alegría-Dulantzi"`

### Estructura de los datos

Cada archivo JSON incluye la relación entre:

- **Provincias**: Nombre y código de cada provincia.
- **Municipios**: Nombre y código que requiere la AEMET para su API.

### Uso de los datos

Estos datos pueden ser utilizados para facilitar la interacción con la API de la AEMET, especialmente para construir consultas relacionadas con municipios específicos o para mostrar información en interfaces de usuario.

## Estructura del repositorio

- `/provincias.json`: Lista de todas las provincias con su código.
- `/localidades_{codigo_provincia}.json`: Archivos con la lista de localidades para cada provincia. El sufijo `{codigo_provincia}` corresponde al código de la provincia.

## Ejemplo de los datos

### Provincias

```json
[
  {
    "id": "16",
    "name": "Cuenca"
  },
  {
    "id": "02",
    "name": "Albacete"
  }
]
```

### Localidades

Archivo: `localidades_16.json`

```json
[
  {
    "id": "16023",
    "provinceId": "16",
    "name": "Tarancón"
  },
  {
    "id": "16078",
    "provinceId": "16",
    "name": "Cuenca"
  }
]
```

## Contribuciones

Si encuentras errores en los datos o quieres mejorar el repositorio, eres bienvenido a crear un *issue* o enviar un *pull request*.

## Nota legal

El uso de los datos proporcionados por la AEMET está sujeto a su [nota legal](https://www.aemet.es/es/nota_legal). Por favor, consulta esta nota para asegurarte de cumplir con los términos y condiciones establecidos.