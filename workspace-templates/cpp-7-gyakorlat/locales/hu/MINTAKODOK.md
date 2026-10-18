# CPP_07 – Analóg mintakódok

A minták nem a mérési feladat kész megoldásai. Más neveket és adatokat használnak. Mindegyik külön fájlként, önállóan fordítható. Inno csak az aktuális mintát mutassa és magyarázza el; ne az egész gyűjteményt egyszerre.

## M1 – Típus, objektum és másolat

```cpp
#include <iostream>
using namespace std;

struct Termek {
    int kod;
    double ar;
    bool kaphato;
};

int main() {
    Termek elso{12, 450.0, true};
    Termek masodik = elso; // Uj objektum inicializalasa.
    masodik.ar = 500.0;
    cout << elso.ar << " " << masodik.ar << '\n';
    masodik = elso;        // Mar letezo objektum ertekadasa.
    cout << elso.ar << " " << masodik.ar << '\n';
    return 0;
}
```

Várható kimenet:

```text
450 500
450 450
```

A típus három mezőt ír le. Két külön objektum készül: a második árának átírása nem módosítja az elsőt. A későbbi értékadás visszamásolja az első mezőértékeit.

## M2 – Struktúraparaméter és struktúra visszaadása

```cpp
#include <iostream>
using namespace std;
struct Pont {
    int x;
    int y;
};

Pont eltolt(Pont hely, int lepes) {
    hely.x += lepes; // A sajat parameterunket modositjuk.
    return hely;    // Egy teljes strukturat adunk vissza.
}

int main() {
    Pont eredeti{1, 2};
    Pont uj = eltolt(eredeti, 5);
    cout << eredeti.x << " " << uj.x << '\n';
    return 0;
}
```

Várható kimenet:

```text
1 6
```

A visszatérési típus Pont. A hely paraméter külön objektum, amelyet a függvény módosít. Az eredeti pont változatlan, az új pont a visszatérő értékből készül.

## M3 – Eredeti objektum módosítása mutatóval

```cpp
#include <iostream>
using namespace std;
struct Arucikk {
    double ar;
};

void kedvezmeny(Arucikk* cikk, double osszeg) {
    cikk->ar -= osszeg; // A megmutatott objektum valtozik.
}

int main() {
    Arucikk termek{100.0};
    kedvezmeny(&termek, 10.0);
    cout << termek.ar << '\n';
    return 0;
}
```

Várható kimenet:

```text
90
```

A függvény a termék címét kapja. A nyíl a megmutatott objektum mezőjét választja ki. Az eredeti ár változik, nem egy külön objektum másolt értéke.

## M4 – Jelzővel követett uniós változat

```cpp
#include <iostream>
using namespace std;
union BeallitasAdat {
    int fokozat;
    double arany;
};
struct Beallitas {
    bool fokozatos;
    BeallitasAdat adat;
};

void megjelenit(Beallitas beallitas) {
    if (beallitas.fokozatos) {
        cout << beallitas.adat.fokozat << '\n';
    } else {
        cout << beallitas.adat.arany << '\n';
    }
}

int main() {
    Beallitas beallitas{};
    beallitas.adat.fokozat = 3;
    beallitas.fokozatos = true;
    megjelenit(beallitas);
    beallitas.adat.arany = 0.75;
    beallitas.fokozatos = false;
    megjelenit(beallitas);
    return 0;
}
```

Várható kimenet:

```text
3
0.75
```

Az unió alternatív mezői közös tárterületet használnak. A struktúra külön jelzője rögzíti a választott változatot. A mezőváltáskor a jelzőt is frissítjük, és a kiírás csak a megfelelő mezőt olvassa.

## M5 – Névkeresés és belső blokk

```cpp
#include <iostream>
using namespace std;
int pont = 3;
void mutat() { cout << pont << '\n'; }

int main() {
    int pont = 8;
    {
        int pont = 12; // Kulon objektum, azonos nevvel.
        cout << pont << '\n';
    }
    cout << pont << '\n';
    cout << ::pont << '\n'; // A globalis nevet minositjuk.
    mutat();
    return 0;
}
```

