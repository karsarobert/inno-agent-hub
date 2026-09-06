/*
 * ALAPGYAKORLAT – Beolvasás, szövegkezelés és konverzió
 *
 * A kiinduló próbához névként Anna, életkorként 19 legyen a bemenet.
 * A két választ külön sorban add meg. Először figyeld meg a teljes programot,
 * majd a gyakorlatban megadott egy-egy bemenetet vagy kódsort változtasd meg.
 */

#include <iostream>
#include <string>

int main() {
    std::string nev;
    int kor = 0;

    std::cout << "Add meg a teljes neved:" << '\n';
    std::getline(std::cin, nev);
    if (!std::cin || nev.empty()) {
        std::cerr << "Hiba: nem sikerult nem ures nevet beolvasni." << '\n';
        return 1;
    }

    std::cout << "Add meg az eletkorod egesz szamkent:" << '\n';
    if (!(std::cin >> kor)) {
        std::cerr << "Hiba: az eletkort nem sikerult egesz szamkent beolvasni." << '\n';
        return 1;
    }
    // A gyakorlat bemeneti szabálya: 0 és 120 közötti életkort fogadunk el.
    if (kor < 0 || kor > 120) {
        std::cerr << "Hiba: az eletkor 0 es 120 kozotti egesz szam legyen." << '\n';
        return 1;
    }

    std::string udvozles = "Szia, " + nev + "!";
    std::cout << udvozles << '\n';
    std::cout << "A nevben tarolt char elemek szama: " << nev.size() << '\n';
    std::cout << "Jovore " << kor + 1 << " eves leszel." << '\n';
    std::cout << "A kor valtozo erteke: " << kor << '\n';

    std::string kor_szoveg = std::to_string(kor);
    std::cout << "Eletkor szovegkent: " << kor_szoveg << '\n';

    std::string s = "alma";
    char betu = s[2]; // Egy karakter kiolvasása.
    s[2] = 'e';
    s += "fa";
    std::cout << "Korabban kiolvasott karakter: " << betu << '\n';
    std::cout << "Modositott szoveg: " << s << '\n';
    std::cout << "A modositott szoveg hossza: " << s.size() << '\n';
    return 0;
}
