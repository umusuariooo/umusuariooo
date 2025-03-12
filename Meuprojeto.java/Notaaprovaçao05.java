import java.util.Scanner;

public class Notaaprovaçao05 {
   
    public static void main(String[] args) {
        // Criando o Scanner para ler as entradas do usuario
        Scanner entrada = new Scanner(System.in);

        // Declaração das variaveis
        double nota1, nota2;

        // Entrada de dados
        System.out.println("Digite a primeira nota:");
        nota1 = entrada.nextDouble();

        System.out.println("Digite a segunda nota:");
        nota2 = entrada.nextDouble();

        // Calculo da média
        double media = (nota1 + nota2) / 2;

        // Exibindo a media
        System.out.println("A média é: " + media);

        // Processamento de aprovação
        boolean aprovado = (media >= 7);

        // Verificando se o aluno foi aprovado
        if (aprovado) {
            System.out.println("VOCÊ FOI APROVADO");
        } else {
            System.out.println("VOCÊ FOI REPROVADO");
        }

        // Fechando o Scanner
        entrada.close();
    }
}
