#include <iostream>
using namespace std;

struct Measurement {
    int id;
    double value;
    bool valid;
};

// You may define your function before main.

int main() {
    Measurement original{201, 10.5, true};
    cout << "Initial measurement: " << original.id << " "
         << original.value << " " << original.valid << '\n';

    // First use a function to create a modified copy.
    // Then modify the original object through a pointer.
    return 0;
}
