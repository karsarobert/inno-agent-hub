#include <iomanip>
#include <iostream>

int main() {
    constexpr double numerator = 1.0;
    constexpr double denominator = 3.0;
    constexpr int short_decimal_places = 2;
    constexpr int detailed_decimal_places = 10;
    const double quotient = numerator / denominator;

    std::cout << "Short output: " << std::fixed
              << std::setprecision(short_decimal_places) << quotient << '\n';
    std::cout << "Detailed output: "
              << std::setprecision(detailed_decimal_places) << quotient << '\n';
    std::cout << "Storage size in bytes: " << sizeof(quotient) << '\n';
    return 0;
}
