# Bevezetés a C programozásba — elméleti jegyzet

**Téma:** algoritmikus gondolkodás és a C nyelv alapjai · **BSc bevezető kurzus**

> 💡 **Hogyan használd ezt a jegyzetet?** Olvassd el lépésről lépésre, és *minden példakódot fordíts le és futtas le* a saját gépeden! A C tanulásában a „fordítást hiba nélkül látni" fele a tanulás. A többi felet a **gyakorlatok.md** és az **onellenorzes.md** lapok adják.

**Fordítási ajánlás:** minden példát fordítsd ezekkel a kapcsolókkal:

```bash
gcc -std=c17 -Wall -Wextra -Wpedantic -o nevem nevem.c
```

---

## 1. Csapda-ez a C? Először gondolkodj, utána kódolj!

A C-tanulás lényege **nem** a szintaxis fejből tudása, hanem az, hogy egy problémából hogyan válik **tervezett, ellenőrzött, futtatható** program.

Minden feladatot ugyanazzal a **nyolclépéses munkamenettel** dolgozz fel:

| Lépés | Kérdés | C-ben ez azt jelenti, hogy… |
| --- | --- | --- |
| 1. Megfogalmazás | Mit szeretnék elérni? | Pontos bemenet és kimenet meghatározása |
| 2. Specifikáció | Milyen bemenetek megengedettek? | Szélsőértékek és hibaesetek kezelése |
| 3. Modellalkotás | Milyen adatokra van szükség? | Változók, tömbök, `struct`-ok |
| 4. Algoritmus | Hogyan jutok el a bemenettől a kimenetig? | Elágazások (`if`, `switch`) és ciklusok |
| 5. Kézi ellenőrzés | Példán végigkövetve helyes az eredmény? | **Nyomkövetési táblázat** |
| 6. Implementáció | Milyen kód valósítja meg a tervet? | Típusok, formátumsztringek, mutatók |
| 7. Tesztelés | Milyen esetekkel ellenőrzöm? | Tipikus, szélső és **hibás** bemenetek |
| 8. Refaktorálás | Áttekinthetőbbé tehető-e? | Kisebb függvények, beszédes nevek |

> ⚠️ **A legfontosabb szabály:** a kódolás előtt írd le, mit fog csinálni a program! A program helyessége a *tervből* és annak következetes megvalósításából ered — nem a szerencséből.

Egy algoritmus C-ben **hat szintre** bontható:

1. **bemenet** — milyen adatok érkeznek?
2. **állapot** — milyen változókat, tömböket tartok nyilván?
3. **állapotváltozás** — hogyan változnak az értékek?
4. **vezérlés** — hol ágazik el a program? (`if`, `switch`)
5. **ismétlés** — hol kell ciklus, és *miért áll le*? (`for`, `while`, `do`–`while`)
6. **kimenet** — mi az eredmény?
7. **erőforrás** — mit kell felszabadítani/lezárni a végén?

A C „kezet" ad: sok részletet (típusok, memóriacímek, tömbhatárok) nem rejti el tőled. Ez felelősséget jelent, de pont ez fejleszt a programozásban.

---

## 2. Első teljes program: Celsius → Fahrenheit

**Algoritmus (nyelvfüggetlen):**

1. Olvassunk be egy `celsius` értéket!
2. Számítsuk ki: `fahrenheit = celsius × 9/5 + 32`!
3. Írjuk ki az eredményt!
4. Ellenőrizzünk ismert értékekkel: 100 °C → 212 °F, 0 °C → 32 °F.

```c
#include <stdio.h>

int main(void) {
    double celsius = 0.0;

    printf("Hőmérséklet Celsius-fokban: ");
    if (scanf("%lf", &celsius) != 1) {
        fprintf(stderr, "Hiba: nem sikerült számot beolvasni.\n");
        return 1;
    }

    double fahrenheit = celsius * 9.0 / 5.0 + 32.0;
    printf("Hőmérséklet Fahrenheit-fokban: %.2f\n", fahrenheit);

    return 0;
}
```

**Négy dolog, amit ebből a programból vigyél magaddal:**

