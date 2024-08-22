import java.util.Scanner;

public class VerificaFolhas {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Leitura dos valores de entrada
        System.out.print("Digite o número de competidores, a quantidade de folhas compradas e as folhas por competidor (separados por espaço): ");
        int C = scanner.nextInt();
        int P = scanner.nextInt();
        int F = scanner.nextInt();

        // Verifica se as entradas estão dentro dos limites especificados
        if (1 <= C && C <= 1000 && 1 <= P && P <= 1000 && 1 <= F && F <= 1000) {
            // Calcula se a quantidade de folhas é suficiente
            if (C * F <= P) {
                System.out.println("S");
            } else {
                System.out.println("N");
            }
        } else {
            System.out.println("Entrada inválida");
        }

        scanner.close();
    }
}
