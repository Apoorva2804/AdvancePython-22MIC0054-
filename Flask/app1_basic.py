from flask import Flask
import random, webbrowser
from threading import Timer

app = Flask(__name__)

quotes = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The future depends on what you do today. – Mahatma Gandhi",
    "Dream big. Start small. Act now. – Robin Sharma",
    "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
    "Everything you can imagine is real. – Pablo Picasso"
]

@app.route('/')
def home():
    return (
        "<h1>🌟 Welcome to the Quote Generator</h1>"
        "<p>Visit <code>/quote</code> to get inspired!</p>"
    )

@app.route('/quote')
def get_quote():
    return f"<h3>💬 {random.choice(quotes)}</h3>"

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5010/")

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True, port=5010)
