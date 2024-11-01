from flask import Flask, render_template, flash, redirect, url_for, session, request
from controllers.usuario_controller import usuarios_controller

app = Flask(__name__)
app.secret_key = "ChaveSegura"

app.register_blueprint(usuarios_controller)

@app.before_request
def require_login():
    rotas_publicas = ['usuario.login', 'usuario.add', 'usuario.index', 'usuario.cadastrar']
    if 'login' not in session and request.endpoint not in rotas_publicas:
        return redirect(url_for('usuario.index'))
    

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