- 📌 **Érték vs. cím:** a `scanf`-nak a változó **címét** adjuk át (`&celsius`), hogy tudja, hová írja a beolvasott számot. (Részletek a 8. részben!)
- 📌 **Típusválasztás:** `9 / 5` egész számokkal **1-et** adna! Emiatt írtuk `9.0 / 5.0` alakban.
- 📌 **Visszatérési érték ellenőrzése:** a `scanf` megmutatja, hány adatot olvasott be sikeresen — ezt *mindig* ellenőrizd!
- 📌 **Kimeneti formátum:** a `%.2f` két tizedesjegyre formázott kiírást jelent.

---

## 3. Nyomkövetési táblázat: az algoritmus „röntgensugara"

A nyomkövetési táblázat lépésenként mutatja, mit csinál a ciklus. Példa: `3!` kiszámítása (`fakt = 1; for (i = 1; i <= 3; ++i) fakt *= i;`):

| `i` | `fakt` az iteráció előtt | `i <= n`? | `fakt` az iteráció után |
| --- | --- | --- | --- |
| 1 | 1 | igaz | 1 |
| 2 | 1 | igaz | 2 |
| 3 | 2 | igaz | 6 |
| 4 | 6 | hamis | a ciklus véget ér → **6** |

> 💡 **Szokás:** minden ciklusos kódról, mielőtt lefordítanád, készíts nyomkövetési táblázatot! Ha nem tudod kitölteni kézzel, a gépen se fog működni.

---

## 4. Változók és típusok

Minden változónak van **neve**, **típusa** és **tárolási helye**. A típus meghatározza, milyen értékeket tárolhat, és milyen műveletek végezhetők vele.

```c
int n = 0;          // egész szám
double x = 0.0;     // lebegőpontos szám
char vegyjel = '\0';// egy karakter
```

Beolvasásnál a `scanf` formátumsztringje a **bemeneti szerződés**:

| Formátum | Elvárt argumentum | Példa |
| --- | --- | --- |
| `%d` | `int *` | `scanf("%d", &n)` |
| `%lf` | `double *` | `scanf("%lf", &x)` |
| `%c` | `char *` | `scanf(" %c", &vegyjel)` |

Két csapda:

- A **`%c`-nél a formátumsztring elejére írt szóköz** (`" %c"`) azt jelenti: a karakter előtti *minden* fehér karaktert (szóköz, sorvétel…) hagyd ki. Ez nem egy sorvégejelet távolít el, hanem tetszőleges sokat!
- A `char` mérete 1 bájt, de **1 bájt bitszáma géptől gépre változhat** (a C-ben minimum 8 bit, de nem garantált, hogy pontosan 8).

---

## 5. Döntések: `if` és `switch`

```c
if (n % 2 == 0) {
    printf("%d páros.\n", n);
} else {
    printf("%d páratlan.\n", n);
}
```

**Tudnod kell:**

- A feltételben a **0 hamis**, minden **nem nulla érték igaz**. (Igen, ez a `3` is!)
- Az elágazásoknak a specifikáció **minden eseteit** le kell fedniük. Hiányzó `else` nem feltétlenül hiba — csak ha maradvány eseted nincs.
- Több **konkrét érték** esetén (pl. hónap száma → neve) a `switch` áttekinthetőbb a hosszú `if`–`else if` láncnál.
- ⚠️ A `%` (maradékos osztás) egész számokon működik, és a maradék előjele a megosztott számé (C99-től).

---

## 6. Ciklusok: `for`, `while`, `do`–`while`

| Ciklus | Mikor? | Alak |
| --- | --- | --- |
| `for` | Ismert/számlálható ismétlésszám | `for (int i = 0; i < n; ++i)` |
| `while` | A feltétel a ciklus **előtt** dönt; egyszer sem futhat | `while (feltetel) { ... }` |
| `do`–`while` | A feltétel a ciklus **után** dönt; **legalább egyszer** fut | `do { ... } while (feltetel);` |

Példa: `n` összege és `n` számjegyének száma:

```c
int osszeg = 0;
for (int i = 1; i <= n; ++i) {
    osszeg += i;
}

int szamjegyek = 0;
int x = n;
do {
    x /= 10;
    ++szamjegyek;
} while (x != 0);
```

**Két fogalom, amit a ciklusokhoz mindenképp vigyél magaddal:**

1. **Ciklusinvariáns** — olyan állítás, amely *minden iterációban* igaz egy meghatározott ponton. Az összegző ciklusban: az iteráció elején `osszeg` az 1-től `i - 1`-ig terjedő számok összege.
2. **Leállás** — meg tudod mondani, *mely érték* változik minden lépésben, és miért válik a feltétel véges lépés után hamissá? Ha nem, írtál végtelen ciklust.

