from flask import Flask, render_template, flash, redirect, url_for, session, request, abort
from controllers.usuario_controller import usuarios_controller
from controllers.loja_controller import loja_controller

app = Flask(__name__)
app.secret_key = "ChaveSegura"
app.static_folder = 'static'

app.register_blueprint(usuarios_controller)
app.register_blueprint(loja_controller)

@app.before_request
def require_login():
    if request.path.startswith('/static/'):
        return  
    rotas_publicas = ['usuario.login', 'usuario.add', 'usuario.index', 'usuario.cadastrar']
    rotas_privadas = ['loja.loja', 'loja.admin', 'usuario.logout']
    if request.endpoint not in rotas_publicas and request.endpoint not in rotas_privadas:
        return abort(404) 
    if 'login' not in session and request.endpoint not in rotas_publicas:
        return abort(403)

@app.errorhandler(404)
def pageNotFound(e):
    return render_template("404.html"), 404

@app.errorhandler(403)
def pageNotFound(e):
    return render_template("403.html"), 403

@app.errorhandler(401)
def pageNotFound(e):
    return render_template("401.html"), 401

@app.errorhandler(500)
def pageNotFound(e):
    return render_template("500.html"), 500

if __name__ == '__main__':
    app.run(debug=True)


