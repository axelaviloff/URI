#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void ordenaValores(int a, int b, int c) {
    int aux;
    if (c < b) {
        aux = b;
        b = c;
        c = aux;
    }
    if (c < a) {
        aux = a;
        a = c;
        c = aux;
    }
    if (b < a) {
        aux = a;
        a = b;
        b = aux;
    }
    printf("%d\n%d\n%d\n", a, b, c);
}

int main() {
    
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    ordenaValores(a, b, c);
    printf("\n%d\n%d\n%d\n", a, b, c);
    
    return 0;

}