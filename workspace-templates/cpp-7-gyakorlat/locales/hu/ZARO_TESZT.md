# CPP_07 – Rögzített záróteszt

A tutor egyenként, sorrendben adja a kérdéseket. Az első érdemi válasz számít. A T2 első öt kódját válaszadás előtt ne futtasd. A hibakeresési kódok elemzésre valók; a veszélyes unió- és tömbhatárhibát javítás előtt ne futtasd.

# T1 – 10 feleletválasztós kérdés

## T1/1

Mi a struktúra egyik jellegzetessége?

A) Csak azonos típusú elemeket tartalmazhat.

B) Nevesített, akár eltérő típusú mezőket fog össze.

C) Mindig számmal indexeljük.

D) Csak egy mező értékét tárolhatja egyszerre.

## T1/2

Mit hoz létre önmagában a struct Meres { int azonosito; double ertek; }; deklaráció?

A) Egy 0 értékű mérést.

B) Két külön globális változót.

C) Egy Meres nevű típust, konkrét mérési objektum nélkül.

D) Egy függvényhívást.

## T1/3

Mi történik a Meres masolat = eredeti; sorban, ha a masolat itt jelenik meg először?

A) Új objektum jön létre másoló inicializálással.

B) Az eredeti objektum törlődik.

C) A masolat az eredeti másik neve lesz.

D) Csak a típus neve változik meg.

## T1/4

Melyik éri el a mutato nevű, struktúrára mutató mutatóval a megmutatott objektum ertek mezőjét?

A) mutato.ertek

B) mutato[ertek]

C) &mutato.ertek

D) mutato->ertek

## T1/5

Mit jelent a const Meres* adatok paraméter?

A) A függvény semmilyen adatot nem olvashat.

B) A függvény ezen a mutatón keresztül nem módosíthatja a méréseket.

C) Az elemszám automatikusan ismert.

D) Az összes mérés biztosan érvényes.

## T1/6

Az egyszerű int/double uniónál melyik mezőt olvassuk a biztonságos példákban?

A) A jelenleg aktív mezőt.

B) Mindkettőt, tetszőleges sorrendben.

C) Mindig az elsőt, függetlenül az értékadástól.

D) Csak a nagyobb méretűt.

## T1/7

Mi biztosítja a külön jelzőmező és az unió aktív mezőjének összhangját?

A) A cout automatikusan kijavítja.

B) Az unió maga eltárolja a jelző helyes értékét.

C) A programnak kell mindkettőt következetesen beállítania.

D) Az include utasítás.

## T1/8

Hol használható az index, ha a for ciklus fejlécében deklaráltuk?

A) A teljes programban.

B) Minden másik függvényben.

C) Csak a ciklus utáni első sorban.

D) A ciklus feltételében, léptetésében és törzsében; utána már nem.

## T1/9

Egy meghívott függvény automatikusan hozzáfér a hívó függvény helyi változójához?

A) Igen, ha ugyanaz a változónév.

B) Nem; az értéket például paraméterként adjuk át.

C) Igen, ha mindkét függvény void.

D) Csak akkor, ha a hívó main.

## T1/10

Mi történik a külső objektummal, amikor egy belső blokk azonos nevű helyi változót deklarál?

A) Azonnal megszűnik.

B) Automatikusan 0 lesz az értéke.

C) Tovább létezik; a belső név elrejti a szokásos névkeresés elől.

D) Mindig a belső objektumra mutató mutatóvá válik.

# T2 – 5 kimenet és 5 hibakeresés

## T2/1 – kimenet

Mi a kód pontos kimenete?

```cpp
#include <iostream>
using namespace std;
struct Meres { double ertek; };
int main() {
    Meres eredeti{8.0};
    Meres masolat = eredeti;
    masolat.ertek = 11.0;
    cout << eredeti.ertek << " " << masolat.ertek << '\n';
    return 0;
}
```

## T2/2 – kimenet

