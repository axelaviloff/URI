#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int saoMultiplos(int a, int b) {
    if (a % b == 0 || b % a == 0) 
        return 1;
    return 0;
}

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    if (saoMultiplos(a, b))
        printf("Sao Multiplos\n");
    else
        printf("Nao sao Multiplos\n");
    return 0;

}