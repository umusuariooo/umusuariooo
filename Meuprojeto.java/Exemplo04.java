import java.util.Scanner;

public class Exemplo04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero; // declara uma variavel do tipo inteiro, chamada 'numero'
        int dobro;

        System.out.println("digite um número inteiro");
        numero = entrada.nextInt(); // atribuição. guarda o valor dentro da variavel

        dobro = numero * 2;

        System.out.println("voce digitou " + numero);
        System.out.println("O dobro é " + dobro);
        entrada.close();
    }
}