import java.io.IOException;
import java.util.Scanner;

public class URI1004 {

    public static void main(String[] args) throws IOException {
        Scanner read = new Scanner(System.in);
        int a = read.nextInt();
        int b = read.nextInt();
        int soma = a * b;
        System.out.println("PROD = "+soma);
    }
}
