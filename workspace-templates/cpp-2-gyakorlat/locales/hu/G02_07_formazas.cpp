#include <iomanip>
#include <iostream>

int main() {
    constexpr double szamlalo = 1.0;
    constexpr double nevezo = 3.0;
    constexpr int rovid_tizedesjegyek = 2;
    constexpr int reszletes_tizedesjegyek = 10;
    const double hanyados = szamlalo / nevezo;

    std::cout << "Rovid kiiras: " << std::fixed
              << std::setprecision(rovid_tizedesjegyek) << hanyados << '\n';
    std::cout << "Reszletes kiiras: "
              << std::setprecision(reszletes_tizedesjegyek) << hanyados << '\n';
    std::cout << "Tarmeret bajtban: " << sizeof(hanyados) << '\n';
    return 0;
}
