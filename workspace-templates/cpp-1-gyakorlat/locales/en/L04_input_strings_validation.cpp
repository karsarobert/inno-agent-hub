/*
 * CORE EXERCISE - Input, string handling and conversion
 *
 * For the initial run, enter Anna as the name and 19 as the age.
 * Enter the two answers on separate lines. First observe the complete program,
 * then change one input or line of code as specified in the exercise.
 */

#include <iostream>
#include <string>

int main() {
    std::string name;
    int age = 0;

    std::cout << "Enter your full name:" << '\n';
    std::getline(std::cin, name);
    if (!std::cin || name.empty()) {
        std::cerr << "Error: could not read a non-empty name." << '\n';
        return 1;
    }

    std::cout << "Enter your age as an integer:" << '\n';
    if (!(std::cin >> age)) {
        std::cerr << "Error: could not read the age as an integer." << '\n';
        return 1;
    }
    // Input rule for this exercise: accept ages from 0 to 120 inclusive.
    if (age < 0 || age > 120) {
        std::cerr << "Error: age must be an integer between 0 and 120." << '\n';
        return 1;
    }

    std::string greeting = "Hi, " + name + "!";
    std::cout << greeting << '\n';
    std::cout << "Number of char elements stored in the name: " << name.size() << '\n';
    std::cout << "Next year you will be " << age + 1 << " years old." << '\n';
    std::cout << "Value of the age variable: " << age << '\n';

    std::string age_text = std::to_string(age);
    std::cout << "Age as text: " << age_text << '\n';

    std::string s = "book";
    char letter = s[2]; // Read a copy of one character.
    s[2] = 'a';
    s += "case";
    std::cout << "Previously read character: " << letter << '\n';
    std::cout << "Modified text: " << s << '\n';
    std::cout << "Length of the modified text: " << s.size() << '\n';
    return 0;
}
