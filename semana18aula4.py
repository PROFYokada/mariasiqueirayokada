# Leitura dos valores de entrada
C, P, F = map(int, input("Digite o número de competidores, a quantidade de folhas compradas e as folhas por competidor (separados por espaço): ").split())

# Verifica se as entradas estão dentro dos limites especificados
if 1 <= C <= 1000 and 1 <= P <= 1000 and 1 <= F <= 1000:
    # Calcula se a quantidade de folhas é suficiente
    if C * F <= P:
        print("S")
    else:
        print("N")
else:
    print("Entrada inválida")

