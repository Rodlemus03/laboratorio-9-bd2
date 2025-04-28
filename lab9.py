import pandas as pd
from pymongo import MongoClient
from pymongo import InsertOne

# Leer el archivo CSV
df = pd.read_csv("ventas.csv")  
data = df.to_dict(orient="records")

# Conectar a MongoDB
uri = "mongodb+srv://riv22500:Uvgbd2@proyecto.wkyu8ko.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client["videojuegos_proyecto"]
collection = db["ventas"]

# Preparar las operaciones para bulkWrite
bulk_operations = [InsertOne(record) for record in data]

# Ejecutar bulkWrite
result = collection.bulk_write(bulk_operations)

# Verificar los resultados
print(f"Datos insertados correctamente: {result.inserted_count} documentos.")
client.close()
