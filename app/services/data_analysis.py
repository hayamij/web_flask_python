"""
Data Analysis Service - Xử lý dữ liệu với Pandas
Separation of Concerns: Tất cả logic xử lý data nằm ở đây
"""
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Any
import os


class DataAnalysisService:
    """Service xử lý và phân tích dữ liệu sản phẩm"""
    
    def __init__(self, csv_path: str, orders_path: str = 'orders.csv', order_details_path: str = 'order_details.csv'):
        """
        Khởi tạo service với đường dẫn CSV
        
        Args:
            csv_path: Đường dẫn tới file CSV
        """
        self.csv_path = csv_path
        self.df: pd.DataFrame = None
        self.orders_path = orders_path
        self.order_details_path = order_details_path
        self.orders_df: pd.DataFrame = None
        self.order_details_df: pd.DataFrame = None
    
    def load_data(self) -> pd.DataFrame:
        """
        Load dữ liệu từ CSV
        
        Returns:
            DataFrame chứa dữ liệu
        
        Raises:
            FileNotFoundError: Nếu file không tồn tại
        """
        try:
            if not os.path.exists(self.csv_path):
                raise FileNotFoundError(f"CSV file not found: {self.csv_path}")
            
            self.df = pd.read_csv(self.csv_path)
            return self.df
        except Exception as e:
            raise Exception(f"Error loading CSV: {str(e)}")
    
    def get_basic_stats(self) -> Dict[str, Any]:
        """
        Tính toán các chỉ số thống kê cơ bản
        
        Returns:
            Dictionary chứa các chỉ số
        """
        if self.df is None:
            self.load_data()
        
        total_products = len(self.df)
        total_quantity = int(self.df['quantity'].sum())
        total_revenue = float((self.df['price'] * self.df['quantity']).sum())
        avg_price = float(self.df['price'].mean())
        avg_quantity = float(self.df['quantity'].mean())
        
        return {
            'total_products': total_products,
            'total_quantity': total_quantity,
            'total_revenue': total_revenue,
            'avg_price': avg_price,
            'avg_quantity': avg_quantity
        }

    def load_orders(self) -> pd.DataFrame:
        """Load orders CSV into DataFrame"""
        try:
            if not os.path.exists(self.orders_path):
                raise FileNotFoundError(f"Orders file not found: {self.orders_path}")

            self.orders_df = pd.read_csv(self.orders_path, parse_dates=['order_date'])
            return self.orders_df
        except Exception as e:
            raise Exception(f"Error loading orders CSV: {str(e)}")

    def load_order_details(self) -> pd.DataFrame:
        """Load order_details CSV into DataFrame"""
        try:
            if not os.path.exists(self.order_details_path):
                raise FileNotFoundError(f"Order details file not found: {self.order_details_path}")

            self.order_details_df = pd.read_csv(self.order_details_path)
            return self.order_details_df
        except Exception as e:
            raise Exception(f"Error loading order details CSV: {str(e)}")

    def get_total_orders(self) -> int:
        if self.orders_df is None:
            self.load_orders()
        return len(self.orders_df)

    def get_total_revenue(self) -> float:
        # prefer authoritative total in orders.csv if present
        if self.orders_df is None:
            try:
                self.load_orders()
            except Exception:
                pass

        if self.orders_df is not None and 'total' in self.orders_df.columns:
            return float(self.orders_df['total'].sum())

        if self.order_details_df is None:
            self.load_order_details()

        return float(self.order_details_df['subtotal'].sum())

    def get_total_quantity_sold(self) -> int:
        if self.order_details_df is None:
            self.load_order_details()
        return int(self.order_details_df['quantity'].sum())

    def get_avg_order_value(self) -> float:
        total_orders = self.get_total_orders()
        if total_orders == 0:
            return 0.0
        total_revenue = self.get_total_revenue()
        return float(total_revenue / total_orders)

    def get_revenue_over_time(self) -> pd.DataFrame:
        """Return DataFrame with order_date and total revenue per date"""
        if self.orders_df is None:
            self.load_orders()

        df = self.orders_df.copy()
        if 'order_date' in df.columns:
            df['order_date'] = pd.to_datetime(df['order_date'])
            grouped = df.groupby(df['order_date'].dt.date)['total'].sum().reset_index()
            grouped = grouped.sort_values('order_date')
            return grouped
        return pd.DataFrame(columns=['order_date', 'total'])

    def get_orders_per_day(self) -> pd.DataFrame:
        if self.orders_df is None:
            self.load_orders()
        df = self.orders_df.copy()
        df['order_date'] = pd.to_datetime(df['order_date'])
        grouped = df.groupby(df['order_date'].dt.date).size().reset_index(name='orders')
        grouped = grouped.sort_values('order_date')
        return grouped

    def get_top_products_by_revenue(self, n: int = 10) -> pd.DataFrame:
        if self.order_details_df is None:
            self.load_order_details()

        grouped = self.order_details_df.groupby(['product_id', 'product_name'])['subtotal'].sum().reset_index()
        grouped = grouped.sort_values('subtotal', ascending=False).head(n)
        return grouped
    
    def get_product_data(self) -> Tuple[List[str], List[int], List[float]]:
        """
        Lấy dữ liệu sản phẩm cho biểu đồ
        
        Returns:
            Tuple (labels, quantities, prices)
        """
        if self.df is None:
            self.load_data()
        
        labels = self.df['name'].tolist()
        quantities = self.df['quantity'].tolist()
        prices = self.df['price'].tolist()
        
        return labels, quantities, prices
    
    def get_revenue_by_product(self) -> pd.DataFrame:
        """
        Tính doanh thu theo từng sản phẩm
        
        Returns:
            DataFrame với cột revenue
        """
        if self.df is None:
            self.load_data()
        
        df_copy = self.df.copy()
        df_copy['revenue'] = df_copy['price'] * df_copy['quantity']
        return df_copy.sort_values('revenue', ascending=False)
    
    def get_top_products(self, n: int = 5, by: str = 'quantity') -> pd.DataFrame:
        """
        Lấy top N sản phẩm
        
        Args:
            n: Số lượng sản phẩm cần lấy
            by: Tiêu chí sắp xếp ('quantity', 'price', 'revenue')
        
        Returns:
            DataFrame chứa top products
        """
        if self.df is None:
            self.load_data()
        
        df_copy = self.df.copy()
        
        if by == 'revenue':
            df_copy['revenue'] = df_copy['price'] * df_copy['quantity']
            return df_copy.nlargest(n, 'revenue')
        else:
            return df_copy.nlargest(n, by)
