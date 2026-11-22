#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool negativDarab(const string& fajlnev, int* eredmeny) {
    ifstream bemeno(fajlnev);
    if (!bemeno) return false;
    int ideiglenes = 0;
    int szam;
    while (bemeno >> szam) {
        // TODO 1
    }
    if (!bemeno.eof() || bemeno.bad()) return false;
    // TODO 2
    return true;
}

int main() {
    string fajlnev;
    cin >> fajlnev;
    int eredmeny = 99;
    bool siker = negativDarab(fajlnev, &eredmeny);
    cout << siker << " " << eredmeny << "\n";
    return 0;
}
