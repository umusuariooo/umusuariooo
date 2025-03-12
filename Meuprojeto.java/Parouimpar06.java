import java.util.Scanner;

public class Parouimpar06 {
    
    public static void main(String[] args) {
        // Criando um Scanner para ler o númeor do usuário
        Scanner scanner = new Scanner(System.in);

        // Solicitar ao usuário que digite um número
        System.out.println("Por favor Digite um Númeor: ");
        int numero = scanner.nextInt();

        // Verificando se o número é par ou ímpa
        if (numero % 2 == 0) {
            System.out.println("O número " + numero + " é PAR.");
        } else {
            System.out.println("O número " + numero + " é ÍMPAR.");
        }

        // Fechar o scanner
        scanner.close();
    }
}