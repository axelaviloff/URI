#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main () {
    double n;
    cin >> n;
    if (n <= 100 && n >=0) {
        if (n >= 0 && n <= 25) {
            cout << "Intervalo [0,25]" << endl;
        } else if (n > 25 && n <= 50) {
            cout << "Intervalo (25,50]" << endl;
        } else if (n > 50 && n <= 75) {
            cout << "Intervalo (50,75]" << endl;
        } else {
            cout << "Intervalo (75,100]" << endl;
        }
        
    } else {
      cout << "Fora de intervalo" << endl;  
    }


}
