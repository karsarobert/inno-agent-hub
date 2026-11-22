#include <iostream>
using namespace std;

class Akkumulator {
    int toltes;
public:
    Akkumulator(int kezdo) {
        toltes = 0; // TODO
    }
    int leker() const { return toltes; }
};

int main() {
    int n;
    cin >> n;
    Akkumulator adat(n);
    cout << adat.leker() << "\n";
    return 0;
}
