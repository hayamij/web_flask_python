"""
Visualizer Service - Tạo biểu đồ với Plotly
Python First: Tất cả biểu đồ được tạo từ Python, không viết JS thủ công
"""
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from typing import Dict, List, Any
import json


class VisualizerService:
    """Service tạo biểu đồ tương tác với Plotly"""
    
    @staticmethod
    def create_bar_chart(
        labels: List[str], 
        values: List[int], 
        title: str = "Biểu đồ cột"
    ) -> str:
        """
        Tạo biểu đồ cột với Plotly
        
        Args:
            labels: Tên các mục
            values: Giá trị tương ứng
            title: Tiêu đề biểu đồ
        
        Returns:
            HTML string của biểu đồ
        """
        fig = go.Figure(data=[
            go.Bar(
                x=labels,
                y=values,
                marker=dict(
                    color=values,
                    colorscale='Viridis',
                    showscale=True
                ),
                text=values,
                textposition='auto',
            )
        ])
        
        fig.update_layout(
            title=title,
            xaxis_title="Sản phẩm",
            yaxis_title="Số lượng",
            template="plotly_white",
            height=400,
            hovermode='x unified'
        )
        
        return fig.to_html(full_html=False, include_plotlyjs='cdn')
    
    @staticmethod
    def create_pie_chart(
        labels: List[str], 
        values: List[float], 
        title: str = "Biểu đồ tròn"
    ) -> str:
        """
        Tạo biểu đồ tròn với Plotly
        
        Args:
            labels: Tên các mục
            values: Giá trị tương ứng
            title: Tiêu đề
        
        Returns:
            HTML string
        """
        fig = go.Figure(data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.4,  # Donut chart
                textinfo='label+percent',
                textposition='auto',
                marker=dict(
                    colors=px.colors.qualitative.Set3
                )
            )
        ])
        
        fig.update_layout(
            title=title,
            template="plotly_white",
            height=400
        )
        
        return fig.to_html(full_html=False, include_plotlyjs='cdn')
    
    @staticmethod
    def create_multi_chart(df: pd.DataFrame) -> str:
        """
        Tạo dashboard với nhiều biểu đồ con
        
        Args:
            df: DataFrame chứa dữ liệu
        
        Returns:
            HTML string chứa nhiều biểu đồ
        """
        # Tính revenue
        df = df.copy()
        df['revenue'] = df['price'] * df['quantity']
        
        # Create subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=(
                'Số lượng sản phẩm',
                'Giá sản phẩm',
                'Doanh thu theo sản phẩm',
                'Phân bổ doanh thu'
            ),
            specs=[
                [{"type": "bar"}, {"type": "bar"}],
                [{"type": "bar"}, {"type": "pie"}]
            ]
        )
        
        # Chart 1: Quantity
        fig.add_trace(
            go.Bar(x=df['name'], y=df['quantity'], name='Số lượng',
                   marker_color='lightblue'),
            row=1, col=1
        )
        
        # Chart 2: Price
        fig.add_trace(
            go.Bar(x=df['name'], y=df['price'], name='Giá',
                   marker_color='lightgreen'),
            row=1, col=2
        )
        
        # Chart 3: Revenue
        fig.add_trace(
            go.Bar(x=df['name'], y=df['revenue'], name='Doanh thu',
                   marker_color='coral'),
            row=2, col=1
        )
        
        # Chart 4: Revenue pie
        fig.add_trace(
            go.Pie(labels=df['name'], values=df['revenue'], name='Doanh thu'),
            row=2, col=2
        )
        
        fig.update_layout(
            height=800,
            showlegend=False,
            template="plotly_white"
        )
        
        return fig.to_html(full_html=False, include_plotlyjs='cdn')
    
    @staticmethod
    def create_line_chart(
        x: List[Any],
        y: List[float],
        title: str = "Biểu đồ đường",
        x_title: str = "X",
        y_title: str = "Y"
    ) -> str:
        """
        Tạo biểu đồ đường
        
        Args:
            x: Dữ liệu trục X
            y: Dữ liệu trục Y
            title: Tiêu đề
            x_title: Label trục X
            y_title: Label trục Y
        
        Returns:
            HTML string
        """
        fig = go.Figure(data=[
            go.Scatter(
                x=x,
                y=y,
                mode='lines+markers',
                line=dict(color='royalblue', width=3),
                marker=dict(size=8)
            )
        ])
        
        fig.update_layout(
            title=title,
            xaxis_title=x_title,
            yaxis_title=y_title,
            template="plotly_white",
            height=400
        )
        
        return fig.to_html(full_html=False, include_plotlyjs='cdn')
