#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int formaTriangulo(double a, double b, double c) {
    if (a + b > c && a + c > b && b + c > a) 
        return 1;
    return 0;
}

int main() {
    double a, b, c;
    scanf("%lf %lf %lf", &a, &b, &c);
    if (formaTriangulo(a, b, c))
        printf("Perimetro = %.1lf\n", (a+b+c));
    else
        printf("Area = %.1lf\n", (a+b)*(c/2));
    return 0;

}