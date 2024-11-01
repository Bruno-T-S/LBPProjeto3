import string
maiusculas = list(string.ascii_uppercase)
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
especiais = list(string.punctuation)
def validarSenha(senha, senha_validacao, maiusculas=maiusculas, numeros=numeros, especiais=especiais):
    tem_maiuscula = False
    tem_numero = False
    tem_especial = False
    igual_validacao = False
    tamanho_correto = False
    nao_vazio = True

    if senha == "" or senha_validacao == "":
        nao_vazio = False
    if senha == senha_validacao:
        igual_validacao = True

    if len(senha) >= 8 and len(senha) <=64:
        tamanho_correto = True
    for char in senha:
        if char in maiusculas:
            tem_maiuscula = True
        if char in numeros:
            tem_numero = True
        if char in especiais:
            tem_especial = True

    return nao_vazio, tamanho_correto, igual_validacao, tem_maiuscula, tem_numero, tem_especial
def validarLogin(nome):
    nao_vazio = True
    tamanho = False
    if nome == "":
        nao_vazio = False
    if len(nome) >= 3:
        tamanho = True
    return nao_vazio, tamanho

