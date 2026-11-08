# CPP_09 – Rögzített záróteszt

20 kérdés, egyenként. Az első érdemi válasz számít. T1-ben A/B/C/D választ adj. T2/1–5 előtt ne futtasd a programot. T2/6–10-ben az ok és a célt megőrző legkisebb javítás is kell. Nincs hallgatói megoldókulcs.

## T1/1

Melyik deklaráció jelöl konstruktort az Ablak osztályban?

A) void Ablak(int szelesseg);

B) Ablak(int szelesseg);

C) int Ablak(int szelesseg);

D) bool ablak(int szelesseg);

## T1/2

Van argumentum nélküli és két egész paraméteres konstruktor. Melyiket választja a Gep gep(4, 7);?

A) Mindig az argumentum nélkülit.

B) Először az argumentum nélkülit, majd külön a kétparaméterest.

C) A main választása alapján bármelyiket.

D) A két egész paraméterest.

## T1/3

Mit jelent a szam(7) a Beallitas() : szam(7) {} konstruktorban?

A) A szam adattag inicializálását a törzs végrehajtása előtt.

B) Egy szam nevű szabad függvény hívását.

C) A konstruktor végén végzett értékadást.

D) Hét külön objektum létrehozását.

## T1/4

A Tag elso; majd Tag masodik; sorrendben deklarált tagoknál melyik inicializálódik előbb, ha a listában masodik(...), elso(...) áll?

A) A masodik, mert a listában előrébb áll.

B) Amelyik több argumentumot kap.

C) Az elso, a tagok deklarációs sorrendje miatt.

D) Ezt a fordító futásonként véletlenül dönti el.

## T1/5

Mi igaz a feltetel ? balErtek : jobbErtek kifejezésre?

A) A feltétel után csak a kiválasztott ág értékelődik ki.

B) Mindkét ág mindig kiértékelődik.

C) Az eredmény mindig bool.

D) Csak cout mellett használható.

## T1/6

Miért választhat a konstruktor hibás adatból alapértéket, míg egy későbbi beállítás elutasít és megőrzi az előző értéket?

A) Mert a C++ minden hibás konstruktori adatot automatikusan nulláz.

B) Mert a setter nem olvashat privát adatot.

C) Mert a bool eredmény automatikusan visszavonja a módosítást.

D) Mert ezek a feladatban választott eltérő szabályok a kezdőállapotra és a már létező állapotra.

## T1/7

A díjszámító a küldemény grammLeker() lekérdezőjét hívja. Mi ennek az előnye?

A) Ez megszünteti az összes objektummásolatot.

B) A számítás a nyilvános felületre támaszkodik, a belső tárolás részleteit nem kell elérnie.

C) Így a privát adat automatikusan nyilvánossá válik.

D) A két osztálynak ugyanazokat az adattagokat kell tárolnia.

## T1/8

Melyik eset kompozíció?

A) Egy függvény helyi int változója összead két számot.

B) Két osztály neve ugyanazzal a betűvel kezdődik.

C) Az Eredmenylap adattagként Versenyzo objektumokat tartalmaz.

D) Egy szabad függvény kiír egy kapott számot.

## T1/9

Négy férőhelyű tárolóban darab = 2. Mely indexeket használja az aktuális lista és összegzés?

A) 0, 1, 2, 3, mert mindegyik tömbelem létrejött.

B) 0 és 1.

C) 1 és 2.

D) Csak a 2-es index.

## T1/10

Mit enged a const Jegypenztar* mutatón keresztüli hozzáférés?

A) Megfelelő const lekérdezők hívását a meglévő objektumon.

B) A privát darabszám közvetlen átírását.

C) Minden módosító művelet hívását.

D) Automatikus másolat készítését minden nyíl operátornál.

## T2/1 – kimenet

Mi a pontos kimenet?

```cpp
#include <iostream>
using namespace std;

class Munka {
private:
    int idotartam;
public:
    Munka() : idotartam(2) {}
    Munka(int ujIdotartam) : idotartam(ujIdotartam) {}
    int idotartamLeker() const { return idotartam; }
};
int main() {
    const Munka elso;
    const Munka masodik(7);
    cout << elso.idotartamLeker() << ' ' << masodik.idotartamLeker() << '\n';
    return 0;
}
```

## T2/2 – kimenet

Mi a pontos kimenet?

```cpp
#include <iostream>
using namespace std;

class Ablak {
private:
    int szam;
public:
    Ablak(int bemenet) : szam(bemenet > 0 ? bemenet : 3) {}
    int szamLeker() const { return szam; }
};
int main() {
    const Ablak elso(0);
    const Ablak masodik(5);
    cout << elso.szamLeker() << ' ' << masodik.szamLeker() << '\n';
    return 0;
}
```

## T2/3 – kimenet

Mi a pontos kimenet?

```cpp
#include <iostream>
using namespace std;

class Munka {
private:
    int idotartam;
public:
    Munka(int ujIdotartam) : idotartam(ujIdotartam) {}
    int idotartamLeker() const { return idotartam; }
};
class Gep {
private:
    int mennyiseg;
public:
    Gep(int ujSzam) : mennyiseg(ujSzam) {}
    int osszes(Munka munka) const { return munka.idotartamLeker() * mennyiseg; }
};
int main() {
    const Munka munka(6);
    const Gep gep(3);
    cout << gep.osszes(munka) << '\n';
    return 0;
}
```

