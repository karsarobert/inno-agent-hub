#include <iostream>
using namespace std;

struct Termek { int darab; double egysegar; };

int main() {
    int n, uj;
    cin >> n >> uj;
    Termek eredeti{n, 4.5};
    Termek masolat{}; // TODO 1: másoló inicializálás
    // TODO 2
    cout << eredeti.darab << " " << masolat.darab << "\n";
    return 0;
}
