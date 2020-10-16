#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main () {
    int i, a, m, d;

    scanf("%d", &i);

    a = i / 365;
    i = i % 365;
    m = i / 30;
    i = i % 30;
    d = i;
    
    printf("%d ano(s)\n%d mes(es)\n%d dia(s)\n", a, m, d);

    return 0;
}