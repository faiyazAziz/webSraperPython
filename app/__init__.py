from flask import Flask

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('app.config.Config')

    # Register Blueprints or routes
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
