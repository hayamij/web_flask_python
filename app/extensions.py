"""
Flask extensions initialization
Tất cả extensions được khởi tạo ở đây và import vào __init__.py
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize extensions (chưa bind vào app)
db = SQLAlchemy()
migrate = Migrate()
