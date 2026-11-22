#include <iostream>
#include <sstream>
#include <string>
using namespace std;

bool egeszToken(const string& szoveg, int* eredmeny) {
    istringstream proba(szoveg);
    int ideiglenes;
    if (!(proba >> ideiglenes)) return false;
    proba >> ws;
    if (!proba.eof()) return false;
    *eredmeny = ideiglenes;
    return true;
}

bool sorEllenoriz(const string& sor, int* kod, int* darab) {
    istringstream reszek(sor);
    string kodSzoveg, darabSzoveg, plusz;
    int k, d;
    // TODO 1: pontosan két token szükséges
    if (!egeszToken(kodSzoveg, &k) || !egeszToken(darabSzoveg, &d)) return false;
    // TODO 2: tartományellenőrzés
    *kod = k;
    *darab = d;
    return true;
}

int main() {
    string sor;
    getline(cin, sor);
    int kod = 77, darab = 88;
    bool siker = sorEllenoriz(sor, &kod, &darab);
    cout << siker << " " << kod << " " << darab << "\n";
    return 0;
}
