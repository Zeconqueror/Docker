!pip install pymongo dotenv
from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

usr = os.environ.get("MONGO_INITDB_ROOT_USERNAME")
pwd = os.environ.get("MONGO_INITDB_ROOT_PASSWORD")
url = f"mongodb://{usr}:{pwd}@mongodb:27017"
client = MongoClient(url)

import csv
from pymongo import MongoClient

# MongoDB connection
db = client['Medical']
collection = db['Patient']

import csv
import json
import json
from pymongo import MongoClient

fcsv = 'healthcare_dataset-20250506.csv'
fjson = 'file.json'
data = []
with open(fcsv) as csvfile:
    reader = csv.DictReader(csvfile)
    for rows in reader:
        data.append(rows)
# Enregistrer le fichier JSON
with open(fjson, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=2))
print("JSON enregistrer!")


#db = client['db_senegal'] #remplacer par le nom de la base
#collection_currency = db['regions_sn']#remplacer /nom collection

with open(fjson) as f:
    file_data = json.load(f)

# utiliser collection_currency.insert(file_data) si la version de pymongo est < 3.0
db.medical.insert_many(file_data)
#client.close()
print('Fichier Importer avec succes!!')

db.Medical.insert_many(file_data)