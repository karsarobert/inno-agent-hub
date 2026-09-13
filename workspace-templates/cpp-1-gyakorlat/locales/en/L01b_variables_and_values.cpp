/*
 * CORE EXERCISE - Variables, assignment and division
 *
 * The code is provided. Follow the statements in order and distinguish
 * creating a variable, assigning a new value later, and displaying a value.
 */

#include <iostream>

int main() {
    int quantity = 3;
    constexpr int unit_price = 250;
    int total = quantity * unit_price; // Initialization.

    quantity = 4; // Assignment.
    std::cout << "Quantity: " << quantity << '\n';
    std::cout << "Previously calculated total: " << total << '\n';

    total = quantity * unit_price; // Calculate the total using the current values.
    std::cout << "Recalculated total: " << total << '\n';

    double integer_division = 5 / 2;
    double floating_point_division = 5.0 / 2;
    std::cout << "Integer division result: " << integer_division << '\n';
    std::cout << "Floating-point division result: " << floating_point_division << '\n';

    bool enough = quantity >= 4;
    if (enough) {
        std::cout << "The quantity is at least 4." << '\n';
    } else {
        std::cout << "The quantity is less than 4." << '\n';
    }
    return 0;
}
