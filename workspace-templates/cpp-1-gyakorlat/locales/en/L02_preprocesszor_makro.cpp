/*
 * SUPPLEMENTARY EXERCISE – Preprocessing and macros
 *
 * Look at this example after the core exercises.
 * The macro serves to demonstrate preprocessing; for a fixed numeric value
 * we usually use a constexpr constant.
 */

#include <iostream>

#define FAVOURITE_NUMBER 42

int main() {
    std::cout << "My name is Kiss Anna." << '\n';
    std::cout << "My favourite number: " << FAVOURITE_NUMBER << '\n';
    return 0;
}
