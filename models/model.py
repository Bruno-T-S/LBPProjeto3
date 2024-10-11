class Usuario:
    def __init__(self, id, usuario, senha):
        self.id = id
        self.usuario = usuario
        self.senha = senha

lista_usuarios = []

def addUsuario(usuario, senha):
    id = len(lista_usuarios) + 1
    lista_usuarios.append(Usuario(id, usuario, senha))
