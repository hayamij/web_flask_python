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
    
    def __init__(self, csv_path: str):
        """
        Khởi tạo service với đường dẫn CSV
        
        Args:
            csv_path: Đường dẫn tới file CSV
        """
        self.csv_path = csv_path
        self.df: pd.DataFrame = None
    
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