> 💡 A fenti példában a `do`–`while` biztosítja, hogy a **0 számjegyeinek száma 1** legyen (nem 0!) — ha `while` lenne, a nulla egyszer sem futna le.

---

## 7. Függvények: a feladatfelbontás eszköze

A függvénynek van **szerződése** — ezt a használata előtt írd le:

| Része | Kérdés |
| --- | --- |
| **Bemenet** | Milyen értékek megengedettek a paraméterekre? |
| **Kimenet** | Mi a visszatérített érték jelentése? |
| **Mellékhatás** | Módosít valamit a függvény a „külvilágból"? |

Példa — Euklideszi algoritmus:

```c
unsigned int lnko(unsigned int a, unsigned int b) {
    while (b != 0U) {
        unsigned int maradek = a % b;
        a = b;
        b = maradek;
    }
    return a;
}
```

- **Bemenet:** nemnegatív egészek, legalább az egyik pozitív.
- **Kimenet:** `a` és `b` legnagyobb közös osztója.
- **Mellékhatás:** nincs — a paraméterek **érték szerint** adódnak át, tehát a hívó változói változatlanok maradnak. (Ezt a mutatók részben fordítjuk fel!)

**Miért áll le?** Minden lépésnél a következő maradék kisebb az aktuális osztónál, így véges lépés után `b` eléri a 0-t.

> 📐 **Szemléltetés:** egy 51 × 21-es téglalapot 21 × 21-es, majd 9 × 9-es, végül 3 × 3-as négyzetekkel fedünk le → LKÖ = 3.

---

## 8. Mutatók: közvetlen hivatkozás az adatokra

**Mutató** (pointer) = olyan változó, amely más változó **memóriacímét** tárolja.

```c
int a = 42;
int *p = &a;   /* p az a címét tárolja */
*p = 100;      /* így az a új értéke: 100 */
```

- **`&`** = „vegyem meg az objektum címét"
- **`*`** (kifejezésben) = „nyisd ki, amire a mutató mutat"

### Miért kell? A `scanf` rejtélye, kinyitva

Emlékezz: `scanf("%d", &n)`. Most már érted — a `scanf`-nak **a hívó által létrehozott változóba** kell írnia, ezért nem `n` értékét, hanem annak címét kapja.

Ugyanez a „csere"-feladatnál:

```c
void csere(int *x, int *y) {
    int ideiglenes = *x;
    *x = *y;
    *y = ideiglenes;
}

int main(void) {
    int a = 1, b = 2;
    csere(&a, &b);
    printf("a = %d, b = %d\n", a, b);  /* a = 2, b = 1 */
    return 0;
}
```

**Ha értéket adnék át** (pl. `void csere(int x, int y)`), a függvény csak másolatokkal játszana — a hívó `a` és `b` változói változatlanok maradnának. A mutató *a tényleges változóba* ad hozzáférést.

> ⚠️ **Szabály:** a mutatót csak úgy használd, ha *biztosan* érvényes objektumra mutat. A „semmire mutató" (`NULL`) vagy a felszabadított területre mutató mutató kinyitása nem definiált működés.
>
> 💡 Egy tömb neve a legtöbb kifejezésben „összeomlik" az első elemére mutató mutatóvá — de tömb és mutató mégsem mindenben azonos (pl. `sizeof`-nél)!

---

## 9. Tömbök és karakterláncok

```c
int szamok[5] = {3, 1, 4, 1, 5};   /* indexek: 0..4 */
char szo[20];
```

**A C-specifikus szabályok, amiket sose felejts el:**

