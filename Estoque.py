from Carro import Carro


class Estoque:
    def __init__(self):
        self.__carros = []  # Inicializa a lista de carros vazia

    def adicionar_carro(self, carro):
        self.__carros.append(carro)
        print(f"Carro {carro.get_marca()} {carro.get_modelo()} adicionado ao estoque.")

    def remover_carro(self, carro):
        if carro in self.__carros:
            self.__carros.remove(carro)
            print(f"Carro {carro.get_marca()} {carro.get_modelo()} removido do estoque.")
        else:
            print("Carro não encontrado no estoque.")

    def listar_carros(self):
        if self.__carros:
            print("Carros no estoque:")
            for carro in self.__carros:
                print(f"{carro.get_marca()} {carro.get_modelo()}")
        else:
            print("Estoque vazio.")

    def total_carros(self):
        return len(self.__carros)


# Exemplo de uso da classe Estoque
estoque = Estoque()

carro1 = Carro("Toyota", "Corolla", 2020, "Preto", 50000)
carro2 = Carro("Honda", "Civic", 2019, "Prata", 45000)

estoque.adicionar_carro(carro1)
estoque.adicionar_carro(carro2)

estoque.listar_carros()
print("Total de carros:", estoque.total_carros())

estoque.remover_carro(carro1)

estoque.listar_carros()
print("Total de carros:", estoque.total_carros())
