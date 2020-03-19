#include <stdio.h>
#include <stdlib.h>

int main() {
    
    int codigo, quantidade;
    float conta;

    scanf("%i %i", &codigo, &quantidade);

    if (codigo == 1)
        conta = 4.00 * quantidade;
    
    if (codigo == 2)
        conta = 4.50 * quantidade;

    if (codigo == 3)
        conta = 5.00 * quantidade;

    if (codigo == 4)
        conta = 2.00 * quantidade;

    if (codigo == 5)
        conta = 1.50 * quantidade;

    printf("Total: R$ %.2f\n", conta);

    return 0;

}