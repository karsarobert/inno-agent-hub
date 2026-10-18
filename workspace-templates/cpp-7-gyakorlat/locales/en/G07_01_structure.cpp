#include <iostream>
using namespace std;

// Define the requested type before main.

int main() {
    const int initialId = 101;
    const double initialValue = 23.5;
    const bool initialValid = true;

    cout << "Initial data: " << initialId << " "
         << initialValue << " " << initialValid << '\n';

    // Create a measurement, then create and modify an independent copy.
    // Try assignment to the existing object as a separate step.
    return 0;
}
