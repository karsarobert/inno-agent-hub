#include <iostream>
using namespace std;

class MoneyBox {
    int money = 0;
public:
    void deposit(int howMany) { money += howMany; }
    int get() const { return money; }
};

int main() {
    int x, y, z;
    cin >> x >> y >> z;
    MoneyBox first;
    first.deposit(x);
    MoneyBox second = first;
    // TODO
    cout << first.get() << " " << second.get() << "\n";
    return 0;
}
