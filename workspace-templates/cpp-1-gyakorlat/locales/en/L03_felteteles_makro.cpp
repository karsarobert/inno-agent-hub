/*
 * LESSON 3 - conditional directives and parameterized macros
 *
 * The behaviour of the program depends on whether the DEBUG macro is
 * defined at compile time. The compile commands are in the lesson
 * description below.
 */

#include <iostream>
#include <cassert>
using namespace std;

#ifndef CXX_ALAPOK_HEADER
#define CXX_ALAPOK_HEADER
// Include guard: this block can be included only once per translation unit.
#endif

#define SQUARE(x) ((x) * (x))

int main() {
#ifdef DEBUG
  cout << "DEBUG mode: diagnostic message enabled" << endl;
#else
  cout << "Normal mode: no debug message" << endl;
#endif

  cout << "SQUARE(3) = " << SQUARE(3) << endl;
  cout << "SQUARE(1 + 2) = " << SQUARE(1 + 2) << endl;

  // The parenthesized macro gives the correct result.
  assert(SQUARE(1 + 2) == 9);
  return 0;
}
