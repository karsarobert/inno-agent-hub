#include <iostream>
using namespace std;

class Room {
    int beds;
public:
    Room(int n) : beds(n) {}
    int bedCount() const { return beds; }
};

int main() {
    int a, b;
    cin >> a >> b;
    Room rooms[2]; // TODO
    cout << rooms[0].bedCount() << " " << rooms[1].bedCount() << "\n";
    return 0;
}
