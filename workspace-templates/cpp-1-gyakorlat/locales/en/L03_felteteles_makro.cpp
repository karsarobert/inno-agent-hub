/*
 * SUPPLEMENTARY EXERCISE – Conditional compilation and parameterized macros
 *
 * We examine the program with two different compilation settings.
 * Use the SQUARE macro only with the given expressions;
 * SQUARE(i++) is not an appropriate use. The programmer's condition
 * is checked by assert.
 */

#include <iostream>
#include <cassert>

#define SQUARE(x) ((x) * (x))

int main() {
#ifdef DEBUG
    std::cout << "The diagnostic message is enabled." << '\n';
#else
    std::cout << "The diagnostic message is disabled." << '\n';
#endif

    std::cout << "SQUARE(3) = " << SQUARE(3) << '\n';
    std::cout << "SQUARE(1 + 2) = " << SQUARE(1 + 2) << '\n';

    // assert checks a programmer's condition; here it is not user input.
    // If the NDEBUG macro is defined, this check is skipped.
    // The call has no side effect that the program's operation depends on.
    assert(SQUARE(1 + 2) == 9);
    return 0;
}
