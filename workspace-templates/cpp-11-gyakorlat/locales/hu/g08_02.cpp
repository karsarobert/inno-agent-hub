#include <iostream>
using namespace std;

class Szamlalo {
    int ertek = 0;
public:
    void novel(int mennyi) { ertek += mennyi; }
    int leker() const { return ertek; }
};

int main() {
    int n;
    cin >> n;
    Szamlalo adat;
    adat.novel(n);
    cout << adat.ertek << "\n";
    return 0;
}
