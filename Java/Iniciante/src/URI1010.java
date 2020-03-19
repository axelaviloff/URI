import java.util.Locale;
import java.util.Scanner;
import java.io.IOException;

public class URI1010 {

    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.US);
        Scanner read = new Scanner(System.in);

        int cod1, cod2, qte1, qte2;
        double preco1, preco2, total;

        cod1 = read.nextInt();
        qte1 = read.nextInt();
        preco1 = read.nextDouble();

        cod2 = read.nextInt();
        qte2 = read.nextInt();
        preco2 = read.nextDouble();

        total = preco1 * qte1 + preco2 * qte2;

        System.out.printf("VALOR A PAGAR: R$ %.2f%n", total);

        read.close();
    }
}