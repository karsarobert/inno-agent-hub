#include <iostream>
using namespace std;

class Parkolo {
    int kapacitas = 0;
    int foglalt = 0;
public:
    void beallit(int k, int f) { kapacitas = k; foglalt = f; }
    int szabadHely() { return kapacitas - foglalt; }
};

int main() {
    int k, f;
    cin >> k >> f;
    Parkolo eredeti;
    eredeti.beallit(k, f);
    const Parkolo adat = eredeti;
    cout << adat.szabadHely() << "\n";
    return 0;
}
