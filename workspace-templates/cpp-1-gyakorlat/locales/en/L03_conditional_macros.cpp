/*
 * OPTIONAL EXERCISE - Conditional compilation and function-like macros
 *
 * We examine this program with two different compilation settings.
 * Use SQUARE only with the specified expressions;
 * SQUARE(i++) is not an appropriate use. assert checks a programmer's assumption.
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

    // assert checks a programmer's assumption, not user input here.
    // If NDEBUG is defined, this check is omitted.
    // The call has no side effect that the program needs in order to work.
    assert(SQUARE(1 + 2) == 9);
    return 0;
}
