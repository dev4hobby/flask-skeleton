from flask import Flask
from flask_cors import CORS
from utils.env import get_database_uri
from utils.auth import generate_key
from flask_oauthlib.client import OAuth
from settings import *
from database import db
from . import home, misc, wtfLab

oauth = OAuth()
google = oauth.remote_app(
    "google",
    consumer_key=GOOGLE_LOGIN_CLIENT_ID,
    consumer_secret=GOOGLE_LOGIN_CLIENT_SECRET,
    request_token_params={"scope": "email"},
    base_url="https://www.googleapis.com/oauth2/v1/",
    request_token_url=None,
    access_token_method="POST",
    access_token_url="https://accounts.google.com/o/oauth2/token",
    authorize_url="https://accounts.google.com/o/oauth2/auth",
)

app = Flask(__name__)
app.secret_key = generate_key(16)
app.config["MONGO_URI"] = get_database_uri(DATABASES)
db.init_app(app)
app.register_blueprint(home.home)
app.register_blueprint(misc.misc)
app.register_blueprint(wtfLab.wtf)

CORS(app, support_credentials=True)
