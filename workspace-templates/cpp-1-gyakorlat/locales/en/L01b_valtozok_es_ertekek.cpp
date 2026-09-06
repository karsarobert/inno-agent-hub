/*
 * CORE EXERCISE – Variables, assignment and division
 *
 * The code is provided. Follow the order of the instructions, and distinguish
 * creating a variable (initialization), assigning a new value later,
 * and printing.
 */

#include <iostream>

int main() {
    int count = 3;
    constexpr int unit_price = 250;
    int total = count * unit_price; // Initialization.

    count = 4; // Assignment.
    std::cout << "Count: " << count << '\n';
    std::cout << "Previously computed total: " << total << '\n';

    total = count * unit_price; // Recomputing the total from the current data.
    std::cout << "Recomputed total: " << total << '\n';

    double int_division = 5 / 2;
    double fp_division = 5.0 / 2;
    std::cout << "Integer division result: " << int_division << '\n';
    std::cout << "Floating-point division result: " << fp_division << '\n';

    bool enough = count >= 4;
    if (enough) {
        std::cout << "The count is at least 4." << '\n';
    } else {
        std::cout << "The count is less than 4." << '\n';
    }
    return 0;
}
