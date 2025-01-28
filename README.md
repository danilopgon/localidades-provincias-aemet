# Provincias y Municipios para la API de AEMET

Este repositorio contiene archivos JSON actualizados con información sobre las provincias y municipios de España, adaptados específicamente para ser utilizados con la API de la AEMET.

## Características del repositorio

### Inspiración y Créditos

Este repositorio se basa en los datos originales del proyecto [angular-consuming-aemet](https://github.com/ivanalbizu/angular-consuming-aemet), con modificaciones realizadas para mejorar la compatibilidad con la API y facilitar la inserción de los datos mediante SQL.

### Cambios realizados

1. **Formato de los IDs de municipios**:

   - Original: `"id":"alegria-dulantzi-id01001"`
   - Actualizado: `"id":"01001"`

2. **Codificación de caracteres**:

   - Original: `"Alegr\u00eda-Dulantzi"`
   - Actualizado: `"Alegría-Dulantzi"`

3. **Organización en carpetas**:

   - Los datos JSON ahora se encuentran en la carpeta `/data`.
   - Scripts de Python en la carpeta `/scripts` generan consultas SQL para usar los JSON y rellenar tablas en bases de datos.

### Estructura de los datos

Cada archivo JSON incluye la relación entre:

- **Provincias**: Nombre y código de cada provincia.
- **Municipios**: Nombre y código que requiere la AEMET para su API.

### Uso de los datos

Estos datos pueden ser utilizados para facilitar la interacción con la API de la AEMET, especialmente para construir consultas relacionadas con municipios específicos o para mostrar información en interfaces de usuario. Adicionalmente, los scripts de Python pueden automatizar la creación de consultas SQL para insertar esta información en bases de datos.

## Estructura del repositorio

- `/data/provincias.json`: Lista de todas las provincias con su código.
- `/data/localidades_{codigo_provincia}.json`: Archivos con la lista de localidades para cada provincia. El sufijo `{codigo_provincia}` corresponde al código de la provincia.
- `/scripts`: Scripts en Python para generar consultas SQL basadas en los datos JSON.

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

Archivo: `data/localidades_16.json`

```json
[
  {
    "id": "16023",
    "id_provincia": "16",
    "name": "Tarancón"
  },
  {
    "id": "16078",
    "id_provincia": "16",
    "name": "Cuenca"
  }
]
```

## Contribuciones

Si encuentras errores en los datos o quieres mejorar el repositorio, eres bienvenido a crear un _issue_ o enviar un _pull request_.

## Nota legal

El uso de los datos proporcionados por la AEMET está sujeto a su [nota legal](https://www.aemet.es/es/nota_legal). Por favor, consulta esta nota para asegurarte de cumplir con los términos y condiciones establecidos.
