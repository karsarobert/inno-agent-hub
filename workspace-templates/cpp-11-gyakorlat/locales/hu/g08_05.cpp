#include <iostream>
using namespace std;

class Persely {
    int penz = 0;
public:
    void befizet(int mennyi) { penz += mennyi; }
    int leker() const { return penz; }
};

int main() {
    int x, y, z;
    cin >> x >> y >> z;
    Persely elso;
    elso.befizet(x);
    Persely masodik = elso;
    // TODO
    cout << elso.leker() << " " << masodik.leker() << "\n";
    return 0;
}
