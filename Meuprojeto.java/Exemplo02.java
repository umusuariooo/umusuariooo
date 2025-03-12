public class Exemplo02 {
    
    public static void main(String[] args) {
        System.out.println();
        System.out.println( 10 > 5); // 10 > 5 é verdadeiro = True
        System.out.println( 10 < 5); // 10 < 5 é falso = false
        System.out.println( 10 >= 5); // Maior ou igula a 10 = verdadeiro
        System.out.println( 10 != 5); //Warning - // (!= Diferentede) Verdadeiro = True

        System.out.println();
        System.out.println(5 + 2 > 7 - 2 * 2); // Resolver as operações matemáticas respeitando a precedência de operadores:
        System.out.println((5 + 2) > (7 - (2 * 2)));// Essa linha é praticamente a mesma da anterior, mas com parênteses adicionais para deixar a ordem das operações explícita.
    }


}