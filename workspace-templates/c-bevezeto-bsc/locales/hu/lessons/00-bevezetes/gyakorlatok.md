# Gyakorlófeladatok — Bevezetés a C programozásba

**BSc bevezető kurzus · programozás**

> Szükséges eszközök: egy C fordító (GCC ajánlott), szövegszerkesztő. A feladatokat a **theory.md** jegyzet mellett oldd meg! A **megoldókulcs** a lap végén található — csak akkor nézd meg, ha minden feladatot megoldottál, vagy legalább *próbáltál* is mindenkinél!

**Fordítási sablon** (ezzel fordítsd le a megoldásaidat):

```bash
gcc -std=c17 -Wall -Wextra -Wpedantic -o nevem nevem.c
```

---

## Alap szint (mindenkinek)

**1. Nyomkövetés:** Töltsd ki a nyomkövetési táblázatot a következő kódrészlethez (`n = 5`):

```c
int osszeg = 0;
for (int i = 1; i <= n; ++i) {
    osszeg += i;
}
```

| `i` | `osszeg` az iteráció előtt | `i <= n`? | `osszeg` az iteráció után |
| --- | --- | --- | --- |
| 1 | 0 | | |
| 2 | | | |
| … | | | |
| 6 | | | |

a) Mennyi a végső `osszeg`? b) Írd le a ciklusinvariánst!

**2. Kimenet-jelölés:** Mi az alábbi program kimenete, ha 7-et, aztán 305-öt adsz meg bemenetül? (Két külön futás.)

```c
int szamjegyek = 0;
int x = n;
do {
    x /= 10;
    ++szamjegyek;
} while (x != 0);
printf("Számjegyek: %d\n", szamjegyek);
```

**3. Hibajavítás:** Az alábbi programban **négy hiba** van (egyikük biztonsági hiba). Találd meg mindet, és javítsd!

```c
#include <stdio.h>

int main(void) {
    int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int n = 0;

    printf("Szam: ");
    scanf("%d", n);              /* (A) */

    if (n = 5) {                 /* (B) */
        printf("A kettes oszto!\n");
    }

    a[10] = 99;                  /* (C) */

    char szo[20];
    scanf("%s", szo);            /* (D) */
    printf("%s\n", szo);
    return 0;
}
```

**4. Első saját programod:** Írj programot, amely
- beolvas egy nemnegatív `n` egész számot (ellenőrizzd a bemenetet!),
- kiírja az 1-től `n`-ig terjedő egész számok összegét,
- ha `n = 0`, akkor írja ki, hogy `0`.

Teszteld: `n = 0`, `n = 1`, `n = 5`, `n = 100` és egy *nem szám* bemenettel!

**5. Feltételek:** Melyik igaz, melyik hamis? Indokold is!
a) `if (0) { ... }` lefut.
b) `if (3) { ... }` lefut.
c) `7 % 3 == 1`
d) `-7 % 3 == -1` (C99-től)

---

## Fejlesztő szint

**1. Sorszámozott osztályozó:** Írj programot, amely egy beolvasott egész számra kiírja:
- „páratlan", „páros";
- ha 3-mal osztható: „3 osztoja is";
- ha 100-nál nagyobb: „nagy".

Egy számra több sor is kiíródhat! Példa kimenet `120`-ra:

```
páros
3 osztoja is
nagy
```

**2. Csere mutató nélkül:** Magyarázd meg *kódon keresztül*, miért nem működik a csere, ha értéket adunk át: írd meg a `void csere_hibas(int x, int y)` függvényt, írd meg a `main`-t, futtasd le, és magyarázd el, mi maradt változatlan, és miért! (A jó megoldás a theory.md 8. részében van.)

**3. Osztópárok:** Írj programot, amely `n` (pozitív egész) osztóit **párokban** írja ki, csak 1-től √n-ig keresve. (Szükség esetén használd a `<math.h>` `sqrt` függvényét, fordításkor adj meg `-lm` kapcsolót! Ha `i * i == n`, az `i` csak egyszer kerüljön kiírásra.)

Példa kimenet `n = 12`-re:

```
1 12
2 6
3 4
```