Várható kimenet:

```text
12
8
3
3
```

A belső név 12-t jelöl, a blokk után ismét a main helyi 8-as értékét érjük el. A ::pont kifejezés közvetlenül a globális 3-at éri el. A mutat függvény kódjában is a globális 3 látható: a hívás nem teszi elérhetővé a main helyi változóját.

## M6 – Beágyazott adat és érték szerinti kiírás

```cpp
#include <iostream>
using namespace std;
struct Pozicio {
    int sor;
    int oszlop;
};
struct Csomag {
    int kod;
    Pozicio hely;
};

void mutat(Csomag csomag) {
    cout << csomag.kod << ": " << csomag.hely.sor << ", "
         << csomag.hely.oszlop << '\n';
}

int main() {
    Csomag doboz{7, {2, 4}};
    mutat(doboz);
    return 0;
}
```

Várható kimenet:

```text
7: 2, 4
```

A hely maga is struktúra. A csomag.hely.sor először helyet, azon belül sort választ. A void függvény érték szerint kap egy csomagot, és annak adatait kiírja.

## M7 – Struktúratömb bejárása meglévő függvénnyel

```cpp
#include <iostream>
using namespace std;
struct Tetel {
    int kod;
    int keszlet;
};

void tetelKiirasa(Tetel tetel) {
    cout << tetel.kod << ": " << tetel.keszlet << '\n';
}

void lista(const Tetel* tetelek, int darab) {
    for (int i = 0; i < darab; ++i) {
        tetelKiirasa(tetelek[i]);
    }
}

int main() {
    Tetel tetelek[2] = {{11, 3}, {12, 8}};
    lista(tetelek, 2);
    return 0;
}
```

Várható kimenet:

```text
11: 3
12: 8
```

A függvény mutatót és külön elemszámot kap. A ciklus egy teljes elemet választ ki, majd átadja a már megírt kiírónak. A const miatt ezen a mutatón keresztül nem módosítjuk a tömbelemeket.

## M8 – Feltételes számlálás

```cpp
#include <iostream>
using namespace std;
struct Vizsga {
    int pont;
    bool resztVett;
};

int megfelelok(const Vizsga* vizsgak, int darab, int minimum) {
    int eredmeny = 0;
    for (int i = 0; i < darab; ++i) {
        if (vizsgak[i].resztVett && vizsgak[i].pont >= minimum) {
            ++eredmeny;
        }
    }
    return eredmeny;
}

int main() {
    Vizsga vizsgak[3] = {{60, true}, {90, false}, {80, true}};
    cout << megfelelok(vizsgak, 3, 60) << '\n';
    return 0;
}
```

Várható kimenet:

```text
2
```

A számláló nulláról indul, a két feltételt && kapcsolja össze. A P3 projektrészben csak az érvényesség kell. A P5 már két feltételt kér, de szigorúan nagyobb értékkel, nem a minta nagyobb-vagy-egyenlő feltételével.

## M9 – Átlag és nulla elemszám

```cpp
#include <iostream>
using namespace std;

double arakAtlaga(const double* arak, int darab) {
    double osszeg = 0.0;
    for (int i = 0; i < darab; ++i) {
        osszeg += arak[i];
    }
    return osszeg / darab; // Elofeltetel: darab pozitiv.
}

int main() {
    const int darab = 2;
    double arak[darab] = {10.0, 15.0};
    if (darab > 0) {
        cout << arakAtlaga(arak, darab) << '\n';
    } else {
        cout << "Nincs adat." << '\n';
    }
    return 0;
}
```

Várható kimenet:

```text
12.5
```

A double összeg megőrzi a tört részt. A hívó ellenőrzi a pozitív darabszámot. A projektben az érvénytelen rekordokat ki is kell szűrni: a nevező az érvényes darabszám, nem a teljes tömbméret.
