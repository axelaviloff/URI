#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main () {
    int cod, qtd;
    cin >> cod >> qtd;
    cout << fixed << setprecision(2);
    if (cod == 1)
        cout << "Total: R$ " << 4.00 * qtd << endl;
    else if (cod == 2)
        cout << "Total: R$ " << 4.50 * qtd << endl;
    else if (cod == 3)
        cout << "Total: R$ " << 5.00 * qtd << endl;
    else if (cod == 4)
        cout << "Total: R$ " << 2.00 * qtd << endl;
    else
        cout << "Total: R$ " << 1.50 * qtd << endl;
    
}
