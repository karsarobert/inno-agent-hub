#include <iostream>
using namespace std;

class Stock {
    int count = 7;
public:
    void set(int next) { count = next; }
    bool isEmpty() const { return false; /* TODO */ }
};

int main() {
    int x, y;
    cin >> x >> y;
    Stock first, second;
    first.set(x);
    second.set(y);
    cout << first.isEmpty() << " " << second.isEmpty() << "\n";
    return 0;
}
