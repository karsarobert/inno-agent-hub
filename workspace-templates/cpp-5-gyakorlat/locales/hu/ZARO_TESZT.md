# CPP_05 – ZH-felkészítő záróteszt

A tutor a kérdéseket **egyenként**, a megadott sorrendben teszi fel. A kérdések
előre rögzítettek; ne cseréld le őket másik feladatra.

# T1 – 10 feleletválasztós kérdés a mai elméleti anyagból

## T1/1
Mi a függvényekre bontás egyik legfontosabb előnye?

A) Minden változó automatikusan globálissá válik.  
B) Csökkenthető a kódismétlés, és a részfeladatok külön kezelhetők.  
C) A programnak több `main()` függvénye lehet.  
D) A program minden esetben automatikusan gyorsabb lesz.

## T1/2
Mit nevezünk **paraméternek**?

A) A függvény definíciójában szereplő bemeneti változót.  
B) A függvényhíváskor átadott konkrét értéket.  
C) A `return` által visszaadott értéket.  
D) A függvény lokális eredményét.

## T1/3
Mit nevezünk **argumentumnak**?

A) A függvény visszatérési típusát.  
B) A függvény definíciójában szereplő paraméternevet.  
C) A függvényhíváskor átadott konkrét értéket vagy kifejezést.  
D) Csak egész szám lehet argumentum.

## T1/4
Mi a `return` szerepe egy értéket visszaadó függvényben?

A) Kiírja az eredményt a képernyőre.  
B) Visszaad egy értéket a hívó kódnak, és befejezi az adott függvényhívást.  
C) Újraindítja a függvényt.  
D) Csak a `main()` függvényben használható.

## T1/5
Mit jelent a `void` visszatérési típus?

A) A függvény nem ad vissza értéket.  
B) A függvénynek nem lehet paramétere.  
C) A függvény nem tartalmazhat `if` vagy ciklus utasítást.  
D) A függvény nem hívható meg a `main()`-ből.

## T1/6
Mi történik érték szerinti paraméterátadáskor egy egyszerű `int` változóval?

A) A paraméter az eredeti változóval azonos objektum lesz.  
B) A függvény automatikusan megkapja a változó címét.  
C) A paraméter az argumentum értékének másolatát kapja.  
D) Az argumentum `const` lesz.

## T1/7
Mire szolgál a függvényprototípus?

A) Előre közli a fordítóval a függvény nevét, visszatérési típusát és paramétertípusait.  
B) Lefuttatja a függvényt a `main()` előtt.  
C) Helyettesíti a függvény definícióját minden esetben.  
D) Memóriát foglal a függvény eredményének.

## T1/8
Melyik állítás igaz egy függvény lokális változójára?

A) A program minden függvényéből közvetlenül elérhető.  
B) Csak abban a hatókörben érhető el, ahol létrehoztuk.  
C) Mindig `static` típusú.  
D) Csak tömb lehet.

## T1/9
Melyik állítás írja le helyesen az `#include <iostream>` és a `using namespace std;` kapcsolatát?

A) Mindkettő pontosan ugyanazt végzi.  
B) Az `#include <iostream>` teszi elérhetővé az I/O deklarációkat; a `using namespace std;` lehetővé teszi, hogy az `std` neveit például `std::cout` helyett `cout` alakban is megtalálja a névkeresés.  
C) A `using namespace std;` tölti be az `<iostream>` fejlécet.  
D) Az `<iostream>` egy névtér neve.

## T1/10
Miért szerepelhet a programban az `#include <cmath>`?

A) A `for` ciklus használatához kötelező.  
B) A `main()` függvényt definiálja.  
C) Matematikai szabványos könyvtári függvényeket, például a `sqrt` használatához szükséges deklarációkat tesz elérhetővé.  
D) A `using namespace std;` helyett használjuk.

# T2 – 10 kódértési és hibakeresési feladat

## T2/1 – kimenetjóslás
Mi a pontos kimenet?

```cpp
#include <iostream>
using namespace std;

int dupla(int szam) {
    return szam * 2;
}

int main() {
    cout << dupla(4) + dupla(3) << '\n';
    return 0;
}
```

## T2/2 – kimenetjóslás
Mi a pontos kimenet?

```cpp
#include <iostream>
using namespace std;

void modosit(int szam) {
    szam = 100;
}

int main() {
    int ertek = 10;
    modosit(ertek);
    cout << ertek << '\n';
    return 0;
}
```

## T2/3 – kimenetjóslás
Mi a pontos kimenet?

```cpp
#include <iostream>
using namespace std;

int negyzet(int x) {
    return x * x;
}

int negyzetOsszeg(int a, int b) {
    return negyzet(a) + negyzet(b);
}

int main() {
    cout << negyzetOsszeg(3, 4) << '\n';
    return 0;
}
```

## T2/4 – kimenetjóslás
Mi a pontos kimenet?

```cpp
#include <iostream>
using namespace std;

int osszeg(const int* adatok, int meret) {
    int eredmeny = 0;
    for (int i = 0; i < meret; ++i) {
        eredmeny += adatok[i];
    }
    return eredmeny;
}

int main() {
    int szamok[4] = {2, 5, 3, 10};
    cout << osszeg(szamok, 4) << '\n';
    return 0;
}
```

## T2/5 – kimenetjóslás
Mi a pontos kimenet?

```cpp
#include <iostream>
using namespace std;

void novel(int* ertek) {
    *ertek += 1;
}

int main() {
    int x = 5;
    novel(&x);
    cout << x << '\n';
    return 0;
}
```

## T2/6 – hibakeresés
A program ebben a formában nem fordul le. Mi a fő probléma, és mi a legkisebb javítás?

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << osszead(2, 3) << '\n';
    return 0;
}

int osszead(int a, int b) {
    return a + b;
}
```

## T2/7 – hibakeresés
Mi a hiba a függvényben?

```cpp
void osszead(int a, int b) {
    return a + b;
}
```

## T2/8 – hibakeresés
A program nem fordul le. Miért?

```cpp
#include <iostream>
using namespace std;

int terulet(int a, int b) {
    return a * b;
}

int main() {
    cout << terulet(4) << '\n';
    return 0;
}
```

## T2/9 – hibakeresés
A program lefordulhat, de a ciklus hibás és veszélyes. Mi a probléma?

```cpp
#include <iostream>
using namespace std;

int osszeg(const int* adatok, int meret) {
    int eredmeny = 0;

    for (int i = 0; i <= meret; ++i) {
        eredmeny += adatok[i];
    }

    return eredmeny;
}
```

## T2/10 – hibakeresés
A kódban szerepel az `<iostream>`, mégsem használható így a `cout`. Mi hiányzik vagy mit kell módosítani?

```cpp
#include <iostream>

int main() {
    cout << "Szia!" << '\n';
    return 0;
}
```
