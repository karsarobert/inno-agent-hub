#include <iostream>
using namespace std;

class Seat {
    int line;
    int seat;
public:
    Seat(int a, int b) {
        line = a;
        seat = b;
    }
    int getRow() const { return line; }
    int getSeat() const { return seat; }
};

int main() {
    int a, b;
    cin >> a >> b;
    Seat item(a, b);
    cout << item.getRow() << " " << item.getSeat() << "\n";
    return 0;
}
