def calcular_cliques_primeiro_link(p):
    # Verificando se t está no intervalo válido
    if 1 <= p <= 1000:
        return 4 * p
    else:
        return "Entrada inválida"

# Teste do programa
p = int(input("Digite o número de pessoas que clicaram no terceiro link: "))
resultado = calcular_cliques_primeiro_link(p)
print(resultado)
