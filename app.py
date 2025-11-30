from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask!"

@app.route("/dashboard")
def dashboard():
    # Đọc CSV
    df = pd.read_csv("products.csv")

    # Lấy dữ liệu cho Chart.js
    labels = df["name"].tolist()
    values = df["quantity"].tolist()

    # Tính thống kê
    total_products = len(df)
    total_quantity = df["quantity"].sum()
    total_revenue = (df["price"] * df["quantity"]).sum()

    return render_template(
        "dashboard.html",
        labels=labels,
        values=values,
        total_products=total_products,
        total_quantity=total_quantity,
        total_revenue=total_revenue
    )

if __name__ == "__main__":
    app.run(debug=True)
