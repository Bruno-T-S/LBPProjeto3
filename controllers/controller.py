from flask import Blueprint, render_template, redirect, url_for
from models import model

hello = Blueprint('mensagens', __name__)

@hello.route('/')
def index():
    return render_template('index.html', mensagens=model.mensagens)

@hello.route('/add', methods=['POST'])
def add_mensagem():
    model.add_mensagem()
    return render_template('index.html', mensagens=model.mensagens)
