from flask import Flask
from controllers.usuario_controller import usuarios_controller

app = Flask(__name__)
app.register_blueprint(usuarios_controller)

if __name__ == '__main__':
    app.run(debug=True)


