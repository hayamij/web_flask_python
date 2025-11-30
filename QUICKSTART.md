# QUICK START GUIDE

## Bước 1: Cài đặt dependencies
```bash
pip install -r requirements.txt
```

Hoặc cài từng package quan trọng:
```bash
pip install Flask==3.0.0
pip install Flask-SQLAlchemy==3.1.1
pip install Flask-Migrate==4.0.5
pip install pandas==2.1.4
pip install plotly==5.18.0
```

## Bước 2: Chạy server
```bash
python run.py
```

## Bước 3: Truy cập Dashboard
Mở browser: http://127.0.0.1:5000/dashboard

---

## Kết quả mong đợi

Dashboard sẽ hiển thị:

1. **4 Cards thống kê:**
   - Tổng sản phẩm
   - Tổng số lượng
   - Tổng doanh thu
   - Giá trung bình

2. **3 Loại biểu đồ Plotly tương tác:**
   - Bar Chart (Số lượng sản phẩm)
   - Pie Chart (Phân bổ doanh thu)
   - Multi Dashboard (4 biểu đồ con)

3. **Bảng chi tiết sản phẩm**
   - Sắp xếp theo doanh thu

---

## Troubleshooting

### Lỗi: ModuleNotFoundError
```bash
# Đảm bảo đang trong virtual environment
python -m venv venv
venv\Scripts\activate

# Cài lại dependencies
pip install -r requirements.txt
```

### Lỗi: File not found (products.csv)
```bash
# Đảm bảo file products.csv nằm ở root folder
# Và run.py cũng chạy từ root folder
cd web_flask_python
python run.py
```

### Lỗi: Port 5000 already in use
```python
# Sửa trong run.py
app.run(debug=True, host='0.0.0.0', port=5001)  # Đổi port
```

---

## Cấu trúc quan trọng cần nhớ

```
web_flask_python/
├── run.py              ← Entry point (chạy file này)
├── config.py           ← Configuration
├── products.csv        ← Data source
├── requirements.txt    ← Dependencies
└── app/
    ├── __init__.py     ← App Factory
    ├── routes/
    │   └── admin.py    ← Routes (chỉ nhận request)
    └── services/
        ├── data_analysis.py   ← Logic xử lý data
        └── visualizer.py      ← Tạo biểu đồ Plotly
```

---

## Nguyên tắc code

1. **Routes chỉ nhận request**, không có logic
2. **Services xử lý tất cả logic** (data + visualization)
3. **Plotly từ Python**, hạn chế JavaScript
4. **Type Hints** cho mọi function
5. **try/except** cho mọi operation

---

## Tài liệu tham khảo

- Flask: https://flask.palletsprojects.com/
- Plotly: https://plotly.com/python/
- Pandas: https://pandas.pydata.org/
- SQLAlchemy: https://www.sqlalchemy.org/
