/*
 * LESSON 2 - preprocessor basics: #include, #define, -E
 *
 * Macros are substituted at COMPILE TIME (not at run time!).
 * Your task: PREDICT the output, then run it and check.
 */

#include <iostream>
using namespace std;

// Defining a macro (a value macro)
#define PRINT_MY_NAME cout << "My name is John Doe" << endl;
#define MY_FAV_NUM 42

int main() {
  // PREDICTION (predict before running!):
  // Question: what will the output be? If you are not sure, say your guess,
  // then run it and compare.

  PRINT_MY_NAME
  cout << "My fav number is: " << MY_FAV_NUM << endl;

  return 0;
}
