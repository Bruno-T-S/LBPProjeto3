class Usuario:
    def __init__(self, id, login, senha):
        self.id = id
        self.login = login
        self.senha = senha

usuarios = []

def addUsuario(login, senha):
    for usuario in usuarios:
        if usuario.login == login:
            return False
    id = len(usuarios) + 1
    usuarios.append(Usuario(id, login, senha))
    return True  
