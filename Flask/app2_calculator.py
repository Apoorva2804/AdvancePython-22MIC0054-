from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2> Mini Calculator</h2><p>Try /calc?a=10&b=5&op=add</p>"

@app.route('/calc')
def calc():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    op = request.args.get('op', 'add').lower()

    ops = {
        "add": a + b,
        "sub": a - b,
        "mul": a * b,
        "div": a / b if b != 0 else "∞"
    }

    if op not in ops:
        return "⚠️ Invalid operation. Use add, sub, mul, or div."

    return f"<h3>Result: {ops[op]}</h3>"

if __name__ == '__main__':
    app.run(debug=True, port=5012)
