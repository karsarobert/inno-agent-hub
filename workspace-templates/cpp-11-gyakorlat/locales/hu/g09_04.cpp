#include <iostream>
using namespace std;

class Hely {
    int sor;
    int szek;
public:
    Hely(int a, int b) {
        sor = a;
        szek = b;
    }
    int sorLeker() const { return sor; }
    int szekLeker() const { return szek; }
};

int main() {
    int a, b;
    cin >> a >> b;
    Hely adat(a, b);
    cout << adat.sorLeker() << " " << adat.szekLeker() << "\n";
    return 0;
}
