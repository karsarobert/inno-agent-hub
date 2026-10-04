# CPP_05 – mintakódok a projekthez

Ezek a példák **nem a mérési projekt kész megoldásai**. Más nevekkel és adatokkal
mutatják meg az adott programozási mintát. Inno mindig csak az aktuális projektrészhez
tartozó mintát mutassa meg és magyarázza el; ne kérje, hogy ezt a fájlt előre végigolvasd.

## M1 – értéket visszaadó függvény

```cpp
int haromszoros(int ertek) {
    return ertek * 3;
}
```

A függvény egy `int` paramétert kap és egy `int` eredményt ad vissza.

## M2 – `void` függvény tömb bejárásával

```cpp
void pontokKiirasa(const int* pontok, int darab) {
    for (int i = 0; i < darab; ++i) {
        cout << pontok[i] << ' ';
    }
    cout << '\n';
}
```

A `const int*` azt jelzi, hogy a függvény ezen a mutatón keresztül csak olvassa az
adatokat. A `darab` külön paraméter, mert a mutatóból önmagában nem tudjuk meg a
tömb elemszámát.

## M3 – összegző függvény

```cpp
int pontokOsszege(const int* pontok, int darab) {
    int osszeg = 0;

    for (int i = 0; i < darab; ++i) {
        osszeg += pontok[i];
    }

    return osszeg;
}
```

Itt a korábban tanult összegzés kerül egy újrafelhasználható függvénybe.

## M4 – egy saját függvény meghív egy másikat

```cpp
int kettoOsszege(int a, int b) {
    return a + b;
}

double kettoAtlaga(int a, int b) {
    return static_cast<double>(kettoOsszege(a, b)) / 2;
}
```

A második függvény nem ismétli meg az összeadást: felhasználja az elsőt.

## M5 – maximumkeresés

```cpp
int legnagyobbPont(const int* pontok, int darab) {
    int legnagyobb = pontok[0];

    for (int i = 1; i < darab; ++i) {
        if (pontok[i] > legnagyobb) {
            legnagyobb = pontok[i];
        }
    }

    return legnagyobb;
}
```

Ez a példa feltételezi, hogy a tömb legalább egy elemet tartalmaz.

## M6 – feltételes számlálás paraméterezett határral

```cpp
int sikeresekSzama(const int* pontok, int darab, int minimum) {
    int db = 0;

    for (int i = 0; i < darab; ++i) {
        if (pontok[i] >= minimum) {
            ++db;
        }
    }

    return db;
}
```

A harmadik paraméter miatt ugyanaz a függvény több különböző határértékkel használható.

## M7 – eredeti változó módosítása mutatón keresztül

```cpp
void novelEgyet(int* ertek) {
    *ertek += 1;
}
```

A hívás például `novelEgyet(&szam);`. Itt nem másolatot módosítunk: a függvény
megkapja az eredeti változó címét.

## M8 – szabványos matematikai könyvtár használata

```cpp
double atfogo(double a, double b) {
    return sqrt(a * a + b * b);
}
```

Ehhez szükséges a `<cmath>` fejléc. A `sqrt` a szabványos könyvtár `std` névterében
van; a kurzusban használt `using namespace std;` miatt írhatjuk röviden `sqrt(...)` alakban.
