#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main () {
    int t, v;
    scanf("%d", &t);
    scanf("%d", &v);
    
    printf("%.3lf\n", (t*v)/12.0);
    
    return 0;
}