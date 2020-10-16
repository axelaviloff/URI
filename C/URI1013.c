#include <stdio.h>
#include <stdlib.h>

int main () {
    int x, y, z, maiorXY, maiorXYZ;
    scanf("%d %d %d",&x,&y,&z);
    maiorXY = (x + y + abs(x - y))/2;
    maiorXYZ = (maiorXY + z + abs(maiorXY - z))/2;
    printf("%d eh o maior\n", maiorXYZ);
    
    return 0;
}