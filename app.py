from flask import Flask #flask é uma biblioteca e Flask e uma classe

app = Flask ("Olá")

@app.route("/")

def ola():
    return "Olá, mundo!"


