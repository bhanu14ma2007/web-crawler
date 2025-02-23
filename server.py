from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample dataset (Replace with actual web crawler data)
search_data = [
    {"title": "Example Domain", "url": "https://example.com", "description": "This is an example website."},
    {"title": "Python Official", "url": "https://www.python.org", "description": "Python is a programming language."},
    {"title": "Flask Framework", "url": "https://flask.palletsprojects.com", "description": "Flask is a web framework for Python."},
    {"title": "EASY TO LEARN", "url": "https://bhanu14ma2007.github.io/very/", "description": "IT IS VAILITAYS DAY SEAPICIAL"},
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q", "").lower()
    results = [item for item in search_data if query in item["title"].lower() or query in item["description"].lower()]
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