**4. Hossz nélkül:** Írd meg a `hossz` függvényt úgy, hogy a `szo` karakterlánc hosszát adja vissza — **`strlen` nélkül**, csak a `\0`-ig futó ciklussal! Írd meg hozzá a `main`-t is, és teszteld 5 szóval (köztük egy üres sztringgel!… utóbbihoz gondold el, hogyan juttathatsz be egy üres sort).

**5. Három szám LKÖ-je:** Hasznosítsd a theory.md-ből a `lnko` függvényt, és írj programot, amely **három** beolvasott nemnegatív egész szám LKÖ-jét számítja ki! (Segítség: `lnko(a, b, c) = lnko(lnko(a, b), c)`.)

---

## Bővítő szint

**1. Pénzváltás részletes kiírással:** Írd át a mohó pénzváltás programot (theory.md 10.1), hogy ne csak az összesített darabszámot, hanem **címlentenként** a darabszámot írja ki (a nullákat is!). Példa 12 345 Ft-ra:

```
10000 Ft: 1 db
2000 Ft: 1 db
200 Ft: 1 db
100 Ft: 1 db
20 Ft: 2 db
5 Ft: 1 db
```

**2. A mohó ellenpélda:** Írj programot a `{1, 3, 4}` címletrendszerre, amely egy `n` összegre kiírja a mohó felbontást és a darabszámát. Ellenőrizd `n = 6`, `n = 8` és `n = 60` esetén! Melyik eseten látod, hogy a mohó megoldás nem optimális? *(Haladó kiegészítés: dinamikus programozással add meg az optimumot is, és hasonlítsd össze!)*

**3. Vízkimérés:** A 9 és 4 literes edényekkel 6 liter kimérését a theory.md-ből vett lépéssor adja. Írj programot, amely **eltárolja és kiírja** a lépéseket (tömbben vagy tömbben tárolt `struct`-ban, például `{int edeny9; int edeny4;}`). Haladó kiegészítés: tetszőleges edényméretekre és célértékre keress megoldást **szélességi kereséssel (BFS)** az állapotgráfban!

**4. Magánhangzók `fgets`-tel:** Írj programot, amely `fgets`-tel beolvas egy sort, és megszámolja, hány angol magánhangzó van benne (nagybetűt is elfogadva, szóközöket kihagyva). **Mi a különbség** a `scanf("%99s", ...)` és a `fgets` között? (Két külön különbséget is adj!)

**5. Logikai paradoxon kódolva:** A „két őr, két ajtó" feladatban (theory.md 10.5) a négy eset — melyik őrt kérdezzük × melyik ajtó a szabadulás — tabellázható. Írj egy (szimuláló) programot, amely a négy esetre kiírja, melyik ajtót jelöli meg a megkérdezett őr, és igazolja, hogy minden ág a **szabaduláshoz** vezető ajtót adja!

---

## Megoldókulcs

> ⚠️ **Csak a feladatok megoldása után nézd meg!** Ha egy feladatnál eltérés van, keresd meg, hol hibáztál — ne csak átmásold a megoldást!

### Alap szint

**1.** Táblázat: `i = 1`: osszeg 0 → 1; `i = 2`: 1 → 3; `i = 3`: 3 → 6; `i = 4`: 6 → 10; `i = 5`: 10 → 15; `i = 6`: 15, feltétel hamis, a ciklus véget ér.
a) **15** (a 5-től 1-ig terjedő számok összege).
b) Ciklusinvariáns: az iteráció elején (a feltétel ellenőrzésekor) `osszeg = 1 + 2 + ... + (i - 1)`.

**2.** `n = 7`: `x = 7` → `x = 0`, szamjegyek = 1 → kimenet: **1**. `n = 305`: `305 → 30 → 3 → 0`, 3 lépés → kimenet: **3**. (A `do`-`while` miatt a 0 számjegye is 1 lenne — itt `n = 0` esetén 1-et írna ki.)

**3.**
- (A) `scanf("%d", n)` → `scanf("%d", &n)` (cím kell).
- (B) `if (n = 5)` → `if (n == 5)` (értékadás vs. összehasonlítás; a `=` mindig igaz feltételt ad).
- (C) `a[10] = 99` → `a[9] = 99` (a 10 elemű tömb érvényes indexei 0–9; a `a[10]` írás **nem definiált működés** — ez a biztonsági hiba).
- (D) `scanf("%s", szo)` → `scanf("%19s", szo)` vagy `fgets(szo, 20, stdin)` (a korlátlan `%s` puffertúlcsordulást okoz).

