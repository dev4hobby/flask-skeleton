from os import getenv, environ
from utils.env import init_json_env
from datetime import datetime

init_json_env(environ.get("ENVIRONMENT", "dev"))
WOKEUP_TIME = datetime.now()
DATABASES = {
    "host": getenv("MONGO_HOST"),
    "port": getenv("MONGO_PORT", 27017),
    "user": getenv("MONGO_USER"),
    "password": getenv("MONGO_PASSWORD"),
    "name": getenv("MONGO_NAME"),
}

REDIS = {
    "expire": int(getenv("REDIS_EXPIRE", 3600)),
    "host": getenv("REDIS_HOST", "localhost"),
    "port": getenv("REDIS_PORT", 6379),
    "password": getenv("REDIS_PASSWORD", None),
}

GOOGLE_LOGIN_CLIENT_ID = getenv("GOOGLE_CLIENT_ID")
GOOGLE_LOGIN_CLIENT_SECRET = getenv("GOOGLE_CLIENT_SECRET")

FLASK_SECRET = getenv("FLASK_SECRET")
