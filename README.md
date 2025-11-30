# Flask Product Dashboard

This is a simple Flask web application that reads product data from a CSV file and displays it on a dashboard.

## Features

- Displays a dashboard with statistics about the products.
- Shows a chart of product quantities.

## Installation

1. Clone the repository:
   ```bash
   git clone https://your-repository-url.git
   ```
2. Install the required packages:
   ```bash
   pip install Flask pandas
   ```

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open your web browser and go to `http://127.0.0.1:5000/dashboard` to see the dashboard.

## File Descriptions

- `app.py`: The main Flask application file.
- `products.csv`: The CSV file containing the product data.
- `templates/dashboard.html`: The HTML template for the dashboard.
- `static/css/style.css`: The CSS file for styling the dashboard.
- `static/js/chart.js`: The JavaScript file for creating the chart.
