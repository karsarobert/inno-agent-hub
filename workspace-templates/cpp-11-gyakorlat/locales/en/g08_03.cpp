#include <iostream>
using namespace std;

class Stock {
    int count = 20;
public:
    bool reserve(int requested) {
        // TODO
        return false;
    }
    int get() const { return count; }
};

int main() {
    int x, y;
    cin >> x >> y;
    Stock item;
    cout << item.reserve(x) << " " << item.get() << "\n";
    cout << item.reserve(y) << " " << item.get() << "\n";
    return 0;
}
