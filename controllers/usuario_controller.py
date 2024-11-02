from models.usuario_model import usuarios, addUsuario
from models.cadastro_model import *
import json
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, make_response, abort
usuarios_controller = Blueprint('usuario', __name__)

@usuarios_controller.route('/')
def index():
    if 'login' in session:  
        return redirect(url_for('loja.loja')) 
    return render_template('home.html')  



@usuarios_controller.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        login = request.form.get('login')
        senha = request.form.get('senha')
        for usuario in usuarios:
            if login == usuario.login and senha == usuario.senha:
                session['login'] = login
                session['admin'] = usuario.admin
                session['id'] = usuario.id 

                cookie_data = json.loads(request.cookies.get('carrinho', '{}'))
                if not (isinstance(cookie_data, dict) and cookie_data.get('usuario_id') == usuario.id):
                    cookie_data = {'usuario_id': usuario.id, 'carrinho': {}}


                resp = make_response(redirect(url_for('loja.loja')))
                resp.set_cookie('carrinho', json.dumps(cookie_data), max_age=60*60*24)
                return resp

        flash("Usuário ou senha incorreto(s) ou usuário inexistente.", "error")
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
        session['admin'] = False  
        session['id'] = usuarios[-1].id  
        session['carrinho'] = {}
        
        response = redirect(url_for('usuario.index'))
        response.set_cookie('login', login)
        return response

    return render_template('cadastrar.html')

@usuarios_controller.route('/logout')
def logout():
    if 'login' in session:  
        session['carrinho'] = request.cookies.get('carrinho')
        session.pop('login', None)
        session.pop('admin', None)
        session.pop('id', None) 
        response = redirect(url_for('usuario.index'))
        response.delete_cookie('login')
        return response
    abort(403)