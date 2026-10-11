#include <iostream>
#include <cmath>

using namespace std;

const int SIZE = 6;

// During the project, place the prototypes of your own functions here.

int main() {
    int measurements[SIZE] = {18, 24, 11, 29, 21, 17};
    int alertThreshold = 20;
    const double stationX = 3.0;
    const double stationY = 4.0;

    cout << "Measurement data project" << '\n';
    cout << "Number of data points: " << SIZE << '\n';
    cout << "First measurement: " << measurements[0] << '\n';
    cout << "Initial alert threshold: " << alertThreshold << '\n';
    cout << "Measurement station coordinates: (" << stationX << ", " << stationY << ")\n";

    // The project will be built step by step. You will add the function calls here.

    return 0;
}

// During the project, place the definitions of your own functions here.
