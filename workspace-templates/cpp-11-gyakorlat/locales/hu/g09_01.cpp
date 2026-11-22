#include <iostream>
using namespace std;

class Teglalap {
    int szelesseg;
    int magassag;
public:
    Teglalap() : szelesseg(0), magassag(0) /* TODO 1 */ {}
    Teglalap(int a, int b) : szelesseg(0), magassag(0) /* TODO 2 */ {}
    int terulet() const { return szelesseg * magassag; }
};

int main() {
    int a, b;
    cin >> a >> b;
    Teglalap elso;
    Teglalap masodik(a, b);
    cout << elso.terulet() << " " << masodik.terulet() << "\n";
    return 0;
}