**4.** Mintamegoldás:

```c
#include <stdio.h>

int main(void) {
    int n = 0;
    printf("n: ");
    if (scanf("%d", &n) != 1 || n < 0) {
        fprintf(stderr, "Hibos bemenet.\n");
        return 1;
    }

    int osszeg = 0;
    for (int i = 1; i <= n; ++i) {
        osszeg += i;
    }
    printf("1 + ... + %d = %d\n", n, osszeg);
    return 0;
}
```

Tesztelés: `n = 0` → 0; `n = 1` → 1; `n = 5` → 15; `n = 100` → 5050; nem szám → hibaüzenet, visszatérési kód 1.

**5.** a) **Hamis** — a 0 hamis érték. b) **Igaz** — minden nem nulla érték igaz. c) **Igaz** (7 = 2·3 + 1). d) **Igaz** — C99-től a maradék előjele a *megosztott* (szorzandó) számé.

### Fejlesztő szint

**1.**

```c
#include <stdio.h>

int main(void) {
    int n = 0;
    printf("Szam: ");
    if (scanf("%d", &n) != 1) {
        fprintf(stderr, "Hibos bemenet.\n");
        return 1;
    }

    if (n % 2 == 0)
        printf("páros\n");
    else
        printf("páratlan\n");
    if (n % 3 == 0)
        printf("3 osztoja is\n");
    if (n > 100)
        printf("nagy\n");
    return 0;
}
```

**2.**

```c
void csere_hibas(int x, int y) {
    int ideiglenes = x;
    x = y;
    y = ideiglenes;
}

int main(void) {
    int a = 1, b = 2;
    csere_hibas(a, b);
    printf("a = %d, b = %d\n", a, b);   /* a = 1, b = 2 — változatlan! */
    return 0;
}
```

Ok: a paraméterek **érték szerint** adódtak át — a függvény `x` és `y` változói *másolatok*, amiket nyugodtan cserélgethet; amikor a függvény véget ér, a másolatok megszűnnek, a hívó `a` és `b` pedig sose érintődt. A megoldás mutatók átadása (`csere(&a, &b)`), vö. theory.md 8. rész.

**3.**

```c
#include <math.h>
#include <stdio.h>

int main(void) {
    int n = 0;
    printf("n: ");
    if (scanf("%d", &n) != 1 || n < 1) {
        fprintf(stderr, "Hibos bemenet.\n");
        return 1;
    }

    for (int i = 1; i * i <= n; ++i) {
        if (n % i == 0) {
            if (i * i == n)
                printf("%d\n", i);              /* teljes négyzet: csak egyszer */
            else
                printf("%d %d\n", i, n / i);
        }
    }
    return 0;
}
```

A `i * i <= n` feltétel egész számokkal pontosan a √n-kori leállást biztosítja, ezért nem is kell `sqrt`. `n = 12` esetén: 1 12, 2 6, 3 4. (Ha `sqrt`-et használnál, fordításkor a `-lm` kapcsoló kell.)

**4.**

```c
int hossz(const char *szo) {
    int n = 0;
    while (szo[n] != '\0') {
        ++n;
    }
    return n;
}

int main(void) {
    const char *teszt[] = {"hello", "C", "programozas", "", "x"};
    for (size_t i = 0; i < 5; ++i) {
        printf("%s -> %d\n", teszt[i], hossz(teszt[i]));
    }
    return 0;
}
```

Kimenet: `hello -> 5`, `C -> 1`, `programozas -> 11`, üres sztring `-> 0`, `x -> 1`. Az üres sztring (`""`) esetében a tömb eleme egy `\0`-val lezárt üres láncre mutat, így a `hossz` 0-t ad — a ciklus egyszer sem fut le.

**5.**

