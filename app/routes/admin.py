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
        orders_path = current_app.config.get('ORDERS_CSV_PATH', 'orders.csv')
        order_details_path = current_app.config.get('ORDER_DETAILS_CSV_PATH', 'order_details.csv')
        # Khởi tạo services (Separation of Concerns)
        data_service = DataAnalysisService(csv_path)
        viz_service = VisualizerService()
        
        # Load và xử lý dữ liệu (products + orders)
        df = data_service.load_data()
        data_service.load_orders()
        data_service.load_order_details()

        # KPI stats
        stats = data_service.get_basic_stats()
        total_orders = data_service.get_total_orders()
        total_revenue = data_service.get_total_revenue()
        total_quantity_sold = data_service.get_total_quantity_sold()
        avg_order_value = data_service.get_avg_order_value()

        # Charts
        # 1) Revenue over time (line)
        rev_df = data_service.get_revenue_over_time()
        revenue_line = viz_service.create_line_chart(
            x=rev_df['order_date'].tolist(),
            y=rev_df['total'].tolist() if not rev_df.empty else [],
            title="Doanh thu theo ngày",
            x_title="Ngày",
            y_title="Doanh thu (₫)"
        )

        # 2) Top products by revenue (bar)
        top_products = data_service.get_top_products_by_revenue(n=8)
        top_bar = viz_service.create_bar_chart(
            labels=top_products['product_name'].tolist(),
            values=top_products['subtotal'].tolist(),
            title="Top sản phẩm theo doanh thu"
        )

        # 3) Orders per day (bar)
        orders_per_day = data_service.get_orders_per_day()
        orders_bar = viz_service.create_bar_chart(
            labels=orders_per_day['order_date'].astype(str).tolist(),
            values=orders_per_day['orders'].tolist(),
            title="Số đơn hàng theo ngày"
        )

        # Trả về template với dữ liệu đã xử lý
        return render_template(
            'admin/dashboard.html',
            stats={
                'total_products': stats['total_products'],
                'total_quantity': stats['total_quantity'],
                'total_revenue': total_revenue,
                'avg_price': stats['avg_price'],
                'avg_quantity': stats['avg_quantity'],
                'total_orders': total_orders,
                'total_quantity_sold': total_quantity_sold,
                'avg_order_value': avg_order_value
            },
            revenue_line=revenue_line,
            top_bar=top_bar,
            orders_bar=orders_bar,
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



@admin_bp.route('/charts')
def charts():
    """
    Simple page that renders a pie chart for all products (by quantity)

    Returns:
        Rendered charts template
    """
    try:
        csv_path = current_app.config.get('CSV_DATA_PATH', 'products.csv')

        data_service = DataAnalysisService(csv_path)
        viz_service = VisualizerService()

        df = data_service.load_data()
        labels, quantities, prices = data_service.get_product_data()

        # Create a larger pie chart for the charts page
        pie_chart = viz_service.create_pie_chart(
            labels=labels,
            values=quantities,
            title="📈 Phân bổ số lượng sản phẩm",
            height=700
        )

        return render_template(
            'admin/charts.html',
            pie_chart=pie_chart,
            products=df.to_dict('records'),
            active='charts'
        )

    except FileNotFoundError as e:
        return render_template(
            'admin/charts.html',
            error=f"Không tìm thấy file dữ liệu: {str(e)}",
            active='charts'
        ), 404

    except Exception as e:
        current_app.logger.error(f"Charts error: {str(e)}")
        return render_template(
            'admin/charts.html',
            error=f"Lỗi khi tải charts: {str(e)}",
            active='charts'
        ), 500



@admin_bp.route('/products')
def products():
    """
    Page to list detailed products (moved from dashboard)

    Returns:
        Rendered products template
    """
    try:
        csv_path = current_app.config.get('CSV_DATA_PATH', 'products.csv')

        data_service = DataAnalysisService(csv_path)

        df = data_service.load_data()
        df['revenue'] = df['price'] * df['quantity']

        return render_template(
            'admin/products.html',
            products=df.to_dict('records'),
            active='products'
        )

    except FileNotFoundError as e:
        return render_template(
            'admin/products.html',
            error=f"Không tìm thấy file dữ liệu: {str(e)}",
            active='products'
        ), 404

    except Exception as e:
        current_app.logger.error(f"Products error: {str(e)}")
        return render_template(
            'admin/products.html',
            error=f"Lỗi khi tải products: {str(e)}",
            active='products'
        ), 500
