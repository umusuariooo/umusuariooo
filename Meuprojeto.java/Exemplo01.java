public class Exemplo01 {

    public static void main(String[] args) {
        System.out.println();
        System.out.println("Resultado = " + 13 + 2); // Vai juntar os numeros inves de somar = 132
        System.out.println("Resultado = " + (13 + 2)); // Vai realmente somar os numoeros por conta das () = 15
        System.out.println("Resultado = " + (13 / 2)); // Vai dividir os numeros, mas de forma inteira = 6 / que no caso era para ser 6.5
        System.out.println("Resultado = " + (13 % 2)); // O simbolo de % vai fornecer o resto da divisao = 1
        System.out.println("Resultado = " + (13.0 / 2)); // Adicionando um .0 e a barra de divisao o codigo ira entender que vai sair um numero "quebrado" = 6.5

    }
}