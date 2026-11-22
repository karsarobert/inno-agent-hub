#include <iostream>
#include <fstream>
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

struct Lista { int ertekek[2]{}; int elemszam = 0; };
bool ervenyesSzam(const string& sor, int* szam) {
    istringstream reszek(sor);
    string szoveg, plusz;
    if (!(reszek >> szoveg) || (reszek >> plusz)) return false;
    return egeszToken(szoveg, szam) && *szam >= 0 && *szam <= 50;
}
bool betolt(const string& fajlnev, Lista* cel) {
    ifstream bemeno(fajlnev);
    if (!bemeno) return false;
    Lista ideiglenes; // TODO: ezt az ideiglenes objektumot használd
    cel->elemszam = 0;
    string sor;
    while (getline(bemeno, sor)) {
        int szam;
        if (!ervenyesSzam(sor, &szam)) return false;
        if (cel->elemszam == 2) return false;
        cel->ertekek[cel->elemszam++] = szam;
    }
    if (!bemeno.eof() || bemeno.bad()) return false;
    // TODO: csak siker esetén add át az eredményt
    return true;
}

int main() {
    string fajlnev;
    cin >> fajlnev;
    Lista adat;
    adat.ertekek[0] = 40;
    adat.ertekek[1] = 41;
    adat.elemszam = 2;
    bool siker = betolt(fajlnev, &adat);
    cout << siker << " " << adat.elemszam;
    for (int i = 0; i < adat.elemszam; i++) cout << " " << adat.ertekek[i];
    cout << "\n";
    return 0;
}
