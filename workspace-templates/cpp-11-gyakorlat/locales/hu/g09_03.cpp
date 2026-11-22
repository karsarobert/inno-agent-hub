#include <iostream>
using namespace std;

class Szoba {
    int agyak;
public:
    Szoba(int n) : agyak(n) {}
    int agySzam() const { return agyak; }
};

int main() {
    int a, b;
    cin >> a >> b;
    Szoba szobak[2]; // TODO
    cout << szobak[0].agySzam() << " " << szobak[1].agySzam() << "\n";
    return 0;
}
