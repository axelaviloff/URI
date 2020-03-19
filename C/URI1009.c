#include <stdio.h>
#include <stdlib.h>

int main () {

    char nomeVendedor[] = "";
    double salarioFixo, totalVendas, salarioTotal;

    scanf("%s %lf %lf", nomeVendedor, &salarioFixo, &totalVendas);

    salarioTotal = salarioFixo + totalVendas * 0.15;

    printf("TOTAL = R$ %.2lf\n", salarioTotal);

    return 0;
}