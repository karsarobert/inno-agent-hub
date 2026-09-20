# CPP_03 – záróteszt

Ezt a tesztet a tutor kérdésenként vezeti. Ne olvasd előre megoldásként; a cél,
hogy az órai munka után saját válaszokat adj.

## T1 – feleletválasztós kérdések

### 1.
Mikor hajtódik végre egy `if` blokk törzse?

A) Mindig egyszer.
B) Ha a feltétel igaz.
C) Ha a feltétel hamis.
D) Csak akkor, ha van `else` ág.

### 2.
Mit biztosít egy szabályos `if–else` szerkezet egyetlen lefutás során?

A) Mindkét ág lefut.
B) Egyik ág sem futhat le.
C) Pontosan az egyik ág fut le.
D) Az `else` mindig előbb fut le.

### 3.
Mi történik egy `if / else if / else` láncban, ha egy feltétel igaz lesz?

A) Az ahhoz tartozó ág lefut, a lánc későbbi ágai kimaradnak.
B) Minden későbbi feltételt is kötelezően végrehajt.
C) Az `else` ág is lefut.
D) A program automatikusan befejeződik.

### 4.
Mi a `break` tipikus szerepe egy `switch` `case` ágában?

A) Újrakezdi a `switch`-et.
B) Leállítja az egész programot.
C) Megakadályozza, hogy a végrehajtás a következő `case` ágakba továbbfusson.
D) Hamissá teszi a `switch` feltételét.

### 5.
Melyik állítás igaz a `do–while` ciklusra?

A) A törzs soha nem fut le, ha a feltétel kezdetben hamis.
B) A törzs legalább egyszer lefut.
C) Csak páros számú iterációja lehet.
D) Nincs benne feltétel.

### 6.
Miért kényelmes gyakran a `for` ciklus számlálásos feladatoknál?

A) Mert nem lehet benne elágazás.
B) Mert mindig pontosan tízszer fut.
C) Mert nincs szüksége ciklusváltozóra.
D) Mert az inicializálás, feltétel és léptetés egy helyen látható.

## T2 – kimenetjóslás

### 1.
Mi a pontos kimenet?

```cpp
#include <iostream>

int main() {
    const int szam = 5;

    if (szam > 3) {
        std::cout << "A\n";
    }

    std::cout << "C\n";
}
```

### 2.
Mi a pontos kimenet?

```cpp
#include <iostream>

int main() {
    const int pontszam = 60;

    if (pontszam >= 80) {
        std::cout << "Kiváló\n";
    } else if (pontszam >= 60) {
        std::cout << "Megfelelő\n";
    } else {
        std::cout << "Fejlesztendő\n";
    }
}
```

### 3.
Mi a pontos kimenet?

```cpp
#include <iostream>

int main() {
    const int ertek = 2;

    switch (ertek) {
        case 1:
            std::cout << "Egy\n";
            break;
        case 2:
            std::cout << "Kettő\n";
            break;
        default:
            std::cout << "Más\n";
            break;
    }
}
```

### 4.
Mi a pontos kimenet?

```cpp
#include <iostream>

int main() {
    int szam = 1;
    int osszeg = 0;

    while (szam <= 3) {
        osszeg += szam;
        ++szam;
    }

    std::cout << osszeg << '\n';
}
```

### 5.
Mi a pontos kimenet?

```cpp
#include <iostream>

int main() {
    int szam = 4;
    const int utolso_szam = 3;

    do {
        std::cout << szam << '\n';
        ++szam;
    } while (szam <= utolso_szam);
}
```

### 6.
Mi a pontos kimenet?

```cpp
#include <iostream>

int main() {
    for (int szam = 1; szam <= 6; ++szam) {
        if (szam % 2 == 0) {
            std::cout << szam << ' ';
        }
    }
    std::cout << '\n';
}
```
