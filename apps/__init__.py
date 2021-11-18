def create_app():
    from flask import Flask
    from flask_cors import CORS
    from utils.env import get_database_uri
    from utils.auth import generate_key
    from settings import DATABASES
    from database import db
    from . import home, misc, wtfLab, redisLab

    app = Flask(__name__)
    app.secret_key = generate_key(16)

    app.config["MONGODB_SETTINGS"] = {
        "db": DATABASES.get("name"),
        "host": get_database_uri(DATABASES),
        "port": int(DATABASES.get("port")),
        "username": DATABASES.get("username"),
        "password": DATABASES.get("password"),
    }
    db.init_app(app)

    app.register_blueprint(home.home)
    app.register_blueprint(misc.misc)
    app.register_blueprint(wtfLab.wtf)
    app.register_blueprint(redisLab.redis_lab)

    CORS(app, support_credentials=True)

    return app
