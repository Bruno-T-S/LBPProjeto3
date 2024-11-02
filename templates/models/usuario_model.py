class Usuario:
    def __init__(self, id, login, senha, admin):
        self.id = id
        self.login = login
        self.senha = senha
        self.admin = admin
usuarios = []

def addUsuario(login, senha, admin=False):
    for usuario in usuarios:
        if usuario.login == login:
            return False
    id = len(usuarios)
    usuarios.append(Usuario(id, login, senha, admin))
    return True  

addUsuario("adm", "senha", True)