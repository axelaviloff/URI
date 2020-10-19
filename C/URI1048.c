#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    double salario, reajuste;
    int pct;
    scanf("%lf", &salario);

    if (salario <= 400) {
        reajuste = salario * 0.15;
        salario += reajuste;
        pct = 15;
    } else if ( salario <= 800) {
        reajuste = salario * 0.12;
        salario += reajuste;
        pct = 12;
    } else if (salario <= 1200) {
        reajuste = salario * 0.10;
        salario += reajuste;
        pct = 10;
    } else if (salario <= 2000) {
        reajuste = salario * 0.07;
        salario += reajuste;
        pct = 7;
    } else {
        reajuste = salario * 0.04;
        salario += reajuste;
        pct = 4;
    }

    printf("Novo salario: %.2lf\n", salario);
    printf("Reajuste ganho: %.2lf\n", reajuste);
    printf("Em percentual: %d %\n", pct);



    return 0;
}