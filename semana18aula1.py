def calcular_cliques_primeiro_link(t):
    # Verificando se t está no intervalo válido
    if 1 <= t <= 1000:
        return 4 * t
    else:
        return "Entrada inválida"

# Teste do programa
t = int(input("Digite o número de pessoas que clicaram no terceiro link: "))
resultado = calcular_cliques_primeiro_link(t)
print(resultado)
