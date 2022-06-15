from flask import Flask

app = Flask(__name__)

def calculo():
    return "200"

@app.route("/")
def hello_world():
    return calculo()

@app.route("/holaa")
def hello_aqui():
    return "<p>holaa si </p>"