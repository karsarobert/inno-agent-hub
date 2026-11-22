#include <iostream>
using namespace std;

struct Konyv { int azonosito; };
class Polc {
    Konyv adatok[2]{};
    int elemszam = 0;
public:
    bool felvesz(Konyv adat) {
        if (elemszam == 2) return false;
        adatok[elemszam++] = adat;
        return true;
    }
    bool utolsotKivesz() {
        // TODO
        return false;
    }
    int leker() const { return elemszam; }
};

int main() {
    int n, k;
    cin >> n >> k;
    Polc polc;
    for (int i = 0; i < n; i++) polc.felvesz(Konyv{10 + i});
    for (int i = 0; i < k; i++) {
        cout << polc.utolsotKivesz() << " " << polc.leker() << "\n";
    }
    return 0;
}
