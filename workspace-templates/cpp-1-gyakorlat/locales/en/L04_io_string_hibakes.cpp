/*
 * CORE EXERCISE – Reading input, string handling and conversion
 *
 * For the initial run, enter Anna as the name and 19 as the age.
 * Give the two answers on separate lines. First observe the whole program,
 * then change one specified input or code line at a time as the exercise says.
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

    std::cout << "Enter your age as a whole number:" << '\n';
    if (!(std::cin >> age)) {
        std::cerr << "Error: could not read the age as a whole number." << '\n';
        return 1;
    }
    // The exercise's input rule: we accept ages between 0 and 120.
    if (age < 0 || age > 120) {
        std::cerr << "Error: the age must be a whole number between 0 and 120." << '\n';
        return 1;
    }

    std::string greeting = "Hi, " + name + "!";
    std::cout << greeting << '\n';
    std::cout << "Number of char elements stored in the name: " << name.size() << '\n';
    std::cout << "Next year you will be " << age + 1 << '.' << '\n';
    std::cout << "Value of the age variable: " << age << '\n';

    std::string age_text = std::to_string(age);
    std::cout << "Age as text: " << age_text << '\n';

    std::string s = "alma";
    char letter = s[2]; // Reading out one character.
    s[2] = 'e';
    s += "fa";
    std::cout << "Character read earlier: " << letter << '\n';
    std::cout << "Modified text: " << s << '\n';
    std::cout << "Length of the modified text: " << s.size() << '\n';
    return 0;
}
