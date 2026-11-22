#include <iostream>
using namespace std;

class Keszlet {
    int darab = 7;
public:
    void beallit(int uj) { darab = uj; }
    bool ures() const { return false; /* TODO */ }
};

int main() {
    int x, y;
    cin >> x >> y;
    Keszlet elso, masodik;
    elso.beallit(x);
    masodik.beallit(y);
    cout << elso.ures() << " " << masodik.ures() << "\n";
    return 0;
}
