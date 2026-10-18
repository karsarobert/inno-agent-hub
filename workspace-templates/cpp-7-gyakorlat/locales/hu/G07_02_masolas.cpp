#include <iostream>
using namespace std;

struct Meres {
    int azonosito;
    double ertek;
    bool ervenyes;
};

// A sajat fuggvenyt a foprogram elott is definialhatod.

int main() {
    Meres eredeti{201, 10.5, true};
    cout << "Kiindulo meres: " << eredeti.azonosito << " "
         << eredeti.ertek << " " << eredeti.ervenyes << '\n';

    // Eloszor fuggvennyel keszits modositott masolatot.
    // Utana mutaton keresztul az eredeti objektumot modositsd.
    return 0;
}
