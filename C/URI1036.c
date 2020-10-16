#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    
    double a, b, c, delta, x1, x2;
    scanf ("%lf %lf %lf", &a, &b, &c);

    if (a == 0) {
        printf("Impossivel calcular\n");
    } else {
        delta = (b * b) - (4 * a * c);
        if (delta >= 0) {
            x1 = (-b + sqrt(delta)) / (2 * a);
            x2 = (-b - sqrt(delta)) / (2 * a);
            printf("R1 = %.5lf\nR2 = %.5lf\n", x1, x2);
        } else {
            printf("Impossivel calcular\n");
        }
    }
    return 0;

}