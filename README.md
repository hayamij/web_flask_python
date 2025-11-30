# E-commerce Admin Dashboard

## Mục tiêu dự án
Xây dựng trang quản trị E-commerce mạnh mẽ với Flask, tập trung vào Data Visualization sử dụng các thư viện Python.

## Kiến trúc dự án
- **Pattern**: Application Factory Pattern
- **Framework**: Flask 3.0
- **Database**: SQLAlchemy ORM
- **Data Processing**: Pandas + NumPy
- **Visualization**: Plotly (ưu tiên #1), Matplotlib, Seaborn

## Cấu trúc thư mục

```
web_flask_python/
├── app/
│   ├── __init__.py              # Application Factory
│   ├── extensions.py            # Extensions (db, migrate)
│   ├── models/                  # Database Models
│   │   ├── __init__.py
│   │   └── product.py
│   ├── routes/                  # Blueprints (Controllers)
│   │   ├── __init__.py
│   │   └── admin.py
│   ├── services/                # Business Logic & Data Processing
│   │   ├── __init__.py
│   │   ├── data_analysis.py     # Pandas data processing
│   │   └── visualizer.py        # Plotly chart generation
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   └── templates/
│       ├── base.html
│       ├── components/
│       │   └── sidebar.html
│       └── admin/
│           └── dashboard.html
├── config.py                    # Configuration classes
├── run.py                       # Entry point
├── requirements.txt             # Dependencies
└── products.csv                 # Sample data
```

## Cài đặt

### 1. Clone repository
```bash
git clone https://github.com/hayamij/web_flask_python.git
cd web_flask_python
```

### 2. Tạo virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

### 3. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 4. Chạy ứng dụng
```bash
python run.py
```

Truy cập: http://127.0.0.1:5000/dashboard

## Tính năng

### Dashboard Admin
- ✅ Thống kê tổng quan (Tổng sản phẩm, số lượng, doanh thu)
- ✅ Biểu đồ cột tương tác (Plotly)
- ✅ Biểu đồ tròn phân bổ doanh thu (Plotly)
- ✅ Dashboard đa biểu đồ (Subplots)
- ✅ Bảng chi tiết sản phẩm
- ✅ Xử lý dữ liệu với Pandas
- ✅ Server-Side Rendering (không viết JS thủ công)

## Tech Stack

| Category | Technology |
|----------|-----------|
| Backend | Flask 3.0 |
| Database | SQLAlchemy + SQLite |
| Data Processing | Pandas 2.1 + NumPy 1.26 |
| Visualization | Plotly 5.18 (Primary) |
| Alternative Viz | Matplotlib + Seaborn |
| Frontend | Bootstrap 5 + Jinja2 |
| Pattern | App Factory + Blueprints |

## 📝Coding Rules

### Separation of Concerns
- **Routes** (`app/routes/`): Chỉ nhận request và trả về template
- **Services** (`app/services/`): Chứa toàn bộ business logic
- **Models** (`app/models/`): Database schemas

### Python First
- Ưu tiên Server-Side Rendering
- Dùng Plotly tạo biểu đồ từ Python
- Hạn chế viết JavaScript thủ công
- Type Hints cho tất cả functions

### Error Handling
- `try/except` cho mọi database operations
- `try/except` cho data processing
- Logging errors với `current_app.logger`

## Development

### Cấu trúc Config
- `DevelopmentConfig`: DEBUG=True
- `ProductionConfig`: DEBUG=False
- `TestingConfig`: Dùng test database

### Database Migration
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## Roadmap

### Phase 1: Foundation
- [x] App Factory Pattern
- [x] Configuration system
- [x] Database models
- [x] Services layer
- [x] Admin blueprint
- [x] Plotly visualization
- [x] Dashboard template

### Phase 2: Enhancement (Next)
- [ ] User authentication (Flask-Login)
- [ ] CRUD operations cho products
- [ ] Advanced charts (Heatmaps, Line charts)
- [ ] Export reports (PDF/Excel)
- [ ] API endpoints (REST API)
- [ ] Real-time data với WebSocket

### Phase 3: Advanced Features
- [ ] Multi-tenancy support
- [ ] Advanced analytics
- [ ] Machine Learning integration
- [ ] Geographic visualization (Folium)

## 📄 License
MIT License

