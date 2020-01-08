import java.io.IOException;
import java.util.Scanner;

public class URI1008 {

    public static void main(String[] args) throws IOException {
        Scanner read = new Scanner(System.in);
        int n = read.nextInt();
        int h = read.nextInt();
        double s = read.nextDouble();
        System.out.println("NUMBER = "+n);
        System.out.printf("SALARY = U$ %.2f", s*h);
        System.out.println();
    }
}
