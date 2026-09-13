// Választható bemutató. A kiinduló program helyes; csak tutorral módosítsd.
#include <iostream>

int main() {
    int darabszam = 50000;
    int egysegar = 50000;
    const long long teljes_ar = static_cast<long long>(darabszam) * egysegar;

    std::cout << "Teljes ar: " << teljes_ar << '\n';
    return 0;
}
