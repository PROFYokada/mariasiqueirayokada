import java.util.Scanner;

public class CalcularDistancia {
    public static int calcularDistancia(int t, int v) {
        if (1 <= t && t <= 100 && 0 <= v && v <= 120) {
            return t * v;
        } else if (t == 0 && v == 0) {
            return 0;
        } else {
            return -1; // Indica entrada inválida
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Leitura dos intervalos
        System.out.print("Digite o tempo e a velocidade para o intervalo 1 (separados por espaço): ");
        int T1 = scanner.nextInt();
        int V1 = scanner.nextInt();

        System.out.print("Digite o tempo e a velocidade para o intervalo 2 (separados por espaço): ");
        int T2 = scanner.nextInt();
        int V2 = scanner.nextInt();

        System.out.print("Digite o tempo e a velocidade para o intervalo 3 (separados por espaço): ");
        int T3 = scanner.nextInt();
        int V3 = scanner.nextInt();

        // Cálculo das distâncias para cada intervalo
        int distancia1 = calcularDistancia(T1, V1);
        int distancia2 = calcularDistancia(T2, V2);
        int distancia3 = calcularDistancia(T3, V3);

        // Verificação de entradas inválidas
        if (distancia1 == -1 || distancia2 == -1 || distancia3 == -1) {
            System.out.println("Entrada inválida");
        } else {
            int distanciaTotal = distancia1 + distancia2 + distancia3;
            System.out.println("Distância total percorrida: " + distanciaTotal);
        }

        scanner.close();
    }
}
