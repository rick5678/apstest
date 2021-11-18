from flask import Flask, render_template, request, redirect, session, flash, url_for
import cv2
import numpy as np
from infoEmpresa import *

app = Flask(__name__)
app.secret_key = 'alura'

class Agrotoxico:
    def __init__(self, nome):
        self.nome = nome

class Usuario:
    def __init__(self, id, nome, senha, cargo):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.cargo = cargo

usuario1 = Usuario('gustavo', 'Gustavo', cv2.imread('digital.jpg'), '3')
usuario2 = Usuario('arion', 'Arion',  cv2.imread('digital2.jpg'), '2')
usuario3 = Usuario('henrique', 'Henrique',  cv2.imread('digital3.jpg'), '3')

usuarios = {usuario1.id: usuario1,
            usuario2.id: usuario2,
            usuario3.id: usuario3}

empresas = [empresa1, empresa2, empresa3, empresa4, empresa5]

produtos = [lista, lista2, lista3, lista4, lista5]

fiscais = [fiscal1, fiscal2, fiscal3, fiscal4, fiscal5]

agrotoxico1 = Agrotoxico('Não sei')
listaagro = [agrotoxico1]

@app.route('/agrotoxicos')
def agrotoxicos():
    proxima = request.args.get('proxima')
    return render_template('agrotoxicos.html', agrotoxicos=listaagro)


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


@app.route('/autenticar', methods=['POST', 'GET'])
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
            if usuario.cargo == '3':
                return render_template('home.html', titulo=usuario.nome,  Produtos=produtos, usuario=usuario, empresa=empresas)
            if usuario.cargo == '2':
                return render_template('home.html', titulo=usuario.nome,  Produtos=produtos, usuario=usuario, empresa=empresas)
            if usuario.cargo == '1':
                return render_template('home.html', titulo=usuario.nome,  Produtos=produtos, usuario=usuario, empresa=empresas)
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
