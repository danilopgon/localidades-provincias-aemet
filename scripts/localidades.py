import json
import os

# Obtener todos los archivos JSON que empiecen por 'localidades_'
json_files = [
    f
    for f in os.listdir("../data")
    if f.startswith("localidades_") and f.endswith(".json")
]

# Generar las consultas SQL
sql_queries = []
for json_file in json_files:
    with open(f"../data/{json_file}", "r", encoding="utf-8") as file:
        data = json.load(file)
        for item in data:
            name = item["name"].replace("'", "''")  # Escapar comillas simples
            province_id = item["provinceId"]
            sql_query = f"INSERT INTO City (id, name, provinceId) VALUES ('{item['id']}', '{name}', '{province_id}');"
            sql_queries.append(sql_query)

# Crear el directorio queries si no existe
if not os.path.exists("queries"):
    os.makedirs("queries")

# Guardar las consultas SQL en un archivo
with open("./queries/localidades-queries.sql", "w", encoding="utf-8") as file:
    for query in sql_queries:
        file.write(query + "\n")

print("Consultas SQL generadas y guardadas en localidades-queries.sql")
