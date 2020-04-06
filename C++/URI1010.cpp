#include <iostream>
#include <iomanip>
using namespace std;

int main () {
    int cd1, cd2, qtd1, qtd2;
    double vl1, vl2;
    cin >> cd1 >> qtd1 >> vl1;
    cin >> cd2 >> qtd2 >> vl2;

    cout << fixed << setprecision(2) << "VALOR A PAGAR: R$ " << (qtd1*vl1 + qtd2*vl2) << endl;

}

