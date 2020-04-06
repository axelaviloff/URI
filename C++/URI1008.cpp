#include <iostream>
#include <iomanip>
using namespace std;

int main () {
    int n, qtd;
    double valorHora;
    cin >> n;
    cin >> qtd;
    cin >> valorHora;
    cout << "NUMBER = " << n << endl;
    cout << fixed << setprecision(2) << "SALARY = U$ " << valorHora*qtd << endl;
    
}

