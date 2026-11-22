#include <iostream>
using namespace std;

class Eredmeny {
    int pont = 0;
public:
    void beallit(int uj) { pont = uj; }
    int leker() const { return pont; }
};
int elerte(const Eredmeny adatok[], int n, int kuszob) {
    int darab = 0;
    // TODO
    return darab;
}

int main() {
    int n, kuszob;
    cin >> n >> kuszob;
    Eredmeny adatok[5];
    for (int i = 0; i < n; i++) {
        int pont;
        cin >> pont;
        adatok[i].beallit(pont);
    }
    cout << elerte(adatok, n, kuszob) << "\n";
    return 0;
}
