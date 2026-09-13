#include <iomanip>
#include <iostream>

int main() {
    constexpr int hallgatok_szama = 2;
    constexpr int maximalis_pontszam = 100;
    constexpr double szazalek_szorzo = 100.0;
    constexpr int kiirt_tizedesjegyek = 1;
    int elso_pontszam = 71;
    int masodik_pontszam = 84;

    const int osszes_pont = elso_pontszam + masodik_pontszam;
    // Kijelölt javítási feladat: ellenőrizd ezt a számítást a kézi átlaggal.
    const double atlag_pontszam = osszes_pont / hallgatok_szama;
    const double atlag_szazalek = atlag_pontszam / maximalis_pontszam * szazalek_szorzo;

    std::cout << std::fixed << std::setprecision(kiirt_tizedesjegyek);
    std::cout << "Atlagos pontszam: " << atlag_pontszam << '\n';
    std::cout << "Atlag szazalekban: " << atlag_szazalek << "%\n";
    return 0;
}
