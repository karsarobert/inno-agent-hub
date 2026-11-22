#include <iostream>
using namespace std;

struct Eszkoz { int azonosito; bool aktiv; };
void kikapcsol(Eszkoz* p) {
    // TODO: érvényes és nullmutató kezelése
}

int main() {
    int azonosito, aktiv;
    cin >> azonosito >> aktiv;
    Eszkoz adat{azonosito, aktiv != 0};
    kikapcsol(&adat);
    kikapcsol(nullptr);
    cout << adat.azonosito << " " << adat.aktiv << "\n";
    return 0;
}
