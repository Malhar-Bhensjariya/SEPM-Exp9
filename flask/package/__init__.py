from flask_cors import CORS
from flask import Flask

def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    from package.main.routes import main_bp
    app.register_blueprint(main_bp, url_prefix='/api/main')
    return app