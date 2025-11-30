"""
Admin Blueprint - Dashboard Routes
Route chỉ nhận request và trả về template.
Mọi logic xử lý nằm trong services.
"""
from flask import Blueprint, render_template, current_app
from app.services.data_analysis import DataAnalysisService
from app.services.visualizer import VisualizerService
from typing import Dict, Any
import os

admin_bp = Blueprint('admin', __name__, url_prefix='/')


@admin_bp.route('/')
def index():
    """Redirect to dashboard"""
    return render_template('admin/dashboard.html')


@admin_bp.route('/dashboard')
def dashboard():
    """
    Main dashboard with charts and statistics
    
    Returns:
        Rendered dashboard template
    """
    try:
        # Lấy đường dẫn CSV từ config
        csv_path = current_app.config.get('CSV_DATA_PATH', 'products.csv')
        
        # Khởi tạo services (Separation of Concerns)
        data_service = DataAnalysisService(csv_path)
        viz_service = VisualizerService()
        
        # Load và xử lý dữ liệu
        df = data_service.load_data()
        stats = data_service.get_basic_stats()
        labels, quantities, prices = data_service.get_product_data()
        revenue_df = data_service.get_revenue_by_product()
        
        # Tạo biểu đồ với Plotly (Server-Side Rendering)
        bar_chart = viz_service.create_bar_chart(
            labels=labels,
            values=quantities,
            title="📊 Số lượng sản phẩm trong kho"
        )
        
        pie_chart = viz_service.create_pie_chart(
            labels=labels,
            values=revenue_df['revenue'].tolist(),
            title="💰 Phân bổ doanh thu theo sản phẩm"
        )
        
        multi_chart = viz_service.create_multi_chart(df)
        
        # Trả về template với dữ liệu đã xử lý
        return render_template(
            'admin/dashboard.html',
            stats=stats,
            bar_chart=bar_chart,
            pie_chart=pie_chart,
            multi_chart=multi_chart,
            products=revenue_df.to_dict('records'),
            active='dashboard'
        )
    
    except FileNotFoundError as e:
        return render_template(
            'admin/dashboard.html',
            error=f"Không tìm thấy file dữ liệu: {str(e)}",
            active='dashboard'
        ), 404
    
    except Exception as e:
        current_app.logger.error(f"Dashboard error: {str(e)}")
        return render_template(
            'admin/dashboard.html',
            error=f"Lỗi khi tải dashboard: {str(e)}",
            active='dashboard'
        ), 500
