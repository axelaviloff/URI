#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main () {
    int valor, anos, meses, dias;
    cin >> valor;
    anos = valor / 365;
    meses = (valor % 365) / 30;
    dias = (valor % 365) % 30;
    
    cout << anos << " ano(s)" << endl;
    cout << meses << " mes(es)" << endl;
    cout << dias << " dia(s)" << endl;
     


}
