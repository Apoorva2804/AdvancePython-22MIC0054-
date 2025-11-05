from flask import Flask
import plotly.graph_objects as go
import random, webbrowser
from threading import Timer

app = Flask(__name__)

@app.route('/')
def home():
    return (
        "<h2> Crop Price Visualization</h2>"
        "<p>Visit <a href='/crop_trend'>/crop_trend</a> to see an interactive graph.</p>"
    )

@app.route('/crop_trend')
def crop_trend():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"]
    rice = [random.randint(20, 40) for _ in months]
    wheat = [random.randint(15, 35) for _ in months]
    maize = [random.randint(10, 30) for _ in months]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=months, y=rice, mode='lines+markers', name='Rice'))
    fig.add_trace(go.Scatter(x=months, y=wheat, mode='lines+markers', name='Wheat'))
    fig.add_trace(go.Scatter(x=months, y=maize, mode='lines+markers', name='Maize'))

    fig.update_layout(
        title="📊 Crop Price Trends (₹ per kg)",
        xaxis_title="Month",
        yaxis_title="Price (₹)",
        template="plotly_dark"
    )

    return fig.to_html()

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5021/")

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True, port=5021)
