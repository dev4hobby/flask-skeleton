from apps import mongo
from settings import DATABASES

db = mongo.db.client.get_database(DATABASES.get("name"))
