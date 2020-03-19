#include <stdio.h>
#include <stdlib.h>

int main () {

    int numero, horasTrabalhadas;
    double valorHora, valorSalario;

    scanf("%d", &numero);
    scanf("%d", &horasTrabalhadas);
    scanf("%lf", &valorHora);

    valorSalario = horasTrabalhadas * valorHora;

    printf("NUMBER = %d\n", numero);
    printf("SALARY = U$ %.2lf\n", valorSalario);

    return 0;
}