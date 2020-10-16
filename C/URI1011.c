#include <stdio.h>
#include <stdlib.h>

int main () {
    double r, volume;
    
    scanf("%lf", &r);
    
    volume = (r * r * r) * 3.14159 * (4.0/3);
    
    printf("VOLUME = %.3lf\n", volume);
    
    return 0;
}