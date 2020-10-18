#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    int i, f, t;
    scanf("%d %d", &i, &f);
    if (f > i)
        t = f - i;
    else if (f <= i)
        t = 24 - (i - f);
    
    printf("O JOGO DUROU %d HORA(S)\n", t);
    return 0;

}