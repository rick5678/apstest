from flask import Flask, render_template, request, redirect, session, flash, url_for
import cv2
import numpy as np
from infoEmpresa import *

app = Flask(__name__)
app.secret_key = 'alura'


class Usuario:
    def __init__(self, id, nome, senha, cargo):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.cargo = cargo


usuario1 = Usuario('gustavo', 'Gustavo', cv2.imread('digital.jpg'), '2')
usuario2 = Usuario('arion', 'Arion', '1234', '2')
usuario3 = Usuario('henrique', 'Henrique', '1234', 'CLI')

usuarios = {usuario1.id: usuario1,
            usuario2.id: usuario2,
            usuario3.id: usuario3}

empresas = [empresa1, empresa2]

lista = [produto1, produto2, produto3]
lista2 = [produto1, produto3]

fiscais = [fiscal1, fiscal2]


@app.route('/')
def index():
    return render_template('login.html', titulo='Agrotoxicos', Produtos=lista)


@app.route('/home')
def home():
    return render_template('home.html', empresa=empresas)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Produto')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima,)

@app.route('/fiscal')
def fiscal():
    proxima = request.args.get('proxima')
    return render_template('fiscal.html', Fiscal=fiscais)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        imgLogada = cv2.imread(request.form['senha'])
        dif = cv2.subtract(imgLogada, usuario.senha)
        result = not np.any(dif)
        if result is True:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            if usuario.cargo == '2':
                return render_template('home.html', titulo=usuario.nome,  Produtos=lista, usuario=usuario, empresa=empresas)
            if usuario.cargo == '1':
                return render_template('home.html', titulo=usuario.nome,  Produtos=lista, usuario=usuario, empresa=empresas)
        return redirect(proxima_pagina)
    else:
        flash('Não logado, tente novamente!')
        return redirect(url_for('login'))
    


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')

    return redirect(url_for('index'))


app.run(debug=True)
