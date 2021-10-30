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
}

GOOGLE_LOGIN_CLIENT_ID = getenv("GOOGLE_CLIENT_ID")
GOOGLE_LOGIN_CLIENT_SECRET = getenv("GOOGLE_CLIENT_SECRET")

FLASK_SECRET = getenv("FLASK_SECRET")
