/*
 * OPTIONAL EXERCISE - Preprocessing and macros
 *
 * Study this example after the core exercises.
 * The macro illustrates preprocessing; for a fixed numerical value,
 * we usually use a constexpr constant.
 */

#include <iostream>

#define FAVORITE_NUMBER 42

int main() {
    std::cout << "My name is Anna Hill." << '\n';
    std::cout << "My favorite number: " << FAVORITE_NUMBER << '\n';
    return 0;
}
