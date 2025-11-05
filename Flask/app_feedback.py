from flask import Flask, request

app = Flask(__name__)
feedback_list = []

@app.route('/')
def home():
    return (
        "<h2>💬 Flask Feedback App</h2>"
        "<p>Submit feedback: /submit?name=Apoorva&msg=Nice+App!</p>"
        "<p>View all feedback: /view</p>"
    )

@app.route('/submit')
def submit():
    name = request.args.get('name')
    msg = request.args.get('msg')
    if not name or not msg:
        return "⚠️ Please provide both name and msg."
    feedback_list.append((name, msg))
    return f"✅ Thanks {name}! Feedback saved."

@app.route('/view')
def view():
    if not feedback_list:
        return "No feedback yet."
    return "<br>".join([f"<b>{n}</b>: {m}" for n, m in feedback_list])

if __name__ == '__main__':
    app.run(debug=True, port=5014)
