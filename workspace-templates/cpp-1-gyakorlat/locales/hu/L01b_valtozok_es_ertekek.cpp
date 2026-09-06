/*
 * ALAPGYAKORLAT – Változók, értékadás és osztás
 *
 * A kód adott. Kövesd az utasítások sorrendjét, és különítsd el
 * a változó létrehozását, a későbbi értékadást és a kiírást.
 */

#include <iostream>

int main() {
    int darab = 3;
    constexpr int egysegar = 250;
    int osszeg = darab * egysegar; // Inicializálás.

    darab = 4; // Értékadás.
    std::cout << "Darabszam: " << darab << '\n';
    std::cout << "Korabban kiszamitott osszeg: " << osszeg << '\n';

    osszeg = darab * egysegar; // Az összeg kiszámítása az aktuális adatokból.
    std::cout << "Ujraszamitott osszeg: " << osszeg << '\n';

    double egesz_osztas = 5 / 2;
    double lebegopontos_osztas = 5.0 / 2;
    std::cout << "Egesz osztas eredmenye: " << egesz_osztas << '\n';
    std::cout << "Lebegopontos osztas eredmenye: " << lebegopontos_osztas << '\n';

    bool elegendo = darab >= 4;
    if (elegendo) {
        std::cout << "A darabszam legalabb 4." << '\n';
    } else {
        std::cout << "A darabszam kisebb 4-nel." << '\n';
    }
    return 0;
}
