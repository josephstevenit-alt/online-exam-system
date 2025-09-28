from flask import Flask
from .config import Config
from .extensions import db, migrate, jwt, bcrypt
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # import blueprints here to avoid circular imports
    from .routes.auth import auth_bp
    from .routes.questions import q_bp
    from .routes.exams import exam_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(q_bp, url_prefix="/api/questions")
    app.register_blueprint(exam_bp, url_prefix="/api/exams")

    return app
