#include <iomanip>
#include <iostream>

int main() {
    constexpr int reszletes_szamjegyek = 17;
    float meres_float = 0.1f;
    double meres_double = 0.1;

    std::cout << std::setprecision(reszletes_szamjegyek);
    std::cout << "float: " << meres_float << '\n';
    std::cout << "double: " << meres_double << '\n';

    constexpr int rovid_szamjegyek = 6;
    constexpr int kozepes_szamjegyek = 7;
    constexpr int hosszu_szamjegyek = 9;
    const float reszletes_meres = 1.23456789f;

    std::cout << "Rovid kiiras: "
              << std::setprecision(rovid_szamjegyek) << reszletes_meres << '\n';
    std::cout << "Kozepes kiiras: "
              << std::setprecision(kozepes_szamjegyek) << reszletes_meres << '\n';
    std::cout << "Hosszu kiiras: "
              << std::setprecision(hosszu_szamjegyek) << reszletes_meres << '\n';
    return 0;
}
