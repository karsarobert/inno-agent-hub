#include <iomanip>
#include <iostream>

int main() {
    constexpr int detailed_digits = 17;
    float float_measurement = 0.1f;
    double double_measurement = 0.1;

    std::cout << std::setprecision(detailed_digits);
    std::cout << "float: " << float_measurement << '\n';
    std::cout << "double: " << double_measurement << '\n';

    constexpr int short_digits = 6;
    constexpr int medium_digits = 7;
    constexpr int long_digits = 9;
    const float detailed_measurement = 1.23456789f;

    std::cout << "Short output: "
              << std::setprecision(short_digits) << detailed_measurement << '\n';
    std::cout << "Medium output: "
              << std::setprecision(medium_digits) << detailed_measurement << '\n';
    std::cout << "Long output: "
              << std::setprecision(long_digits) << detailed_measurement << '\n';
    return 0;
}
