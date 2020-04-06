#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main () {
    int valor, valorPrint; 
    int nota100 = 0, nota50 = 0, nota20 = 0, nota10 = 0, nota5 = 0, nota2 = 0, nota1 = 0;
    cin >> valor;
    valorPrint = valor;
    while (valor > 0) { 
        if (valor >= 100) {
            nota100 += 1;
            valor -= 100;
        } else if (valor >= 50) {
            nota50 += 1;
            valor -= 50;
        } else if (valor >= 20) {
            nota20 += 1;
            valor -= 20;
        } else if (valor >= 10) {
            nota10 += 1;
            valor -= 10;
        } else if (valor >= 5) {
            nota5 += 1;
            valor -= 5;
        } else if (valor >= 2) {
            nota2 += 1;
            valor -= 2;
        } else {
            nota1 += valor;
            valor = 0;
        }
      } 
    cout << valorPrint << endl;
    cout << nota100 << " nota(s) de R$ 100,00" << endl;
    cout << nota50 << " nota(s) de R$ 50,00" << endl;
    cout << nota20 << " nota(s) de R$ 20,00" << endl;
    cout << nota10 << " nota(s) de R$ 10,00" << endl;
    cout << nota5 << " nota(s) de R$ 5,00" << endl;
    cout << nota2 << " nota(s) de R$ 2,00" << endl;
    cout << nota1 << " nota(s) de R$ 1,00" << endl;

}
