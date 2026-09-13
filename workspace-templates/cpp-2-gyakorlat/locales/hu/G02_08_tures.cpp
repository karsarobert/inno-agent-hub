#include <cmath>
#include <iomanip>
#include <iostream>

int main() {
    constexpr double elvart_hossz_meter = 1.2340;
    constexpr double megengedett_elteres_meter = 0.001;
    constexpr int kiirt_tizedesjegyek = 4;
    double mert_hossz_meter = 1.2345;

    const double abszolut_elteres_meter = std::abs(mert_hossz_meter - elvart_hossz_meter);
    const bool turesen_belul = abszolut_elteres_meter < megengedett_elteres_meter;

    std::cout << "Abszolut elteres meterben: " << std::fixed
              << std::setprecision(kiirt_tizedesjegyek) << abszolut_elteres_meter << '\n';
    std::cout << "Turesen belul: " << std::boolalpha << turesen_belul << '\n';
    return 0;
}
