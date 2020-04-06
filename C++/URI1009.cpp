#include <iostream>
#include <iomanip>
using namespace std;

int main () {
    string nome;
    double salarioFixo, montante;
    cin >> nome;
    cin >> salarioFixo;
    cin >> montante;

    cout << fixed << setprecision(2) << "TOTAL = R$ " << salarioFixo+(montante*0.15) << endl;

}

