#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main () {
    int valor, horas, minutos, segundos;
    cin >> valor;
    horas = valor / 3600;
    minutos = (valor % 3600) / 60;
    segundos = (valor % 3600) % 60;
    cout << horas << ":" << minutos << ":" << segundos << endl;
     


}
