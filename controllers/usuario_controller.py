from models.usuario_model import usuarios, addUsuario
from flask import Blueprint, render_template, request, redirect, url_for, session
usuarios_controller = Blueprint('usuario', __name__)

usuarios_controller.secret_key = 'chave_muito_segura'

@usuarios_controller.route('/')
def index():
    if 'login' in session:
        return render_template('index.html', usuarios=usuarios)
    return 'Você não está logado! Faça <a href="/login">login</a> ou então <a href="cadastrar">crie sua conta</a>'

@usuarios_controller.route("/cadastrar", methods=["POST", "GET"])
def add():
    login = request.form['login']
    senha = request.form['senha']
    addUsuario(login, senha)
    return redirect(url_for('usuario.index'))

@usuarios_controller.route('/logout')
def logout():
    session.pop('login', None)
    return redirect(url_for(index))
