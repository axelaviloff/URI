import java.io.IOException;
import java.util.Scanner;

public class URI1002 {

    public static void main(String[] args) throws IOException {
        Scanner read = new Scanner(System.in);
        double raio = read.nextDouble();
        double pi = 3.14159;
        double area = pi * Math.pow(raio, 2);
        System.out.printf("A=%.4f", area);
        System.out.println();

    }
}