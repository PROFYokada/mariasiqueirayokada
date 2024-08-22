# Leitura dos valores de entrada
C, N = map(int, input("Digite o número de metros que Leonardo pretende correr e o comprimento da pista (separados por espaço): ").split())

# Verifica se as entradas estão dentro dos limites especificados
if 1 <= C <= 1e8 and 1 <= N <= 100:
    ponto_termino = C % N
    print("Ponto de término do treinamento:", ponto_termino)
else:
    print("Entrada inválida")