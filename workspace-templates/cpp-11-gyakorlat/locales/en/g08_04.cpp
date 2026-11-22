#include <iostream>
using namespace std;

class Parking {
    int capacity = 0;
    int occupied = 0;
public:
    void set(int k, int f) { capacity = k; occupied = f; }
    int freeSpaces() { return capacity - occupied; }
};

int main() {
    int k, f;
    cin >> k >> f;
    Parking original;
    original.set(k, f);
    const Parking item = original;
    cout << item.freeSpaces() << "\n";
    return 0;
}
