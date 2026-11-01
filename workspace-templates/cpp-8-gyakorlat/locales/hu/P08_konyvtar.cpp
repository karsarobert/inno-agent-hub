#include <iostream>
using namespace std;

// Csak forrasadatok; a Konyv objektumokat es ciklusokat te keszited.
int main() {
    const int meret = 6;
    const int azonositok[meret] = {501, 502, 503, 504, 505, 506};
    const int allomanyok[meret] = {5, 3, 0, 7, 4, 2};
    const int kolcsonzesek[meret] = {3, 3, 0, 2, 0, 1};
    cout << "Forrascimek szama: " << meret << '\n';
    cout << "Elso forras: " << azonositok[0] << ' ' << allomanyok[0] << ' ' << kolcsonzesek[0] << '\n';
    return 0;
}
