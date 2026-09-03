/*
 * LESSON 4 - C++ I/O, std::string, conversion and debugging
 *
 * The program reads data from the user, performs string operations,
 * and checks an important condition with assert.
 * PREDICT the output before you run it!
 */

#include <iostream>
#include <string>
#include <cassert>
using namespace std;

int main() {
  string name;
  int age;

  cout << "Enter your name and age (separated by a space): ";
  cin >> name >> age;

  // string operations
  string greeting = "Hello, " + name + "!";
  cout << greeting << endl;
  cout << "Your name is " << name.size() << " characters long." << endl;

  // conversion
  string age_as_text = to_string(age);
  cout << "Your age as text: " + age_as_text << endl;

  // assert: the age is in a sensible range
  assert(age > 0);
  assert(age < 150);

  return 0;
}
