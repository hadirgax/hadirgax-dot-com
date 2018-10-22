from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello, World! and Hello Hadir"

@app.route("/about")
def about():
    return "About Hadir Page!"

if __name__ == "__main__":
    app.run(debug=True)