Mi a kód pontos kimenete?

```cpp
#include <iostream>
using namespace std;
struct Meres { double ertek; };
Meres emelt(Meres adat) {
    adat.ertek += 4.0;
    return adat;
}
int main() {
    Meres eredeti{10.0};
    Meres uj = emelt(eredeti);
    Meres* mutato = &eredeti;
    mutato->ertek += 3.0;
    cout << eredeti.ertek << " " << uj.ertek << '\n';
    return 0;
}
```

## T2/3 – kimenet

Mi a kód pontos kimenete?

```cpp
#include <iostream>
using namespace std;
struct Meres { double ertek; bool ervenyes; };
int main() {
    Meres adatok[3] = {{8.0, true}, {100.0, false}, {12.0, true}};
    double osszeg = 0.0;
    int darab = 0;
    for (int i = 0; i < 3; ++i) {
        if (adatok[i].ervenyes) {
            osszeg += adatok[i].ertek;
            ++darab;
        }
    }
    cout << osszeg / darab << '\n';
    return 0;
}
```

## T2/4 – kimenet

Mi a kód pontos kimenete?

```cpp
#include <iostream>
using namespace std;
union Szam { int egesz; double tort; };
int main() {
    Szam adat{};
    adat.egesz = 4;
    cout << adat.egesz << " ";
    adat.tort = 1.5;
    cout << adat.tort << '\n';
    return 0;
}
```

## T2/5 – kimenet

Mi a kód pontos kimenete?

```cpp
#include <iostream>
using namespace std;
int szam = 5;
void kiir() { cout << szam << " "; }
int main() {
    int szam = 10;
    {
        int szam = 20;
        cout << szam << " ";
        kiir();
    }
    cout << szam << '\n';
    return 0;
}
```

## T2/6 – hibakeresés

Mi a fő hiba, és mi a legkisebb helyes javítás? Ne feltételezd, hogy a sikeres fordítás bizonyítja a helyességet.

```cpp
#include <iostream>
using namespace std;
struct Meres {
    double ertek;
}
int main() {
    Meres adat{2.5};
    cout << adat.ertek << '\n';
    return 0;
}
```

## T2/7 – hibakeresés

Mi a fő hiba, és mi a legkisebb helyes javítás? Ne feltételezd, hogy a sikeres fordítás bizonyítja a helyességet.

```cpp
#include <iostream>
using namespace std;
struct Meres { double ertek; };
int main() {
    Meres adat{2.5};
    Meres* mutato = &adat;
    cout << mutato.ertek << '\n';
    return 0;
}
```

## T2/8 – hibakeresés

Mi a fő hiba, és mi a legkisebb helyes javítás? Ne feltételezd, hogy a sikeres fordítás bizonyítja a helyességet.

```cpp
#include <iostream>
using namespace std;
union Szam { int egesz; double tort; };
int main() {
    Szam adat{};
    adat.tort = 2.5;
    cout << adat.egesz << '\n';
    return 0;
}
```

## T2/9 – hibakeresés

Mi a fő hiba, és mi a legkisebb helyes javítás? Ne feltételezd, hogy a sikeres fordítás bizonyítja a helyességet.

```cpp
#include <iostream>
using namespace std;
int main() {
    {
        int darab = 3;
    }
    cout << darab << '\n';
    return 0;
}
```

## T2/10 – hibakeresés

Mi a fő hiba, és mi a legkisebb helyes javítás? Ne feltételezd, hogy a sikeres fordítás bizonyítja a helyességet.

```cpp
#include <iostream>
using namespace std;
struct Meres { double ertek; };
int main() {
    const int meret = 2;
    Meres adatok[meret] = {{3.0}, {5.0}};
    double osszeg = 0.0;
    for (int i = 0; i <= meret; ++i) {
        osszeg += adatok[i].ertek;
    }
    cout << osszeg << '\n';
    return 0;
}
```