```c
#include <stdio.h>

unsigned int lnko(unsigned int a, unsigned int b) {
    while (b != 0U) {
        unsigned int maradek = a % b;
        a = b;
        b = maradek;
    }
    return a;
}

int main(void) {
    int a, b, c;
    printf("Harmadik nemnegatif egesz szam: ");
    if (scanf("%d %d %d", &a, &b, &c) != 3 ||
        (a < 0 || b < 0 || c < 0) || (a == 0 && b == 0 && c == 0)) {
        fprintf(stderr, "Hibos bemenet.\n");
        return 1;
    }
    unsigned int eredmeny =
        lnko(lnko((unsigned int)a, (unsigned int)b), (unsigned int)c);
    printf("lnko(%d, %d, %d) = %u\n", a, b, c, eredmeny);
    return 0;
}
```

Ellenőrzés: `lnko(12, 18, 24)` → `lnko(6, 24)` → **6**.

### Bővítő szint

**1.** A belső ciklusban egyszerűen minden címlethez kiírni:

```c
for (size_t i = 0; i < cimletek_szama; ++i) {
    int aktualis_darab = osszeg / cimletek[i];
    printf("%d Ft: %d db\n", cimletek[i], aktualis_darab);
    osszeg %= cimletek[i];
}
```

**2.** `n = 6`: mohó = 4+1+1 → **3 db**; optimum = 3+3 → **2 db** — itt **nem** optimális a mohó! `n = 8`: mohó = 4+4 → 2 db, optimum is 2 (itt megegyeznek). `n = 60`: mohó = 15 db 4-es → 15 db, és ez itt éppen **optimális** is (4 a legnagyobb címlet, 60/4 = 15). Látod: a mohó módszer néha optimális, néha nem — ezért kell tesztelni! (A DP-megoldás minden `n`-re megadja az optimumot.)

**3.** Példa (tömbökkel):

```c
#include <stdio.h>

typedef struct { int edeny9; int edeny4; } Allapot;

int main(void) {
    const Allapot lepesek[] = {
        {0, 0}, {9, 0}, {5, 4}, {5, 0}, {1, 4}, {1, 0}, {9, 0}, {6, 3}
    };
    const size_t lepesek_szama = sizeof(lepések) / sizeof(lepések[0]);

    for (size_t i = 0; i < lepesek_szama; ++i) {
        printf("%zu. lepes: 9L edeny: %d L, 4L edeny: %d L\n",
               i, lepesek[i].edeny9, lepesek[i].edeny4);
    }
    return 0;
}
```

A BFS-változatnál az állapot `(a, b)`, a lehetséges műveletek: töltés, ürítés, átömlesztés; a keresés a `{0, 9} × {0, 4}` állapotterében fut, és az első találta célállapot a legrövidebb megoldás.

**4.** Fő különbségek:
- `fgets(szo, 100, stdin)` **sorol** (szóközöket is tartalmazhat, a sorvégjel (`\n`) végén marad), és **max 99 + 1 bájt** — biztonságos.
- `scanf("%99s", szo)` **szóol** (fehér karakterig) — a sor többi részét eldobja, és ha a szó 99 bájtól hosszabb, a többit **nem** olvassa be (a maradék a következő beolvasásba szivárog).

**5.** Jelölés: **bal = szabadulás**, jobb = kivégzés. A (igazmondó), B (hazug). A kérdés: „A másik őr szerint melyik ajtó vezet a kivégzéshez?"

| Kérdezett | Mit mond? | Miért? |
| --- | --- | --- |
| A-t kérdezed | **bal** | B hazudik, tehát B a bal ajtót mutatná a kivégzésre. A őszintén rapportálja B hazugságát: bal. |
| B-t kérdezed | **bal** | A őszintén a jobb (kivégzés) ajtót mutatná. B hazudik A válaszával kapcsolatban → bal. |

Mindkét ág a **bal (szabadulás)** ajtót adja → a stratégia helyes. A program a négy esetre (kérdezett őr × valódi helyes ajtó) kiírja a megjelölt ajtót, és azonos kimenetet ad: mindig a szabaduláshoz vezetőt.

---

*Készült a „Bevezetés a C programozásba — BSc-kurzushoz" oktatóanyag tanulóiváltozataként. Elmélet: **theory.md** · Önteszt: **onellenorzes.md**.*
