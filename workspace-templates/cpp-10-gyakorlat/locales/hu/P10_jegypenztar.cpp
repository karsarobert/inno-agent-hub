// A regi osztalyok adottak; az uj fajlkezelesi muveleteket te irod.
#include <iostream>
using namespace std;

const int KAPACITAS = 4;
class Jegy {
private:
    int sor;
    int szek;
public:
    Jegy() : sor(0), szek(0) {}
    Jegy(int ujSor, int ujSzek) : sor(0), szek(0) {
        if (ujSor >= 1 && ujSor <= 3 && ujSzek >= 1 && ujSzek <= 4) {
            sor = ujSor; szek = ujSzek;
        }
    }
    int sorLeker() const { return sor; }
    int szekLeker() const { return szek; }
    bool ervenyesE() const { return sor >= 1 && sor <= 3 && szek >= 1 && szek <= 4; }
    int ar() const { return !ervenyesE() ? 0 : sor == 1 ? 4000 : 3000; }
};
class Jegypenztar {
private:
    Jegy jegyek[KAPACITAS];
    int darab;
public:
    Jegypenztar() : darab(0) {}
    int darabLeker() const { return darab; }
    bool foglaltE(int sor, int szek) const {
        for (int i = 0; i < darab; ++i)
            if (jegyek[i].sorLeker() == sor && jegyek[i].szekLeker() == szek) return true;
        return false;
    }
    bool felvesz(int sor, int szek) {
        Jegy uj(sor, szek);
        if (!uj.ervenyesE() || darab >= KAPACITAS || foglaltE(sor, szek)) return false;
        jegyek[darab] = uj;
        ++darab;
        return true;
    }
    int bevetel() const {
        int osszeg = 0;
        for (int i = 0; i < darab; ++i) osszeg += jegyek[i].ar();
        return osszeg;
    }
    void lista() const {
        for (int i = 0; i < darab; ++i)
            cout << jegyek[i].sorLeker() << ' ' << jegyek[i].szekLeker() << '\n';
    }
// TODO: P2-P5
};
int main() {
    Jegypenztar penztar;
    cout << penztar.felvesz(1,2) << ' ' << penztar.felvesz(2,3) << ' '
         << penztar.felvesz(1,2) << '\n';
    cout << penztar.darabLeker() << ' ' << penztar.bevetel() << '\n';
}
