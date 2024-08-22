import java.util.Scanner;

public class TreinamentoLeonardo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Leitura dos valores de entrada
        System.out.print("Digite o número de metros que Leonardo pretende correr e o comprimento da pista (separados por espaço): ");
        int C = scanner.nextInt();
        int N = scanner.nextInt();

        // Verifica se as entradas estão dentro dos limites especificados
        if (1 <= C && C <= 1e8 && 1 <= N && N <= 100) {
            int pontoTermino = C % N;
            System.out.println("Ponto de término do treinamento: " + pontoTermino);
        } else {
            System.out.println("Entrada inválida");
        }

        scanner.close();
    }
}
