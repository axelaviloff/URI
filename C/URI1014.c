#include <stdio.h>
#include <stdlib.h>

int main () {
    int x;
    double c, r;
    scanf("%d", &x);
    scanf("%lf", &c);
    r = x/c;
    printf("%.3lf km/l\n", r);
    
    
    return 0;
}