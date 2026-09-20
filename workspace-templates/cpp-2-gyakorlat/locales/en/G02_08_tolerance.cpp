#include <cmath>
#include <iomanip>
#include <iostream>

int main() {
    constexpr double expected_length_m = 1.2340;
    constexpr double allowed_deviation_m = 0.001;
    constexpr int displayed_decimal_places = 4;
    double measured_length_m = 1.2345;

    const double absolute_deviation_m = std::abs(measured_length_m - expected_length_m);
    const bool within_tolerance = absolute_deviation_m < allowed_deviation_m;

    std::cout << "Absolute deviation in metres: " << std::fixed
              << std::setprecision(displayed_decimal_places) << absolute_deviation_m << '\n';
    std::cout << "Within tolerance: " << std::boolalpha << within_tolerance << '\n';
    return 0;
}
