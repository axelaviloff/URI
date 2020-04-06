#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main () {
    int tempoGasto, velMedia;
    double distancia;
    cin >> tempoGasto >> velMedia;
    distancia = tempoGasto*velMedia;
    cout << fixed << setprecision(3) << distancia/12 << endl;

}
