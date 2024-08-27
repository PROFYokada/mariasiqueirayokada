class Carro:
    def __init__(self, marca, modelo, ano, cor, preco):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor
        self.__preco = preco

    def get_marca(self):
        return self.__marca

    def set_marca(self, nova_marca):
        self.__marca = nova_marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    def get_ano(self):
        return self.__ano

    def set_ano(self, novo_ano):
        self.__ano = novo_ano

    def get_cor(self):
        return self.__cor

    def set_cor(self, nova_cor):
        self.__cor = nova_cor

    def get_preco(self):
        return self.__preco

    def set_preco(self, novo_preco):
        self.__preco = novo_preco


# Exemplo de uso da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020, "Preto", 50000)

# Obtendo os valores dos atributos
print("Marca:", meu_carro.get_marca())
print("Modelo:", meu_carro.get_modelo())
print("Ano:", meu_carro.get_ano())
print("Cor:", meu_carro.get_cor())
print("Preço:", meu_carro.get_preco())

# Alterando valores dos atributos
meu_carro.set_modelo("Camry")
meu_carro.set_ano(2021)
meu_carro.set_cor("Branco")
meu_carro.set_preco(55000)

# Verificando as alterações
print("Novo modelo:", meu_carro.get_modelo())
print("Novo ano:", meu_carro.get_ano())
print("Nova cor:", meu_carro.get_cor())
print("Novo preço:", meu_carro.get_preco())
