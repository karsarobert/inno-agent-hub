#include <iostream>
using namespace std;

// The date will be a nested member of a measurement.
struct Date {
    int year;
    int month;
    int day;
};

struct Measurement {
    int id;
    double value;
    bool valid;
    Date recorded;
};

// Add your function prototypes here.

int main() {
    const int size = 6;
    Measurement measurements[size] = {
        {101, 18.5, true,  {2026, 10, 17}},
        {102, 26.0, false, {2026, 10, 17}},
        {103, 21.0, true,  {2026, 10, 17}},
        {104, -2.0, true,  {2026, 10, 17}},
        {105, 30.5, true,  {2026, 10, 17}},
        {106, 21.0, true,  {2026, 10, 17}}
    };
    const double threshold = 20.0;

    cout << "Measurement data project" << '\n';
    cout << "Number of records: " << size << '\n';
    cout << "First identifier: " << measurements[0].id << '\n';
    cout << "Initial threshold: " << threshold << '\n';

    // Add your processing function calls here, one step at a time.
    return 0;
}

// Add your function definitions here.
