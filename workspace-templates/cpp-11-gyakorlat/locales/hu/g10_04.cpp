#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    string fajlnev;
    cin >> fajlnev;
    ifstream bemeno(fajlnev);
    if (!bemeno) { cout << "ERROR\n"; return 0; }
    int szam = 0;
    int darab = 0;
    while (!bemeno.eof()) {
        bemeno >> szam;
        if (szam % 2 == 0) darab++;
    }
    cout << darab << "\n";
    return 0;
}
