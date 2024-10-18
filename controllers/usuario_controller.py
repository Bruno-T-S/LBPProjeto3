from models.usuario_model import usuarios, addUsuario
from controllers.cadastro_controller import *
from flask import Blueprint, render_template, request, redirect, url_for, session
usuarios_controller = Blueprint('usuario', __name__)

usuarios_controller.secret_key = 'chave_muito_segura'

@usuarios_controller.route('/')
def index():
    if 'login' in session:
        return render_template('logado', usuarios=usuarios)
    return render_template('home.html')

@usuarios_controller.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        login = request.form.get('login')
        senha = request.form.get('senha')
        for usuario in usuarios:
            if login == usuario.login and senha == usuario.senha:
                return f'Acesso autenticado, {login}'
        return f'Acesso negado. Clique <a href="/" para voltar para a página inicial.>aqui</a>'
    return render_template('login.html')

@usuarios_controller.route("/cadastrar", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        login = request.form.get('login')
        senha = request.form.get('senha')
        confirmacao = request.form.get('confirmacao')
        if not False in (validarSenha(senha, confirmacao) or validarLogin(login)):
            addUsuario(login, senha)
            return redirect(url_for('usuario.index'))
        else:
            return "Erro no cadastro."
    return render_template('cadastrar.html')

@usuarios_controller.route('/logout')
def logout():
    session.pop('login', None)
    return redirect(url_for(index))
