#include <iostream>

int main() {
    constexpr int maximalis_pontszam = 100;
    int pontszam{};
    std::cout << "Kezdo pontszam: " << pontszam << '\n';

    pontszam = 72;
    const int rogzitett_pontszam = pontszam;

    std::cout << "Aktualis pontszam: " << pontszam << '\n';
    std::cout << "Rogzitett pontszam: " << rogzitett_pontszam << '\n';
    std::cout << "Maximalis pontszam: " << maximalis_pontszam << '\n';
    return 0;
}