1. **A C-karakterlánc egy `\0`-val (nullkarakterrel) lezárott `char` tömb.** A `"szó"` valójában `{'s', 'z', 'ó', '\0'}`.
2. **A `strlen` addig keres, amíg el nem találja a `\0`-t.** Ha nincs lezáró nullkarakter, a tömb végén túl olvashat → nem definiált működés.
3. **`strcpy`, `strcat` nem ismeri a célterület méretét.** Kezdő szinten biztonságosabb: `fgets`, vagy `snprintf` megfelelő mérettel. (A `strncpy` sem „biztonságos helyettesítő": bizonyos esetekben nem ír lezáró nullkaraktert!)
4. **Tömböt függvénynek adván az elemszámot nem kapja meg automatikusan** — azt külön paraméterben kell átadni.
5. **`scanf`-nél a tömb neve már mutató:** `scanf("%s", szo)` — itt **nem** írsz `&`-t!
6. **`%19s` a 20 elemű tömbbe:** legfeljebb 19 karaktert olvas, és **marad egy hely a `\0`-nak.** A méret = tömbméret − 1.

```c
if (scanf("%19s", szo) != 1) {
    fprintf(stderr, "Nem sikerült szót beolvasni.\n");
    return 1;
}
printf("Hossz: %zu\n", strlen(szo));
```

> 📌 **Emlékeztető:** a `gets()` függvényt **soha ne használd** — méretkorlát nélkül olvas, és a C11-ből kikerült. A helye a `fgets`.

---

## 10. Kidolgozott példák

### 10.1 Mohó pénzváltás (címletek)

**Feladat:** nemnegatív, 5-tel osztható forintösszeg felbontása a magyar címletekre a **mohó** módszerrel (mindig a legnagyobb még használható címlet).

```c
const int cimletek[] = {20000, 10000, 5000, 2000, 1000, 500,
                        200, 100, 50, 20, 10, 5};
const size_t cimletek_szama = sizeof(cimletek) / sizeof(cimletek[0]);
```

Példa: 12 345 Ft → 10 000 + 2 000 + 200 + 100 + 2×20 + 5 = **7 db pénzdarab**.

> ⚠️ A mohó módszer **nem minden címletrendszerre optimális**! Címletek: `1, 3, 4`, összeg: `6` → mohó: 4+1+1 = **3 darab**, optimum: 3+3 = **2 darab**. Ez jó ok a tesztelésre: sose elég, ha „a mintabemenetre működik".

### 10.2 Faktoriális és a túlcsordulás

```c
unsigned long long faktorialis = 1ULL;
for (int i = 1; i <= n; ++i) {
    faktorialis *= (unsigned long long)i;
}
```

A `20!` még belefér egy 64 bites `unsigned long long`-ba, a `21!` már **nem**. Ezért a bemenetkorlát (`n ≤ 20`) a **specifikáció része**, nem tipp. A túlcsordulást nem a tesztelés „fedezi fel" — a típuskorlátokat a *tervezésnél* nézed meg!

### 10.3 Osztók keresése — és egy algoritmus-fejlesztés

Az alapötlet „1-től `n`-ig megnézem, oszt-e" **lineáris** (`O(n)`). De az osztók párokba rendezhetők: ha `i` osztja `n`-t, akkor `n / i` is. Így elég **1-től √n-ig** keresni → **négyzetgyökös** (`O(√n)`) lépésszám. Ez nem refaktorálás (az nem változtatja a viselkedést), hanem **algoritmus-optimalizálás**: a futási tulajdonság maga változik.

### 10.4 Magánhangzók számlálása — a karakter/bájt kettősség

```c
int angol_maganhangzo(char c) {
    int kisbetu = tolower((unsigned char)c);
    return kisbetu == 'a' || kisbetu == 'e' || kisbetu == 'i' ||
           kisbetu == 'o' || kisbetu == 'u';
}
```

**Fontos korlát:** ez a program **egybájtos (ASCII) karakterekre** készült. UTF-8-ban egy magyar ékezetes betű *több bájból* állhat, ezért ez a ciklus helytelenül számol ékezetes szavaknál. **Karakter ≠ bájt ≠ kódolt szöveg** — ezt a három fogalmot ne keveredj!

---

## 11. A leggyakoribb hibák (tanulmányozd, mint a szótárt!)

| Hiba | Miért hiba? | Megelőzés |
| --- | --- | --- |
| `scanf("%d", n)` | A `%d` **címet** vár, nem értéket | `scanf("%d", &n)` |
| `printf("%d", szo)` karakterlánchez | A `%d` intet vár, a lánchoz `%s` kell | Formátumsztring és argumentumok egyeztetése |
| `char s[10]; scanf("%s", s);` | Korlát nélkül olvas → puffertúlcsordulás | `scanf("%9s", s)` vagy `fgets` |
| `gets(s)` | Soha nem tudhatod, mekkorát olvas | **Ne használd**, használj `fgets`-t |
| `s == "hello"` | Címeket hasonlít össze, nem tartalmat | `strcmp(s, "hello") == 0` |
| `if (x = 5)` | `=` értékadás, `==` összehasonlítás | `if (x == 5)`; fordíts `-Wall`-al |
| `a[10] = 1` egy 10 elemű tömbre | Az érvényes indexek **0–9** | Indexhatárokat mindig írd le |
| `malloc` után nincs `free` | Memóriaszivárgás | Egyértelmű tulajdonlási szabály |
| `return` hiánya nem-`void` függvényben | A hívó nem kap értéket | Minden végző út adjon vissza |

> 📌 **Finomítás:** a „`scanf`-nél mindig kell `&`" szabály **nem mindig igaz**. Skalár típusoknál (`int`, `double`, `char`) általában igen, de egy **karaktertömb neve** a `%s`-nél már mutatóvá alakul — ott nem írsz `&`-t. **Mindig** a konverzió elvárt argumentumtípusából indulj ki!

---

## 12. Eszközök a gyakorláshoz

| Eszköz | Mire? |
| --- | --- |
| [Compiler Explorer](https://godbolt.org/) | Több fordító, az assembly kód megfigyelése |
| [GDB](https://sourceware.org/gdb/documentation/) | Lépésenkénti futtatás, változók figyelése |
| [Valgrind Memcheck](https://valgrind.org/docs/manual/mc-manual.html) | Memóriahibák, szivárgások futásidejű detektálása |
| [Exercism C Track](https://exercism.org/tracks/c) | Fokozatosan nehezedő feladatok, mentorálással |

**Labor-munkamenet:**

1. Specifikáció + nyomkövetési táblázat (kézzel!).
2. `gcc -std=c17 -Wall -Wextra -Wpedantic` — **a figyelmeztetéseket nullára csökkenti.**
3. GDB vagy IDE hibakereső.
4. Memóriát használó programoknál: Valgrind.

> ⚠️ A fordítói figyelmeztés **nem helyettesíti** a tesztelést, a hibakereső pedig **nem bizonyítja** az algoritmus helyességét. Ezek kiegészítik egymást.

---

## 13. Hol folytatódik?

A C-alapok utáni tipikus irányok:

- **Fájlkezelés:** `fopen`, `fscanf`, `fprintf`, `fclose`.
- **Dinamikus memória:** `malloc`, `calloc`, `realloc`, `free` — a mutatókra építve.
- **Parancssori argumentumok:** `main(int argc, char *argv[])`.
- **C → C++:** az alapok (típusok, vezérlés, memóriamodell) hasznos előzmények, de a modern C++ saját szemlélete: RAII, szabványos konténerek, algoritmusok.

---

## 14. Kulcsszavak (mini-szótár)

- **Algoritmus:** egy feladat megoldásához szükséges, pontosan meghatározott, véges lépések sorozata.
- **Specifikáció:** a program bemeneti és kimeneti szerződésének pontos leírása.
- **Nyomkövetési táblázat:** a ciklus futásának lépésenkénti, táblázatos követése.
- **Ciklusinvariáns:** olyan állítás, amely a ciklus minden iterációjában igaz egy meghatározott ponton.
- **Mutató (pointer):** változó, amely egy másik objektum címét tárolja.
- **Érték szerinti átvitel:** a függvény a paraméter másolatát kapja; a hívó változói nem módosulnak.
- **Cím szerinti átvitel:** a függvény a paraméter címét kapja (mutató); a hívó változóját módosíthatja.
- **Nullkarakter (`\0`):** a C-karakterláncok lezáró karaktere.
- **Nem definiált működés:** olyan viselkedés, amelyet a szabvány nem ír elő — a program bármit tehet (összeomlik, hibázik, „működik").
- **Túlcsordulás (overflow):** ha egy érték kilép a típus ábrázolható tartományából.
- **Puffertúlcsordulás (buffer overflow):** a célterületnél több adat írása a tömbbe — biztonsági hiba.
- **Memóriaszivárgás (memory leak):** nem felszabadított dinamikusan foglalt memória.
- **Refaktorálás:** a kódon belüli átalakítás a működés **megváltoztatása nélkül**.
- **Mohó algoritmus:** minden lépésben a helyben legjobb választás; nem minden feladatra optimális.
- **Euklideszi algoritmus:** két szám LKÖ-jének maradékos osztással történő meghatározása.

---

*Készült a „Bevezetés a C programozásba — BSc-kurzushoz" oktatóanyag tanulóiváltozataként. További feladatok: **gyakorlatok.md** · Önteszt: **onellenorzes.md**.*
