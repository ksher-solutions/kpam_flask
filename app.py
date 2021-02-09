from flask import Flask
from flask_talisman import Talisman
from config import Config
from flask_cors import CORS


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    from kpam import kpam_bp
    app.register_blueprint(kpam_bp)

    # Initiate CORS
    CORS(app)
    
    # Adding Content Security Policy 
    Talisman(app)

    return app
