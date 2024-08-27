# -*- coding: UTF-8 -*-
class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.curtidas = 0

    def imprimir(self):
        print("Nome: %s, Telefone: %s, Empresa: %s" % (self.nome, self.telefone, self.empresa))

perfil = Perfil('Flávio Almeida', 'não informado', 'Caelum')
perfil.curtidas

perfil.curtidas = 1000
print(perfil.curtidas)