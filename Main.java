import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o número de pessoas que clicaram no terceiro link: ");
        int t = scanner.nextInt();
        
        String resultado = calcularCliquesPrimeiroLink(t);
        System.out.println(resultado);
    }
    
    //ma oe comentário adicionado
    public static String calcularCliquesPrimeiroLink(int t) {
        if (1 <= t && t <= 1000) {
            return String.valueOf(4 * t);
        } else {
            return "Entrada inválida";
        }
    }
}
