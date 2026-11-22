#include <iostream>
using namespace std;

class Battery {
    int charge;
public:
    Battery(int initial) {
        charge = 0; // TODO
    }
    int get() const { return charge; }
};

int main() {
    int n;
    cin >> n;
    Battery item(n);
    cout << item.get() << "\n";
    return 0;
}
