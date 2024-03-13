from flask import Flask #flask é uma biblioteca e Flask e uma classe

app = Flask

@app.route('/')

#Função que realiza ações
def ola():
    return 'Olá, mundo!'


