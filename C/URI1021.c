#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main () {
    
int dinheiro1, cem, cinquenta, vinte, dez, cinco, dois;

int moedas, um, um1, cinquentac, vintec, dezc, cincoc, umc;

double dinheiro;

scanf("%lf", &dinheiro);

dinheiro1 = (int)dinheiro;
dinheiro -= dinheiro1;
moedas = (dinheiro *100);

cem = dinheiro1 / 100;
dinheiro1 = dinheiro1 %100;
cinquenta = dinheiro1 / 50;
dinheiro1 = dinheiro1 % 50;
vinte = dinheiro1 / 20;
dinheiro1 = dinheiro1 % 20;
dez = dinheiro1 / 10;
dinheiro1 = dinheiro1 % 10;
cinco = dinheiro1/5;
dinheiro1 = dinheiro1 % 5;
dois = dinheiro1 / 2;
dinheiro1 = dinheiro1 % 2;
um = dinheiro1 / 1;

printf("NOTAS:\n");
printf("%d nota(s) de R$ 100.00\n",cem);
printf("%d nota(s) de R$ 50.00\n",cinquenta);
printf("%d nota(s) de R$ 20.00\n",vinte);
printf("%d nota(s) de R$ 10.00\n",dez);
printf("%d nota(s) de R$ 5.00\n",cinco);
printf("%d nota(s) de R$ 2.00\n",dois);

cinquentac = moedas / 50;
moedas = moedas % 50;
vintec = moedas / 25;
moedas = moedas % 25;
dezc = moedas / 10;
moedas = moedas % 10;
cincoc = moedas / 5;
moedas = moedas % 5;
umc = moedas / 1;

printf("MOEDAS:\n");
printf("%d moeda(s) de R$ 1.00\n", um);
printf("%d moeda(s) de R$ 0.50\n", cinquentac);
printf("%d moeda(s) de R$ 0.25\n", vintec);
printf("%d moeda(s) de R$ 0.10\n", dezc);
printf("%d moeda(s) de R$ 0.05\n", cincoc);
printf("%d moeda(s) de R$ 0.01\n", umc);
    
    return 0;
}