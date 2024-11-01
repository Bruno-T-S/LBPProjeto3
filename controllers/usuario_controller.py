from models.usuario_model import usuarios, addUsuario
from controllers.cadastro_controller import *
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, abort
usuarios_controller = Blueprint('usuario', __name__)

@usuarios_controller.route('/')
def index():
    if 'login' in session:  
        return redirect(url_for('usuario.dashboard')) 
    return render_template('home.html')  


@usuarios_controller.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        login = request.form.get('login')
        senha = request.form.get('senha')
        for usuario in usuarios:
            if login == usuario.login and senha == usuario.senha:
                session['login'] = login
                return redirect(url_for('usuario.dashboard'))
        flash("Usuário ou senha incorreto(s).", "error")
        return redirect(url_for('usuario.login'))
    return render_template('login.html')

@usuarios_controller.route("/cadastrar", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        login = request.form.get('login')
        senha = request.form.get('senha')
        confirmacao = request.form.get('confirmacao')
        if False in (validarSenha(senha, confirmacao)) or False in (validarLogin(login)):
            flash("Erro no cadastro. O login não pode ser vazio e menor que três caracteres. A senha deve ter: caractere maiúsculo; número; caractere especial; senha e confirmação devem ser iguais; o tamanho deve ser entre 8 e 64 caracteres; não pode ser vazia.", "error")
            return redirect(url_for('usuario.add')) 
        if (not(addUsuario(login, senha))):
            flash("O nome de usuário já existe.", "error")
            return redirect(url_for('usuario.add'))
        session['login'] = login
        response = redirect(url_for('usuario.index'))
        response.set_cookie('login', login)
        flash("Cadastro bem-sucedido!", "success")
        return response

    return render_template('cadastrar.html')

@usuarios_controller.route('/logout')
def logout():
    session.pop('login', None)
    response = redirect(url_for('usuario.index'))
    response.delete_cookie('login')
    return response

@usuarios_controller.route('/dashboard')
def dashboard():
    if 'login' in session:
        return render_template('dashboard.html', usuario=session['login'])
    else:
        abort(403)
    return redirect(url_for('usuario.login'))