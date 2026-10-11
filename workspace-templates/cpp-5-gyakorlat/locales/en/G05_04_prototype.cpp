#include <iostream>

using namespace std;

int main() {
    const int a = 8;
    const int b = 3;

    cout << "a = " << a << ", b = " << b << '\n';

    // First, try to call the add function here.
    // Observe what the compiler says, then solve the problem with a prototype.

    return 0;
}

int add(int a, int b) {
    return a + b;
}
