#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    int horaInicio, horaFinal, minutoInicio, minutoFinal, tempoHoraTotal, tempoMinutoTotal;
    
    scanf("%d %d %d %d", &horaInicio, &minutoInicio, &horaFinal, &minutoFinal);

    tempoHoraTotal = horaFinal - horaInicio;
    tempoMinutoTotal = minutoFinal - minutoInicio;
    
    if (tempoHoraTotal <= 0 && tempoMinutoTotal <= 0) {
        tempoHoraTotal += 24;
    }
    if (tempoMinutoTotal < 0) {
        tempoMinutoTotal += 60;
        tempoHoraTotal--;
    }
    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", tempoHoraTotal, tempoMinutoTotal);
    
    return 0;

}