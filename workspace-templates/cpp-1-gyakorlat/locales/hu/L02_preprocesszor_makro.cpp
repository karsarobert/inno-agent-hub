/*
 * KIEGÉSZÍTŐ GYAKORLAT – Előfeldolgozás és makrók
 *
 * Ezt a példát az alapgyakorlatok után nézd meg.
 * A makró az előfeldolgozás szemléltetését szolgálja; rögzített számértékhez
 * általában constexpr állandót használunk.
 */

#include <iostream>

#define KEDVENC_SZAM 42

int main() {
    std::cout << "A nevem: Kiss Anna." << '\n';
    std::cout << "Kedvenc szamom: " << KEDVENC_SZAM << '\n';
    return 0;
}
