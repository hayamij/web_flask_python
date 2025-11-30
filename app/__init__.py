"""
Application Factory Pattern
Khởi tạo Flask app với các extensions và blueprints
"""
from flask import Flask
from config import config
from app.extensions import db, migrate


def create_app(config_name: str = 'default') -> Flask:
    """
    Application Factory
    
    Args:
        config_name: Tên config (development, production, testing)
    
    Returns:
        Flask application instance
    """
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    from app.routes.admin import admin_bp
    app.register_blueprint(admin_bp)
    
    # Create database tables (trong development)
    with app.app_context():
        db.create_all()
    
    return app
