#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool mentes(const string& fajlnev, const int adatok[], int n) {
    ofstream kimeno(fajlnev);
    if (!kimeno) return false;
    // TODO
    kimeno.close();
    return !kimeno.fail();
}

int main() {
    int n;
    cin >> n;
    int adatok[4]{};
    for (int i = 0; i < n; i++) cin >> adatok[i];
    if (!mentes("out01.txt", adatok, n)) { cout << "ERROR\n"; return 0; }
    cout << "OK\n";
    ifstream bemeno("out01.txt");
    int szam;
    while (bemeno >> szam) cout << szam << "\n";
    return 0;
}
