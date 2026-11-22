#include <iostream>
using namespace std;

class Keszlet {
    int darab = 20;
public:
    bool lefoglal(int kert) {
        // TODO
        return false;
    }
    int leker() const { return darab; }
};

int main() {
    int x, y;
    cin >> x >> y;
    Keszlet adat;
    cout << adat.lefoglal(x) << " " << adat.leker() << "\n";
    cout << adat.lefoglal(y) << " " << adat.leker() << "\n";
    return 0;
}