## T2/4 – kimenet

Mi a pontos kimenet?

```cpp
#include <iostream>
using namespace std;

class Bejegyzes {
private:
    int szam;
public:
    Bejegyzes() : szam(2) {}
    Bejegyzes(int ujSzam) : szam(ujSzam) {}
    int szamLeker() const { return szam; }
};
class Tarolo {
private:
    Bejegyzes adatok[3];
    int aktiv;
public:
    Tarolo() : aktiv(1) { adatok[0] = Bejegyzes(9); }
    int osszes() const {
        int eredmeny = 0;
        for (int i = 0; i < aktiv; ++i) { eredmeny += adatok[i].szamLeker(); }
        return eredmeny;
    }
};
int main() {
    const Tarolo tarolo;
    cout << tarolo.osszes() << '\n';
    return 0;
}
```

## T2/5 – kimenet

Mi a pontos kimenet?

```cpp
#include <iostream>
using namespace std;

class Beallitas {
private:
    int szam;
public:
    Beallitas(int bemenet) : szam(bemenet) {}
    void ertekBeallit(int ujSzam) { szam = ujSzam; }
    int szamLeker() const { return szam; }
};
Beallitas novel(Beallitas beallitas) {
    beallitas.ertekBeallit(beallitas.szamLeker() + 2);
    return beallitas;
}
int main() {
    Beallitas eredeti(4);
    const Beallitas masolat = novel(eredeti);
    cout << eredeti.szamLeker() << ' ' << masolat.szamLeker() << '\n';
    Beallitas* cel = &eredeti;
    cel->ertekBeallit(9);
    cout << eredeti.szamLeker() << ' ' << masolat.szamLeker() << '\n';
    return 0;
}
```

## T2/6 – hibakeresés

A cél: egy Ablak létrehozása után 7 legyen lekérdezhető. Mi a fő hiba és a legkisebb javítás?

```cpp
#include <iostream>
using namespace std;

class Ablak {
private:
    int szam = 2;
public:
    void Ablak() { szam = 7; }
    int szamLeker() const { return szam; }
};
int main() {
    const Ablak ablak;
    cout << ablak.szamLeker() << '\n';
    return 0;
}
```

## T2/7 – hibakeresés

A két tömbelem kezdeti időtartama legyen 0, a paraméteres létrehozást is meg kell tartani. Miért hibás a program, és hogyan javítanád?

```cpp
#include <iostream>
using namespace std;

class Munka {
private:
    int idotartam;
public:
    Munka(int ujIdotartam) : idotartam(ujIdotartam) {}
    int idotartamLeker() const { return idotartam; }
};
int main() {
    Munka munkak[2];
    cout << munkak[0].idotartamLeker() << ' ' << munkak[1].idotartamLeker() << '\n';
    return 0;
}
```

## T2/8 – hibakeresés

A Tag objektum közvetlenül a kapott értékkel jöjjön létre. Ne adj új alapértelmezett konstruktort a Tag típushoz. Miért nem elég a törzsbeli értékadás?

```cpp
#include <iostream>
using namespace std;

class Tag {
private:
    int szam;
public:
    Tag(int bemenet) : szam(bemenet) {}
    int szamLeker() const { return szam; }
};
class Tarolo {
private:
    Tag tag;
public:
    Tarolo(int bemenet) { tag = Tag(bemenet); }
    int szamLeker() const { return tag.szamLeker(); }
};
int main() {
    const Tarolo tarolo(6);
    cout << tarolo.szamLeker() << '\n';
    return 0;
}
```

## T2/9 – hibakeresés

A cél kizárólag az aktív elemek összege. Minden tömbelem inicializált; nem fordítási hibát keresünk. Mi a fő hiba és a legkisebb javítás?

```cpp
#include <iostream>
using namespace std;

class Tarolo {
private:
    int adatok[3] = {10, 2, 2};
    int aktiv = 1;
public:
    int osszes() const {
        int eredmeny = 0;
        for (int i = 0; i < 3; ++i) { eredmeny += adatok[i]; }
        return eredmeny;
    }
};
int main() {
    const Tarolo tarolo;
    cout << tarolo.osszes() << '\n';
    return 0;
}
```

## T2/10 – hibakeresés

Csak nemnegatív beállítás engedélyezett. Elutasításkor az előző érték maradjon meg. Mi a fő hiba és a legkisebb javítás?

```cpp
#include <iostream>
using namespace std;

class Beallitas {
private:
    int szam;
public:
    Beallitas(int bemenet) : szam(bemenet) {}
    bool ertekBeallit(int ujSzam) {
        szam = ujSzam;
        if (ujSzam < 0) { return false; }
        return true;
    }
    int szamLeker() const { return szam; }
};
int main() {
    Beallitas beallitas(5);
    cout << beallitas.ertekBeallit(-1) << ' ' << beallitas.szamLeker() << '\n';
    return 0;
}
```
