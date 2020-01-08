import java.io.IOException;
import java.util.Scanner;

public class URI1007 {

    public static void main(String[] args) throws IOException {
        Scanner read = new Scanner(System.in);
        int a = read.nextInt();
        int b = read.nextInt();
        int c = read.nextInt();
        int d = read.nextInt();
        int dif = (a*b - c*d);
        System.out.println("DIFERENCA = "+dif);
    }
}
