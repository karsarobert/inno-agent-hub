# Leckék lépésről lépésre

> Minden parancsot a **munkaterület alatti terminálban** írj be.
> Minden `.cpp` fájl a munkaterület **gyökerében** van — így nem kell elérési utat írni.

---

## 1. lecke — elsõ program (megfigyelés)

A kód **adott** a `L01_elso_program.cpp`-ben. Nem kell megírni, csak **megfigyelni**.

**1. Fordítsd le:**
```
g++ -Wall -o L01 L01_elso_program.cpp
```

**2. Futtasd:**
```
./L01
```

**3. Mit figyelj meg?**
- Mi jelenik meg a képernyőn?
- Miért kellett **előbb lefordítani**? (Miben más ez, mint a Python?)
- Mi a szerepe a `#include <iostream>` sornak? A `using namespace std;`-nek? A `return 0;`-nak?
- Távolítsd el a `using namespace std;` sort, és változtasd a `cout`-ot `std::cout`-ra. Fordul-e még? Mit veszel észre?

---

## 2. lecke — preprocesszor és makrók

A `L02_preprocesszor_makro.cpp` már van. **Előbb JÓSOLD MEG a kimenetet**, aztán futtasd.

**1. Fordítsd és futtasd:**
```
g++ -Wall -o L02 L02_preprocesszor_makro.cpp
./L02
```

**2. Nézd meg a preprocesszált kimenetet:**
A `-E` kapcsoló megmutatja, mivé válik a kód a fordítás előtt.
```
g++ -E L02_preprocesszor_makro.cpp
```

**3. Mit figyelj meg?**
- Mivé alakul a `PRINT_MY_NAME` és `MY_FAV_NUM` makró a preprocesszált kimenetben?
- Mennyi extra kód került a rövid program elé (az `iostream`-ból)?
- Változtasd meg a `MY_FAV_NUM`-ot 7-re, fordítsd újra — mi történik?

---

## 3. lecke — feltételes fordítás

**1. Előbb jósold meg, mi múlik a `DEBUG` makrón.**

**2. Fordítás DEBUG nélkül:**
```
g++ -Wall -o L03 L03_felteteles_makro.cpp
./L03
```

**3. Fordítás DEBUG-gal:**
```
g++ -Wall -DDEBUG -o L03 L03_felteteles_makro.cpp
./L03
```

**4. Mit figyelsz meg?**
- Melyik üzenet jelenik meg a két esetben? Miért?
- A `DEBUG` makró **fordításidőben** dönt — nem futásidőben. Látod a különbséget az `#ifdef` és egy sima `if` között?
- **SQUARE csapda:** a makró itt `((x)*(x))` — zárójelezett, ezért `SQUARE(1+2)=9`. Próbáld ki a zárójelek nélkül (`(x) * (x)` helyett `x * x`). Mi az eredmény? Miért?

---

## 4. lecke — I/O, string, hibakeresés

**1. Jósold meg, milyen kimenetet kapsz a bemenetedre.**

**2. Fordítsd és futtasd:**
```
g++ -Wall -o L04 L04_io_string_hibakes.cpp
./L04
```

**3. Mit figyelsz meg?**
- Mi az operátor iránya `cout <<` és `cin >>` esetén? Miért ellentétesek?
- Mit ad a `nev.size()`? Mi a `to_string()` szerepe?
- Mit csinál az `assert`? Próbálj meg 0 vagy 200 életkort megadni — mi történik? Miért áll le a program?

---

## Hasznos ismétlés

Általános fordítás-futtatás mintája (bármelyik `.cpp`-re):
```
g++ -Wall -o <kimeneti_nev> <fajl>.cpp
./<kimeneti_nev>
```
> Mindig **-Wall**-lal fordíts! Így meglátod azokat a figyelmeztetéseket, amik segítenek a hibák elkerülésében.
