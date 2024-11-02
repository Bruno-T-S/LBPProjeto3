class Produto:
    def __init__(self, id, nome, imagem, preco) -> None:
        self.__id = id
        self.__nome = nome
        self.__imagem = imagem
        self.__preco = preco
    
    def __getattribute__(self, name):
        return super().__getattribute__(f"_Produto__{name}")

produtos = []
def addProduto(nome, imagem, preco):
    id = len(produtos) + 1
    produtos.append(Produto(id, nome, imagem, preco))

addProduto("Notebook Ben 10", "ben10", 450.99)
addProduto("GS4 Pro", "gs4", 1250.99)
addProduto("GS5", "gs5", 3000.99)
addProduto("Controle oficial para Xbox 720", "xbox720", 199.95)
addProduto("Brinquedos autênticos Superheroes", "superheroes", 40.47)