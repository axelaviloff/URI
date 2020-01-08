import java.io.IOException;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Scanner;

public class URI1009 {

    public static void main(String[] args) throws IOException {
        Scanner read = new Scanner(System.in);
        String nome = read.nextLine();
        double s = read.nextDouble();
        double m = read.nextDouble();
        BigDecimal resultado = new BigDecimal((s) + (m * 0.15)).setScale(2, RoundingMode.HALF_DOWN);
        System.out.print("TOTAL = R$ " + resultado + "\n");
    }
}
