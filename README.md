# No_sql_exercise on redis
# Redis Movie & Actor Database

Cette application utilise **Redis** comme base de données en mémoire pour stocker et manipuler des données sur des **films** et des **acteurs**. Elle est conçue pour fonctionner avec des scripts en **Python** (via un Notebook Jupyter) et permet d'exécuter diverses requêtes analytiques.

## 📃 Structure des données

### 1. **Acteurs**

* **Clé principale** : `actor:<id>`
* **Type** : Hash
* **Exemple** :

```python
{
  "first_name": "Jon",
  "last_name": "Hamm",
  "date_of_birth": "1971"
}
```

* **Volume** : Environ **1300** entrées

### 2. **Films**

* **Clé principale** : `movie:<id>`
* **Type** : Hash
* **Exemple** :

```python
{
  "title": "Guardians of the Galaxy",
  "release_year": "2014",
  "genre": "Action",
  "rating": "8.1",
  "votes": "704613",
  "plot": "A group of intergalactic criminals must pull together...",
  "poster": "https://...",
  "ibmdb_id": "tt2015381"
}
```

* **Volume** : Environ **900** entrées

## ⚙️ Fonctionnalités disponibles

* 🔍 **Lister les films les mieux notés**
* 🎯 **Filtrer les films récents avec beaucoup de votes**
* 📊 **Compter les films au-dessus d’un seuil de note**
* 🔧 **Mettre à jour la note d’un film spécifique**
* 🏆 **Créer des hash de meilleurs films par genre**


## 🧪 Process 
* Le fichier (docker-compose.yml) a permis de définir et lancer plusieurs services (Jupyter Notebook, Redis, Redis Insights).
* Chargement des données `.redis` depuis un script python  ou manuellement dans Redis
* Analyse et manipulatvia un Notebook Jupyter avec le client `redis-py`
* Utilisation d'opérations simples (`hgetall`, `hset`, `keys`, `scan`) pour interroger et manipuler les données
