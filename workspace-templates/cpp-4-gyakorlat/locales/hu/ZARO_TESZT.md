# CPP_04 – záróteszt

Ezt a tesztet a tutor kérdésenként vezeti. Ne olvasd előre megoldásként; a cél,
hogy az órai kódírás után saját válaszokat adj.

## T1 – feleletválasztós kérdések

### 1.
Egy ötelemű tömb deklarációja:

```cpp
int szamok[5] = {10, 20, 30, 40, 50};
```

Melyik az utolsó érvényes index?

A) `5`  
B) `1`  
C) `4`  
D) `0`

### 2.
Mit ad meg a `&szam` kifejezés?

```cpp
int szam = 42;
```

A) A `szam` értékét.  
B) A `szam` memóriahelyének címét.  
C) A `szam` típusát.  
D) A `szam` értékének másolatát.

### 3.
Mit tárol a `mutato` változó?

```cpp
int szam = 42;
int* mutato = &szam;
```

A) Közvetlenül a `42` értéket.  
B) A `szam` változó nevét szövegként.  
C) A `szam` típusát.  
D) A `szam` memóriahelyének címét.

### 4.
Mit jelent ebben a példában a `*mutato` kifejezés?

```cpp
int szam = 42;
int* mutato = &szam;
```

A) A mutatóban tárolt címen lévő `int` objektumot érjük el.  
B) Új mutatót hozunk létre.  
C) Lekérdezzük a `mutato` memóriahelyének címét.  
D) A mutatót automatikusan `nullptr` értékre állítjuk.

### 5.
Melyik megoldás használja biztonságosan a `mutato` változót, ha az lehet `nullptr`?

A)
```cpp
std::cout << *mutato << '\n';
```

B)
```cpp
if (mutato == nullptr) {
    std::cout << *mutato << '\n';
}
```

C)
```cpp
if (mutato != nullptr) {
    std::cout << *mutato << '\n';
}
```

D)
```cpp
if (*mutato != 0) {
    std::cout << mutato << '\n';
}
```

### 6.
Melyik állítás helyes?

```cpp
int szamok[3] = {10, 20, 30};
int* mutato = szamok;
```

A) A `szamok` tömb és a `mutato` változó ugyanaz az objektum.  
B) A `mutato` a tömb első elemére mutat; a tömb ettől még nem válik mutatóvá.  
C) A `mutato` automatikusan a tömb utolsó elemére mutat.  
D) A `mutato` a tömb elemszámát tárolja.

## T2 – kimenetjóslás

### 1.
Mi a pontos kimenet?

```cpp
#include <iostream>

int main() {
    int a = 5;
    int b = 9;
    int* mutato = &a;

    *mutato = 7;
    mutato = &b;
    *mutato += 3;

    std::cout << a << ' ' << b << '\n';
}
```

### 2.
Mi a pontos kimenet?

```cpp
#include <iostream>

int main() {
    int szamok[4] = {10, 20, 30, 40};
    int* mutato = szamok;

    std::cout << *(mutato + 2) << '\n';
}
```

### 3.
Mi a pontos kimenet?

```cpp
#include <iostream>

int main() {
    int szamok[4] = {5, 10, 15, 20};
    int* mutato = szamok;

    *(mutato + 1) = 42;

    std::cout << szamok[1] << '\n';
}
```

### 4.
Mi a pontos kimenet?

```cpp
#include <iostream>

int main() {
    const int meret = 4;
    int szamok[meret] = {2, 4, 6, 8};
    int* mutato = szamok;
    int osszeg = 0;

    for (int i = 0; i < meret; ++i) {
        osszeg += *(mutato + i);
    }

    std::cout << osszeg << '\n';
}
```

### 5.
Mi a pontos kimenet?

```cpp
#include <iostream>

int main() {
    int szam = 8;
    int* mutato = nullptr;

    if (mutato != nullptr) {
        std::cout << *mutato << '\n';
    } else {
        std::cout << "ures\n";
    }

    mutato = &szam;

    if (mutato != nullptr) {
        std::cout << *mutato << '\n';
    }
}
```

### 6.
Mi a pontos kimenet?

```cpp
#include <iostream>

int main() {
    const int meret = 4;
    int szamok[meret] = {1, 2, 3, 4};
    int* mutato = szamok;

    for (int i = 0; i < meret; ++i) {
        if (*(mutato + i) % 2 == 0) {
            *(mutato + i) *= 10;
        }
    }

    for (int i = 0; i < meret; ++i) {
        std::cout << szamok[i] << ' ';
    }
    std::cout << '\n';
}
```
