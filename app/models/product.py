"""
Product model - Quản lý sản phẩm
"""
from app.extensions import db
from datetime import datetime
from typing import Optional


class Product(db.Model):
    """Model cho bảng products"""
    __tablename__ = 'products'
    
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(200), nullable=False)
    price: float = db.Column(db.Float, nullable=False)
    quantity: int = db.Column(db.Integer, nullable=False, default=0)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f'<Product {self.name}>'
    
    def to_dict(self) -> dict:
        """Chuyển model thành dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
