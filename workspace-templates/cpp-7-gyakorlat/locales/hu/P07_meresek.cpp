#include <iostream>
using namespace std;

// A datum egy meres osszetett mezoje lesz.
struct Datum {
    int ev;
    int honap;
    int nap;
};

struct Meres {
    int azonosito;
    double ertek;
    bool ervenyes;
    Datum rogzitve;
};

// Ide kerulnek a sajat fuggvenyek prototipusai.

int main() {
    const int meret = 6;
    Meres meresek[meret] = {
        {101, 18.5, true,  {2026, 10, 17}},
        {102, 26.0, false, {2026, 10, 17}},
        {103, 21.0, true,  {2026, 10, 17}},
        {104, -2.0, true,  {2026, 10, 17}},
        {105, 30.5, true,  {2026, 10, 17}},
        {106, 21.0, true,  {2026, 10, 17}}
    };
    const double kuszob = 20.0;

    cout << "Meresi adatok projekt" << '\n';
    cout << "Adatok szama: " << meret << '\n';
    cout << "Elso azonosito: " << meresek[0].azonosito << '\n';
    cout << "Kezdeti kuszob: " << kuszob << '\n';

    // A feldolgozo fuggvenyek hivasait te irod ide, lepesenkent.
    return 0;
}

// Ide kerulnek a sajat fuggvenyek definicioi.
