#include <iostream>
using namespace std;

class Counter {
    int value = 0;
public:
    void increment(int howMany) { value += howMany; }
    int get() const { return value; }
};

int main() {
    int n;
    cin >> n;
    Counter item;
    item.increment(n);
    cout << item.value << "\n";
    return 0;
}
