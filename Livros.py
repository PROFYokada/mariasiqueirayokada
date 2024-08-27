class Livro:
    def __init__(self, titulo, autor, ano_publicacao, preco):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao
        self.__preco = preco

# Getter para titulo
    def get_titulo(self):
        return self.__titulo

# Setter para titulo
    def set_titulo(self, novo_titulo):
        self.__titulo = novo_titulo

# Getter para autor
    def get_autor(self):
        return self.__autor

# Setter para autor
    def set_autor(self, novo_autor):
        self.__autor = novo_autor

# Getter para ano de publicação
    def get_ano_publicacao(self):
        return self.__ano_publicacao

# Setter para ano de publicação
    def set_ano_publicacao(self, novo_ano_publicacao):
        self.__ano_publicacao = novo_ano_publicacao

 # Getter para preço
    def get_preco(self):
        return self.__preco

# Setter para preço
    def set_preco(self, novo_preco):
        self.__preco = novo_preco

#Teste dos métodos
#Aqui está um exemplo de como você pode testar os métodos implementados:

# Criando uma instância de Livro
meu_livro = Livro("1984", "George Orwell", 1949, 40.00)

# Acessando os atributos através dos getters
print("Título:", meu_livro.get_titulo())
print("Autor:", meu_livro.get_autor())
print("Ano de Publicação:", meu_livro.get_ano_publicacao())
print("Preço:", meu_livro.get_preco())

# Modificando os atributos através dos setters
meu_livro.set_titulo("A Revolução dos Bichos")
meu_livro.set_autor("George Orwell")
meu_livro.set_ano_publicacao(1945)
meu_livro.set_preco(35.00)

# Acessando os atributos modificados
print("\nApós as modificações:")
print("Título:", meu_livro.get_titulo())
print("Autor:", meu_livro.get_autor())
print("Ano de Publicação:", meu_livro.get_ano_publicacao())
print("Preço:", meu_livro.get_preco())
