from flask import Flask

app = Flask(__name__)

@app.route("/olamundo")
def hello_world():
    return "<h1>Olá mundo!<h1>"
