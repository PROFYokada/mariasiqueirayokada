import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o número de pessoas que clicaram no terceiro link: ");
        int t = scanner.nextInt();
        
        String resultado = calcularCliquesPrimeiroLink(t);
        System.out.println(resultado);
    }
    
}
