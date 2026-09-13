#include <iostream>
#include <limits>

int main() {
    constexpr unsigned int novekmeny = 1u;
    unsigned int szamlalo = std::numeric_limits<unsigned int>::max();
    std::cout << "Szamlalo elotte: " << szamlalo << '\n';

    szamlalo = szamlalo + novekmeny;
    std::cout << "Szamlalo utana: " << szamlalo << '\n';

    int darabszam = 50000;
    int egysegar = 50000;
    const long long teljes_ar = static_cast<long long>(darabszam) * egysegar;

    std::cout << "int felso hatara: " << std::numeric_limits<int>::max() << '\n';
    std::cout << "Teljes ar: " << teljes_ar << '\n';
    return 0;
}
