#include <iostream>
using namespace std;

struct KetSzam { int egesz; double tort; };
union Szam { int egesz; double tort; };

int main() {
    char tipus;
    cin >> tipus;
    Szam adat{};
    if (tipus == 'I') cin >> adat.egesz;
    else cin >> adat.tort;
    // TODO: csak az aktív mező kiírása
    cout << sizeof(KetSzam) << " " << sizeof(Szam) << " " << sizeof(int) << " " << sizeof(double) << "\n";
    return 0;
}
