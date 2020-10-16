#include <stdio.h>
#include <stdlib.h>

int main () {
    int cp1, np1, cp2, np2;
    double vp1, vp2;
    scanf("%d %d %lf", &cp1, &np1, &vp1);
    scanf("%d %d %lf", &cp2, &np2, &vp2);
    printf("VALOR A PAGAR: R$ %.2lf\n", np1 * vp1 + np2 * vp2);
    return 0;
}