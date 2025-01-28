import json
import os

# Cargar el archivo JSON
with open(
    "../data/provincias.json",
    "r",
    encoding="utf-8",
) as file:
    data = json.load(file)

# Generar las consultas SQL
sql_queries = []
for item in data:
    name = item["name"]
    sql_query = f"INSERT INTO Province (id, name) VALUES ('{item['id']}', '{name}');"
    sql_queries.append(sql_query)

# Creamos el directorio queries si no existe
if not os.path.exists("queries"):
    os.makedirs("queries")

# Guardar las consultas SQL en un archivo
with open("./queries/provincias-queries.sql", "w", encoding="utf-8") as file:
    for query in sql_queries:
        file.write(query + "\n")

print("Consultas SQL generadas y guardadas en insert_queries.sql")
