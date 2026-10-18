#include <iostream>
using namespace std;

int number = 5;

void printGlobal() {
    cout << "Value visible in the function: " << number << '\n';
}

int main() {
    cout << "Initial global value: " << number << '\n';

    // Add a local variable and a separate inner block as instructed.
    // Examine shadowing, then call the existing function.
    // Finally, examine the scope of a variable declared in the loop header.
    return 0;
}
