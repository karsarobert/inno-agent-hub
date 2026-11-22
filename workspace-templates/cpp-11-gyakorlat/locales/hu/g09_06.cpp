#include <iostream>
#include <string>
using namespace std;

class Eszkoz {
public:
    virtual string jelzes() const { return "BASE"; }
};
class Csengo : public Eszkoz {
public:
    string jelzes() const override { return "DING"; }
};

int main() {
    int valasztas;
    cin >> valasztas;
    Eszkoz alap;
    Csengo csengo;
    Eszkoz* mutato = &alap;
    // TODO: hívás a mutatón keresztül
    if (valasztas == 1) mutato = &csengo;
    // TODO: hívás a mutatón keresztül
    return 0;
}
