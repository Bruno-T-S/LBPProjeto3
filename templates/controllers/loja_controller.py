from flask import Blueprint, render_template, request, redirect, url_for, session, flash, abort, make_response
import json
from models.usuario_model import usuarios
from models.produto_model import produtos

loja_controller = Blueprint('loja', __name__)

@loja_controller.route('/loja')
def loja():
    if 'login' in session:
        user_id = session.get('id')
        if user_id is None:
            abort(403)

        cookie_data = request.cookies.get('carrinho', '{}')
        
        try:
            cookie_data = json.loads(cookie_data)
        except json.JSONDecodeError:
            cookie_data = {}

        if not isinstance(cookie_data, dict):
            cookie_data = {}

        if cookie_data.get('usuario_id') != user_id:
            cookie_data = {'usuario_id': user_id, 'carrinho': {}}

        id = request.args.get('id', default=0, type=int)

        if id > 0:
            if str(id) in cookie_data.get('carrinho', {}):
                cookie_data['carrinho'][str(id)] += 1
            else:
                cookie_data['carrinho'][str(id)] = 1
        elif id == -1:  
            cookie_data['carrinho'] = {}

        carrinho_produtos = []
        total = 0.0
        for prod_id, quantidade in cookie_data.get('carrinho', {}).items():
            produto = next((p for p in produtos if p.id == int(prod_id)), None)
            if produto:
                subtotal = produto.preco * quantidade
                total += subtotal
                carrinho_produtos.append({
                    'produto': produto,
                    'quantidade': quantidade,
                    'subtotal': subtotal
                })

        resp = make_response(render_template("loja.html", produtos=produtos, carrinho=carrinho_produtos, total=total, usuario=session['login']))
        cookie_data['usuario_id'] = user_id  
        resp.set_cookie('carrinho', json.dumps(cookie_data), max_age=60*60*24)
        return resp

    abort(403)

@loja_controller.route('/loja/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        usuario_login = request.form.get('usuario')
        for usuario in usuarios:
            if usuario.login == usuario_login:
                usuario.admin = True
                flash(f"Elevação do usuário {usuario_login} realizada com sucesso!", "success")
                break
        
        return redirect(url_for('loja.admin'))  

    if 'login' in session and any(usuario.login == session['login'] and usuario.admin for usuario in usuarios):
        return render_template('paineladmin.html', usuarios=usuarios)
    abort(403)
