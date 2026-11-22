#include <iostream>
#include <fstream>
using namespace std;

int main() {
    int szam;
    cin >> szam;
    ofstream kimeno("out02.txt"); // TODO
    if (!kimeno) { cout << "ERROR\n"; return 0; }
    kimeno << szam << "\n";
    kimeno.close();
    if (kimeno.fail()) { cout << "ERROR\n"; return 0; }
    ifstream bemeno("out02.txt");
    while (bemeno >> szam) cout << szam << "\n";
    return 0;
}
