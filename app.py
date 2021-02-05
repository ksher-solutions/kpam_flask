from flask import Flask
from flask_talisman import Talisman
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    from kpam import kpam_bp
    app.register_blueprint(kpam_bp)


    # Adding Content Security Policy to load all content either locally or from omise.co.
    Talisman(app)

    return app
