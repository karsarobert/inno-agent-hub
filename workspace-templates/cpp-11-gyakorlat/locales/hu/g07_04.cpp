#include <iostream>
using namespace std;

struct Konyv { int oldalszam; bool kolcsonozheto; };
int szamol(const Konyv adatok[], int n) {
    int darab = 0;
    // TODO: csak a megfelelő rekordok számlálása
    return darab;
}

int main() {
    int n;
    cin >> n;
    Konyv adatok[5]{};
    for (int i = 0; i < n; i++) cin >> adatok[i].oldalszam >> adatok[i].kolcsonozheto;
    cout << szamol(adatok, n) << "\n";
    return 0;
}
